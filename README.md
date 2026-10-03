# Agente de Triagem de Ordens de Serviço de Manutenção — Construtora Apollo S.A.

Projeto da disciplina **Engenharia de Agentes e IA Agêntica** (Pós-graduação PUC Minas).

O notebook implementa um agente único baseado em LLM que faz a triagem de ordens de
serviço de manutenção de equipamentos pesados: consulta a documentação técnica (Vector RAG)
e os sistemas operacionais (histórico, preventiva, estoque e frota) por Tool Calling
estruturado e registra um parecer na fila de manutenção.

> **Dados fictícios.** A Construtora Apollo S.A., seus documentos, códigos de alarme TL e
> códigos internos de peças APL foram criados para esta disciplina. Os modelos de
> equipamento são reais; os documentos técnicos são de autoria própria e não reproduzem
> trechos dos manuais dos fabricantes. As referências de peças da carregadeira 924H seguem
> o catálogo público do fabricante.

## Como executar

1. Abra o notebook no Google Colab.
2. Cadastre a chave do Gemini nos *Secrets* do Colab com o nome `GEMINI_API_KEY`.
3. Execute *Ambiente de execução → Executar tudo*.

Nenhum outro requisito externo é necessário: documentos e tabelas são baixados deste
repositório pelo próprio notebook.

## Estrutura

```
documentos/          base de conhecimento técnica (PDF) — indexada no Vector RAG
  FTM-CAT320.pdf     Ficha técnica de manutenção — Escavadeira CAT 320
  FTM-CATD9T.pdf     Ficha técnica de manutenção — Trator de esteiras CAT D9T
  FTM-CAT924H.pdf    Ficha técnica de manutenção — Carregadeira CAT 924H
  FTM-MBCAM.pdf      Ficha técnica de manutenção — Caminhões basculantes Mercedes-Benz
  CAT-ALM-001.pdf    Catálogo de alarmes de telemetria (códigos TL)
  PRO-SEG-001.pdf    Procedimento de segurança — bloqueio e impedimento de operação
  POL-MAN-001.pdf    Política de manutenção da frota
dados/               estado operacional (CSV) — acessado pelas ferramentas
  obras.csv
  equipamentos.csv
  ordens_servico.csv          entrada do agente
  historico_manutencao.csv    manutenções corretivas
  plano_preventiva.csv
  registro_preventivas.csv
  estoque_pecas.csv
scripts/             geradores dos documentos e das tabelas (reprodutibilidade)
notebook/            notebook da entrega
```

Data de referência dos dados: **2026-09-28**.
