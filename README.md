# Agente de Triagem de Ordens de Serviço de Manutenção — Construtora Apollo S.A.

[![Abrir no Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/diogo-hsf/apollo-agente-manutencao/blob/main/notebook/Apollo_Agente_Triagem_Manutencao.ipynb)

Projeto da disciplina **Engenharia de Agentes e IA Agêntica** (Pós-graduação PUC Minas) —
Entrega 1: caracterização do caso e agente único.

Neste projeto, desenvolvi um agente de IA para fazer a triagem de ordens de serviço de
manutenção de equipamentos pesados.

O agente consulta a documentação técnica usando RAG e também acessa informações operacionais,
como histórico de manutenção, planos de manutenção preventiva, estoque e equipamentos
disponíveis. Com essas informações, analisa a ordem de serviço e gera um parecer. Antes de
registrar o resultado, o sistema verifica se a recomendação atende às regras de segurança.

A documentação técnica fica indexada em um Vector RAG, os sistemas operacionais (cadastro,
histórico, preventiva, estoque e frota) são consultados por Tool Calling estruturado, e o
parecer é validado antes de ser registrado na fila de manutenção.

> **Dados fictícios.** A Construtora Apollo S.A., seus documentos, códigos de alarme TL e
> códigos internos de peças APL foram criados para esta disciplina. Os modelos de
> equipamento são reais; os documentos técnicos são de autoria própria e não reproduzem
> trechos dos manuais dos fabricantes. As referências de peças da carregadeira 924H seguem
> o catálogo do fabricante.

## Como executar

1. Abra o notebook no Google Colab pelo botão acima.
2. Cadastre a chave do Gemini nos *Secrets* do Colab com o nome `GEMINI_API_KEY` e conceda
   acesso ao notebook quando solicitado.
3. Execute *Ambiente de execução → Executar tudo*.

Nenhum outro requisito externo é necessário: documentos e tabelas são baixados deste
repositório pelo próprio notebook.

**Cota da API.** No nível gratuito, o `gemini-3.6-flash` permite cerca de 20 chamadas de
geração por dia; uma execução completa usa entre 12 e 16. Se a cota se esgotar durante a
execução, o notebook não é interrompido: as triagens afetadas são registradas como
`incompleta` ou "não executada", e os testes indicam isso explicitamente.

## Estrutura

```
notebook/
  Apollo_Agente_Triagem_Manutencao.ipynb   entrega
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

Data de referência dos dados: **2026-09-28**.

## Conteúdo do notebook

1. Caracterização do caso · 2. Desenho da solução · 3. Configuração e camada de acesso ao
modelo (retry, cota, orçamento) · 4. Dados operacionais · 5. Base de conhecimento (Vector RAG) ·
6. Ferramentas · 7. O agente de triagem · 8. Testes de comportamento · 9. Conclusão
