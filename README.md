# Agente de Triagem de Ordens de Serviço de Manutenção — Construtora Apollo S.A.

Projeto da disciplina **Engenharia de Agentes e IA Agêntica** (Pós-graduação PUC Minas).

Neste projeto, desenvolvi um agente de IA para fazer a triagem de ordens de serviço de
manutenção de equipamentos pesados.

O agente consulta a documentação técnica usando RAG e também acessa informações operacionais,
como histórico de manutenção, planos de manutenção preventiva, estoque e equipamentos
disponíveis. Com essas informações, analisa a ordem de serviço e gera um parecer. Antes de
registrar o resultado, o sistema verifica se a recomendação atende às regras de segurança.

> **Dados fictícios.** A Construtora Apollo S.A., seus documentos, códigos de alarme TL e
> códigos internos de peças APL foram criados para esta disciplina. Os modelos de
> equipamento são reais; os documentos técnicos são de autoria própria e não reproduzem
> trechos dos manuais dos fabricantes. As referências de peças da carregadeira 924H seguem
> o catálogo do fabricante.

## Entregas

| Entrega | Notebook | Conteúdo |
|---|---|---|
| **1** — Caracterização do caso e agente único | [![Abrir no Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/diogo-hsf/apollo-agente-manutencao/blob/main/notebook/Apollo_Agente_Triagem_Manutencao.ipynb) | Agente único com laço ReAct, Vector RAG, Tool Calling estruturado, validação, guardrail de segurança e testes de comportamento |
| **2** — Orquestração e sistema multiagente | [![Abrir no Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/diogo-hsf/apollo-agente-manutencao/blob/main/notebook/Apollo_Multiagente_Triagem_Manutencao.ipynb) | Parte 1: o agente da Entrega 1 orquestrado por LangGraph, com ferramentas via MCP. Parte 2: Supervisor e três especialistas (Knowledge, Operations e Strategy) comunicando-se por A2A |

O estado exato da Entrega 1, como foi entregue, está preservado na tag
[`entrega-1`](https://github.com/diogo-hsf/apollo-agente-manutencao/tree/entrega-1).

## Como executar

1. Abra o notebook da entrega no Google Colab pelo botão da tabela acima.
2. Cadastre a chave do Gemini nos *Secrets* do Colab com o nome `GEMINI_API_KEY` e conceda
   acesso ao notebook quando solicitado.
3. Execute *Ambiente de execução → Executar tudo*.

Nenhum outro requisito externo é necessário: documentos e tabelas são baixados deste
repositório pelo próprio notebook.

**Cota da API.** No nível gratuito, cada modelo permite cerca de 20 chamadas de geração por
dia. Uma execução completa usa cerca de 18 chamadas na Entrega 1 e cerca de 9 na Entrega 2. Se
o modelo estiver sobrecarregado (erro 503) ou esgotar a cota, o notebook passa para um modelo
de reserva (`gemini-3.5-flash` e, depois, `gemini-3.1-flash-lite`). Se nenhum responder, o
notebook não é interrompido: as triagens afetadas são registradas como `incompleta` ou
"não executada".

## Estrutura

```
notebook/
  Apollo_Agente_Triagem_Manutencao.ipynb       Entrega 1
  Apollo_Multiagente_Triagem_Manutencao.ipynb  Entrega 2
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
```

Os scripts dos servidores MCP e A2A da Entrega 2 são gerados pelo próprio notebook durante a
execução. Data de referência dos dados: **2026-09-28**.

## Conteúdo dos notebooks

**Entrega 1:** 1. Caracterização do caso · 2. Desenho da solução · 3. Configuração e camada
de acesso ao modelo (retry e cota) · 4. Dados operacionais · 5. Base de conhecimento (Vector
RAG) · 6. Ferramentas · 7. O agente de triagem · 8. Testes de comportamento · 9. Conclusão

**Entrega 2:** 1. Por que evoluir · 2. Desenho da Parte 1 · 3. Desenho da Parte 2 ·
4. Configuração do ambiente · 5. Dados operacionais · 6. Base de conhecimento · 7. Servidor e
cliente MCP · 8. Parte 1 — O agente em LangGraph · 9. Parte 2 — Os agentes especialistas ·
10. Parte 2 — O Supervisor · 11. Verificações e comparação · 12. Conclusão
