"""Gera as tabelas operacionais da Construtora Apollo S.A. (dados fictícios).

Uso:  python scripts/gerar_dados.py  (gera em dados/)

Data de referência de todo o conjunto: 2026-09-28. O notebook usa essa
mesma data para calcular janelas de histórico, de forma que o resultado
não dependa do dia em que ele for executado.

Cenários plantados para os testes de comportamento (ordens_servico.csv):
- OS-2026-0101  EH-07  alarme TL-214 recorrente (3ª ocorrência hidráulica em 90 dias)
- OS-2026-0102  CB-12  relato vago ("barulho estranho na frente")
- OS-2026-0103  EH-15  equipamento inexistente; obra tem duas escavadeiras
- OS-2026-0104  TE-02  perda de potência com revisão R500 vencida
- OS-2026-0105  CR-04  falha de freio (TL-331) com peça principal sem estoque
- OS-2026-0106  TE-05  relato vazio (rejeitada antes de chamar o modelo)
"""
from pathlib import Path

import pandas as pd

SAIDA = Path(__file__).resolve().parent.parent / "dados"
DATA_REFERENCIA = "2026-09-28"
HORAS_POR_DIA = 9

# ----------------------------------------------------------------------
OBRAS = [
    ("OB-01", "Duplicação Rodoviária — Lote 2", "Sete Lagoas/MG", "ALM-01"),
    ("OB-02", "Alteamento de Barragem — Mina Serra Azul", "Itabirito/MG", "ALM-02"),
    ("OB-03", "Terraplenagem — Polo Industrial Oeste", "Betim/MG", "ALM-03"),
]

# id, tipo, fabricante, modelo, ano, obra, status, criticidade, horímetro, ficha
EQUIPAMENTOS = [
    ("EH-07", "Escavadeira hidráulica", "Caterpillar", "CAT 320", 2021, "OB-01", "Operando", "A", 7850, "FTM-CAT320"),
    ("EH-09", "Escavadeira hidráulica", "Caterpillar", "CAT 320", 2022, "OB-01", "Operando", "B", 5120, "FTM-CAT320"),
    ("EH-11", "Escavadeira hidráulica", "Caterpillar", "CAT 320", 2020, "OB-02", "Operando", "A", 9630, "FTM-CAT320"),
    ("EH-13", "Escavadeira hidráulica", "Caterpillar", "CAT 320", 2023, "OB-03", "Disponível", "B", 3210, "FTM-CAT320"),
    ("TE-02", "Trator de esteiras", "Caterpillar", "CAT D9T", 2019, "OB-02", "Operando", "A", 12480, "FTM-CATD9T"),
    ("TE-05", "Trator de esteiras", "Caterpillar", "CAT D9T", 2021, "OB-03", "Operando", "A", 8870, "FTM-CATD9T"),
    ("CR-03", "Carregadeira de rodas", "Caterpillar", "CAT 924H", 2018, "OB-01", "Operando", "B", 14320, "FTM-CAT924H"),
    ("CR-04", "Carregadeira de rodas", "Caterpillar", "CAT 924H", 2019, "OB-02", "Operando", "A", 11760, "FTM-CAT924H"),
    ("CR-06", "Carregadeira de rodas", "Caterpillar", "CAT 924H", 2017, "OB-03", "Disponível", "C", 16940, "FTM-CAT924H"),
    ("CB-12", "Caminhão basculante", "Mercedes-Benz", "MB Axor 3344 K", 2022, "OB-01", "Operando", "B", 4380, "FTM-MBCAM"),
    ("CB-14", "Caminhão basculante", "Mercedes-Benz", "MB 2726 K", 2020, "OB-01", "Operando", "B", 6720, "FTM-MBCAM"),
    ("CB-15", "Caminhão basculante", "Mercedes-Benz", "MB 2726 K", 2020, "OB-01", "Operando", "B", 6505, "FTM-MBCAM"),
    ("CB-21", "Caminhão basculante", "Mercedes-Benz", "MB Axor 3344 K", 2023, "OB-02", "Operando", "B", 2950, "FTM-MBCAM"),
    ("CB-22", "Caminhão basculante", "Mercedes-Benz", "MB Axor 3344 K", 2023, "OB-02", "Em manutenção", "B", 3010, "FTM-MBCAM"),
]

