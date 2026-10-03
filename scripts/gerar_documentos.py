"""Gera os PDFs da base de conhecimento técnica da Construtora Apollo S.A.

Uso:  python scripts/gerar_documentos.py  (gera em documentos/)
"""
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import (
    KeepTogether, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle,
)

from conteudo_documentos import AVISO_FICTICIO, DATA_REVISAO, DOCUMENTOS, EMPRESA

SAIDA = Path(__file__).resolve().parent.parent / "documentos"

AZUL = colors.HexColor("#1F3B57")
CINZA = colors.HexColor("#5A6775")

estilos = getSampleStyleSheet()
EST = {
    "titulo": ParagraphStyle("titulo", parent=estilos["Title"], fontSize=15,
                             leading=19, textColor=AZUL, alignment=TA_LEFT,
                             spaceAfter=6),
    "meta": ParagraphStyle("meta", parent=estilos["Normal"], fontSize=9,
                           leading=12, textColor=CINZA),
    "aviso": ParagraphStyle("aviso", parent=estilos["Normal"], fontSize=8,
                            leading=10, textColor=CINZA, fontName="Helvetica-Oblique"),
    "secao": ParagraphStyle("secao", parent=estilos["Heading2"], fontSize=12,
                            leading=15, textColor=AZUL, spaceBefore=12, spaceAfter=4),
    "sub": ParagraphStyle("sub", parent=estilos["Heading3"], fontSize=10.5,
                          leading=13, textColor=AZUL, spaceBefore=8, spaceAfter=3),
    "corpo": ParagraphStyle("corpo", parent=estilos["Normal"], fontSize=10,
                            leading=13.5, spaceAfter=5),
    "item": ParagraphStyle("item", parent=estilos["Normal"], fontSize=10,
                           leading=13.5, leftIndent=12, spaceAfter=2),
    "cel": ParagraphStyle("cel", parent=estilos["Normal"], fontSize=8.8, leading=11),
    "cel_h": ParagraphStyle("cel_h", parent=estilos["Normal"], fontSize=8.8,
                            leading=11, fontName="Helvetica-Bold", textColor=colors.white),
}


def _tabela(cabecalho, linhas):
    largura_total = A4[0] - 4 * cm
    n = len(cabecalho)
    if n == 2:
        larguras = [0.18, 0.82]
    elif n == 3:
        larguras = [0.18, 0.16, 0.66] if cabecalho[1] == "Intervalo" else [0.25, 0.45, 0.30]
    else:
        larguras = [0.12, 0.33, 0.08, 0.47]
    dados = [[Paragraph(c, EST["cel_h"]) for c in cabecalho]]
    dados += [[Paragraph(str(c), EST["cel"]) for c in linha] for linha in linhas]
    tabela = Table(dados, colWidths=[largura_total * w for w in larguras], repeatRows=1)
    tabela.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), AZUL),
        ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#B8C4D0")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F2F5F8")]),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]))
    return tabela


def _cabecalho_rodape(doc_info):
    def desenhar(canvas, doc):
        canvas.saveState()
        canvas.setFont("Helvetica", 7.5)
        canvas.setFillColor(CINZA)
        canvas.drawString(2 * cm, A4[1] - 1.2 * cm,
                          f"{EMPRESA} · {doc_info['codigo']} · {doc_info['revisao']}")
        canvas.drawRightString(A4[0] - 2 * cm, 1.1 * cm, f"Página {doc.page}")
        canvas.restoreState()
    return desenhar


def gerar(doc_info):
    caminho = SAIDA / f"{doc_info['codigo']}.pdf"
    pdf = SimpleDocTemplate(
        str(caminho), pagesize=A4,
        leftMargin=2 * cm, rightMargin=2 * cm, topMargin=1.8 * cm, bottomMargin=1.8 * cm,
        title=f"{doc_info['codigo']} — {doc_info['titulo']}", author=EMPRESA,
    )
    historia = [
        Paragraph(doc_info["titulo"], EST["titulo"]),
        Paragraph(
            f"<b>Código:</b> {doc_info['codigo']} &nbsp;&nbsp; <b>Revisão:</b> "
            f"{doc_info['revisao']} ({DATA_REVISAO}) &nbsp;&nbsp; <b>Aplicação:</b> "
            f"{doc_info['aplicacao']}", EST["meta"]),
        Paragraph(f"<b>Emitente:</b> {EMPRESA} — Engenharia de Manutenção de Equipamentos",
                  EST["meta"]),
        Spacer(1, 4),
        Paragraph(AVISO_FICTICIO, EST["aviso"]),
        Spacer(1, 6),
    ]
    for numero, titulo, blocos in doc_info["secoes"]:
        cabeca = Paragraph(f"{numero} {titulo}", EST["secao"])
        elementos = []
        subtitulo_pendente = None
        for bloco in blocos:
            tipo = bloco[0]
            if tipo == "sub":
                subtitulo_pendente = Paragraph(f"{bloco[1]} {bloco[2]}", EST["sub"])
                continue
            inicio = len(elementos)
            if tipo == "p":
                elementos.append(Paragraph(bloco[1], EST["corpo"]))
            elif tipo == "lista":
                elementos += [Paragraph(item, EST["item"]) for item in bloco[1]]
                elementos.append(Spacer(1, 3))
            elif tipo == "tabela":
                elementos += [_tabela(bloco[1], bloco[2]), Spacer(1, 5)]
            else:
                raise ValueError(f"Bloco desconhecido: {tipo}")
            if subtitulo_pendente is not None:
                # mantém o subtítulo na mesma página do primeiro bloco
                elementos[inicio] = KeepTogether([subtitulo_pendente, elementos[inicio]])
                subtitulo_pendente = None
        # mantém o título junto do primeiro bloco da seção
        historia.append(KeepTogether([cabeca, elementos[0]]))
        historia += elementos[1:]
    desenho = _cabecalho_rodape(doc_info)
    pdf.build(historia, onFirstPage=desenho, onLaterPages=desenho)
    return caminho


if __name__ == "__main__":
    SAIDA.mkdir(exist_ok=True)
    for info in DOCUMENTOS:
        print("gerado:", gerar(info).name)