# ----------------------------------------------------------------------
ORDENS_SERVICO = [
    ("OS-2026-0101", "2026-09-28 07:40", "OB-01", "EH-07", "Operador de escavadeira",
     "Alarme TL-214 no painel. Depois de umas duas horas de trabalho a lança e o braço "
     "ficam lentos e sem força para escavar. De manhã, com a máquina fria, funciona normal."),
    ("OS-2026-0102", "2026-09-28 08:15", "OB-01", "CB-12", "Motorista",
     "Caminhão fazendo barulho estranho na frente."),
    ("OS-2026-0103", "2026-09-28 09:02", "OB-01", "EH-15", "Apontador",
     "Vazamento de óleo no cilindro da caçamba da escavadeira, pingando bastante no fim "
     "do turno."),
    ("OS-2026-0104", "2026-09-28 09:30", "OB-02", "TE-02", "Operador de trator",
     "Trator perdendo força para empurrar material na rampa. A rotação cai muito com a "
     "lâmina carregada e está saindo fumaça escura no escapamento."),
    ("OS-2026-0105", "2026-09-28 10:05", "OB-02", "CR-04", "Operador de carregadeira",
     "Pedal do freio ficando baixo e a carregadeira demorando para parar, principalmente "
     "com a caçamba cheia. Apareceu o alarme TL-331 no painel."),
    ("OS-2026-0106", "2026-09-28 10:20", "OB-03", "TE-05", "Operador de trator", ""),
]

# ----------------------------------------------------------------------
# Histórico de manutenção CORRETIVA. As revisões preventivas ficam em registro_preventivas.csv.
# ordem, equipamento, abertura, conclusão, tipo, sistema, alarme, serviço, peças, horas paradas
HISTORICO = [
    ("OS-2026-0047", "EH-07", "2026-06-02", "2026-06-02", "Corretiva", "Material rodante", "",
     "Ajuste da tensão da esteira esquerda.", "", 2),
    ("OS-2026-0071", "EH-07", "2026-08-14", "2026-08-14", "Corretiva", "Hidráulico", "TL-214",
     "Colmeia do arrefecedor de óleo hidráulico obstruída por lama: limpeza executada e "
     "nível do óleo completado com 20 litros.", "APL-10026", 6),
    ("OS-2026-0089", "EH-07", "2026-09-09", "2026-09-10", "Corretiva", "Hidráulico", "TL-214",
     "Alarme reincidente. Filtro de retorno do óleo hidráulico substituído; máquina "
     "testada por um turno sem alarme.", "APL-10021", 8),
    ("OS-2026-0028", "EH-11", "2026-05-10", "2026-05-10", "Corretiva", "Elétrico", "TL-402",
     "Bateria substituída após falha de partida.", "", 3),
    ("OS-2026-0081", "TE-02", "2026-09-02", "2026-09-02", "Corretiva", "Motor", "TL-108",
     "Alarme de restrição do filtro de ar. Elemento primário limpo com ar comprimido como "
     "medida provisória; revisão R500 pendente por indisponibilidade da máquina na frente "
     "de serviço.", "", 2),
    ("OS-2026-0054", "TE-05", "2026-06-15", "2026-06-15", "Corretiva", "Trem de força", "TL-342",
     "Limpeza do arrefecedor de óleo da transmissão.", "", 5),
    ("OS-2026-0041", "CR-03", "2026-05-28", "2026-05-28", "Corretiva", "Freios", "TL-335",
     "Ajuste do interruptor do freio de estacionamento.", "", 2),
    ("OS-2026-0016", "CR-04", "2026-04-03", "2026-04-03", "Corretiva", "Hidráulico", "TL-226",
     "Filtro de retorno hidráulico substituído.", "", 3),
    ("OS-2026-0009", "CB-12", "2026-02-12", "2026-02-12", "Corretiva", "Elétrico", "",
     "Lâmpada do farol dianteiro direito substituída.", "", 1),
    ("OS-2026-0084", "CB-14", "2026-08-25", "2026-08-25", "Corretiva", "Freios", "TL-350",
     "Vazamento na linha de ar do freio traseiro corrigido.", "", 4),
    ("OS-2026-0097", "CB-22", "2026-09-26", "", "Corretiva", "Trem de força", "",
     "Em andamento: substituição do conjunto de embreagem.", "", ""),
]

# ----------------------------------------------------------------------
PLANO_PREVENTIVA = [
    ("FTM-CAT320", "R250", 250), ("FTM-CAT320", "R500", 500), ("FTM-CAT320", "R1000", 1000),
    ("FTM-CAT320", "R2000", 2000), ("FTM-CAT320", "R3000", 3000), ("FTM-CAT320", "R6000", 6000),
    ("FTM-CATD9T", "R250", 250), ("FTM-CATD9T", "R500", 500),
    ("FTM-CATD9T", "R1000", 1000), ("FTM-CATD9T", "R2000", 2000),
    ("FTM-CAT924H", "R250", 250), ("FTM-CAT924H", "R500", 500),
    ("FTM-CAT924H", "R1000", 1000), ("FTM-CAT924H", "R2000", 2000),
    ("FTM-MBCAM", "R200", 200), ("FTM-MBCAM", "R300", 300),
    ("FTM-MBCAM", "R600", 600), ("FTM-MBCAM", "R1200", 1200),
]

# Fração do intervalo já consumida desde a última execução de cada revisão.
# Todas ficam em dia, exceto as exceções explícitas abaixo.
FRACOES_PADRAO = [0.45, 0.62, 0.38, 0.71, 0.55, 0.30]
EXCECOES_PREVENTIVA = {
    # TE-02: última R500 às 11.840 h; horímetro atual 12.480 h -> 640 h (> 550 h = vencida)
    ("TE-02", "R500"): 11840,
    ("TE-02", "R1000"): 11840,
    ("TE-02", "R250"): 12300,
}

# ----------------------------------------------------------------------
# código, descrição, referência do fabricante, ficha, {almoxarifado: saldo}, unidade, prazo (dias)
PECAS = [
    ("APL-10021", "Filtro de retorno do óleo hidráulico", "", "FTM-CAT320", {"ALM-01": 2, "ALM-02": 1}, "un", 7),
    ("APL-10022", "Kit de vedação do cilindro do braço", "", "FTM-CAT320", {"ALM-01": 1, "ALM-CEN": 1}, "un", 20),
    ("APL-10023", "Filtro de óleo do motor", "", "FTM-CAT320", {"ALM-01": 4, "ALM-02": 3, "ALM-03": 2}, "un", 5),
    ("APL-10024", "Filtro primário de combustível (separador de água)", "", "FTM-CAT320", {"ALM-01": 4, "ALM-02": 2}, "un", 5),
    ("APL-10025", "Filtro secundário de combustível", "", "FTM-CAT320", {"ALM-01": 4, "ALM-02": 2}, "un", 5),
    ("APL-10026", "Óleo hidráulico", "", "FTM-CAT320", {"ALM-01": 380, "ALM-02": 400, "ALM-03": 200}, "L", 3),
    ("APL-10027", "Mangueira de alta pressão do cilindro da caçamba", "", "FTM-CAT320", {"ALM-01": 1, "ALM-CEN": 2}, "un", 10),
    ("APL-10028", "Elemento primário do filtro de ar", "", "FTM-CAT320", {"ALM-01": 2, "ALM-02": 1}, "un", 7),
    ("APL-20011", "Elemento primário do filtro de ar", "", "FTM-CATD9T", {"ALM-02": 2, "ALM-03": 1}, "un", 7),
    ("APL-20012", "Elemento secundário do filtro de ar", "", "FTM-CATD9T", {"ALM-02": 1, "ALM-03": 1}, "un", 7),
    ("APL-20013", "Filtro primário de combustível (separador de água)", "", "FTM-CATD9T", {"ALM-02": 2, "ALM-03": 2}, "un", 7),
    ("APL-20014", "Filtro secundário de combustível", "", "FTM-CATD9T", {"ALM-02": 2, "ALM-03": 2}, "un", 7),
    ("APL-20015", "Filtro de óleo do motor", "", "FTM-CATD9T", {"ALM-02": 3, "ALM-03": 2}, "un", 7),
    ("APL-30011", "Filtro de óleo do motor", "269-8325", "FTM-CAT924H", {"ALM-01": 2, "ALM-02": 2}, "un", 7),
    ("APL-30012", "Filtro primário de combustível e separador de água", "326-1644", "FTM-CAT924H", {"ALM-02": 2}, "un", 7),
    ("APL-30013", "Filtro secundário de combustível", "308-7480", "FTM-CAT924H", {"ALM-02": 2}, "un", 7),
    ("APL-30014", "Elemento primário do filtro de ar", "256-7902", "FTM-CAT924H", {"ALM-02": 1}, "un", 7),
    ("APL-30015", "Elemento secundário do filtro de ar", "256-7903", "FTM-CAT924H", {"ALM-02": 1}, "un", 7),
    ("APL-30021", "Válvula de controle do freio de serviço", "144-8521", "FTM-CAT924H", {"ALM-02": 0, "ALM-CEN": 0}, "un", 15),
    ("APL-30022", "Sensor de pressão do óleo do freio", "290-5825", "FTM-CAT924H", {"ALM-02": 0, "ALM-CEN": 1}, "un", 10),
    ("APL-30023", "Bomba de engrenagem do freio e do ventilador", "299-3941", "FTM-CAT924H", {"ALM-CEN": 0}, "un", 30),
    ("APL-40011", "Filtro de óleo do motor", "", "FTM-MBCAM", {"ALM-01": 6, "ALM-02": 4}, "un", 5),
    ("APL-40012", "Filtro de combustível", "", "FTM-MBCAM", {"ALM-01": 6, "ALM-02": 4}, "un", 5),
    ("APL-40013", "Kit de lonas de freio dianteiro", "", "FTM-MBCAM", {"ALM-01": 2, "ALM-02": 1}, "un", 8),
    ("APL-40014", "Amortecedor dianteiro", "", "FTM-MBCAM", {"ALM-01": 0, "ALM-CEN": 2}, "un", 8),
    ("APL-40015", "Terminal de direção", "", "FTM-MBCAM", {"ALM-01": 1}, "un", 8),
]


def gerar():
    SAIDA.mkdir(exist_ok=True)

    obras = pd.DataFrame(OBRAS, columns=["obra_id", "nome", "municipio_uf", "almoxarifado_id"])

    equipamentos = pd.DataFrame(EQUIPAMENTOS, columns=[
        "equipamento_id", "tipo", "fabricante", "modelo", "ano_fabricacao", "obra_id",
        "status_operacional", "criticidade", "horimetro_atual", "ficha_tecnica"])

    ordens = pd.DataFrame(ORDENS_SERVICO, columns=[
        "os_id", "data_abertura", "obra_id", "equipamento_informado", "aberta_por", "relato"])

    historico = pd.DataFrame(HISTORICO, columns=[
        "ordem_id", "equipamento_id", "data_abertura", "data_conclusao", "tipo_manutencao",
        "sistema", "codigo_alarme", "descricao_servico", "pecas_utilizadas", "horas_parado"])

    plano = pd.DataFrame(PLANO_PREVENTIVA, columns=["ficha_tecnica", "revisao", "intervalo_horas"])

    registros = []
    for eq in EQUIPAMENTOS:
        eq_id, horimetro, ficha = eq[0], eq[8], eq[9]
        revisoes = [p for p in PLANO_PREVENTIVA if p[0] == ficha]
        for i, (_, revisao, intervalo) in enumerate(revisoes):
            if (eq_id, revisao) in EXCECOES_PREVENTIVA:
                ultima = EXCECOES_PREVENTIVA[(eq_id, revisao)]
            else:
                fracao = FRACOES_PADRAO[(i + len(eq_id) + horimetro) % len(FRACOES_PADRAO)]
                ultima = horimetro - round(intervalo * fracao)
            if ultima <= 0:
                continue  # revisão ainda não atingida pela primeira vez
            # data aproximada, considerando uso médio de 9 horas por dia
            dias_atras = round((horimetro - ultima) / HORAS_POR_DIA)
            data = (pd.Timestamp(DATA_REFERENCIA) - pd.Timedelta(days=dias_atras)).date()
            registros.append((eq_id, revisao, ultima, data.isoformat()))
    registro = pd.DataFrame(registros, columns=[
        "equipamento_id", "revisao", "horimetro_execucao", "data_execucao"])

    estoque = pd.DataFrame(
        [(cod, desc, ref, ficha, alm, saldo, un, prazo)
         for cod, desc, ref, ficha, saldos, un, prazo in PECAS
         for alm, saldo in saldos.items()],
        columns=["codigo_peca", "descricao", "ref_fabricante", "ficha_tecnica",
                 "almoxarifado_id", "saldo", "unidade", "prazo_reposicao_dias"])

    tabelas = {
        "obras.csv": obras, "equipamentos.csv": equipamentos,
        "ordens_servico.csv": ordens, "historico_manutencao.csv": historico,
        "plano_preventiva.csv": plano, "registro_preventivas.csv": registro,
        "estoque_pecas.csv": estoque,
    }
    for nome, df in tabelas.items():
        df.to_csv(SAIDA / nome, index=False, encoding="utf-8")
        print(f"gerado: {nome:<28} {len(df):>3} linhas")
    return tabelas


if __name__ == "__main__":
    gerar()
