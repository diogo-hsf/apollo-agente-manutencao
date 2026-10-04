"""Conteúdo dos documentos técnicos da Construtora Apollo S.A. (fictícia).

Os documentos são de autoria da própria Apollo, redigidos para esta
disciplina. Os intervalos de manutenção e as referências de peças da
carregadeira 924H foram consultados nos manuais dos fabricantes como
referência factual; nenhum trecho dos manuais foi reproduzido.

Convenções que o chunker do notebook depende:
- Seção principal: linha "N TÍTULO EM MAIÚSCULAS".
- Subseção: linha "N.N Título".
- Passos de procedimento usam letras "a)", "b)"... (nunca números),
  para não serem confundidos com títulos de seção.

Blocos aceitos em cada seção:
    ("p", texto)                     parágrafo
    ("sub", numero, titulo)          subseção, ex.: ("sub", "5.2", "Sintomas")
    ("lista", [itens])               itens já prefixados com "a)", "b)"...
    ("tabela", cabecalho, linhas)    tabela simples
"""

EMPRESA = "Construtora Apollo S.A."
DATA_REVISAO = "setembro de 2026"

AVISO_FICTICIO = (
    "Documento fictício elaborado para fins acadêmicos (PUC Minas · Engenharia "
    "de Agentes e IA Agêntica). A Construtora Apollo S.A., os códigos de alarme "
    "TL e os códigos internos de peças APL são fictícios."
)

REFERENCIA_FABRICANTE = (
    "Esta ficha não substitui o manual do fabricante, que prevalece em caso de "
    "divergência e deve ser consultado para torques, especificações de fluidos, "
    "capacidades e procedimentos detalhados de desmontagem."
)

DOCUMENTOS = [
    # ------------------------------------------------------------------
    {
        "codigo": "FTM-CAT320",
        "titulo": "Ficha Técnica de Manutenção — Escavadeira Hidráulica Caterpillar 320",
        "revisao": "Rev. 02",
        "aplicacao": "CAT 320",
        "secoes": [
            ("1", "OBJETIVO E REFERÊNCIAS", [
                ("p", "Esta ficha consolida as orientações de inspeção, manutenção "
                      "preventiva e diagnóstico inicial das escavadeiras hidráulicas "
                      "Caterpillar 320 da frota da Construtora Apollo. É o documento de "
                      "primeira consulta do planejador de manutenção na triagem de ordens "
                      "de serviço."),
                ("p", REFERENCIA_FABRICANTE + " Referência: Manual de Operação e "
                      "Manutenção da escavadeira 320, publicação M0083583."),
                ("p", "Os códigos de alarme citados (TL-xxx) são gerados pelo sistema "
                      "Apollo Telemetria e estão descritos no CAT-ALM-001."),
            ]),
            ("2", "APLICAÇÃO NA FROTA", [
                ("p", "As escavadeiras 320 são usadas em escavação de cortes, carga de "
                      "caminhões basculantes e abertura de valas de drenagem. Quando a "
                      "escavadeira é a única máquina de carga de uma frente de serviço, a "
                      "parada dela interrompe também os caminhões que ela carrega."),
            ]),
            ("3", "INSPEÇÕES DIÁRIAS DO OPERADOR", [
                ("p", "A cada 10 horas de serviço, ou no início de cada turno, o operador "
                      "verifica os itens abaixo e registra no checklist. Anomalia "
                      "encontrada gera ordem de serviço."),
                ("lista", [
                    "a) Nível do líquido arrefecedor.",
                    "b) Nível do óleo do motor.",
                    "c) Nível do óleo hidráulico, com a máquina na posição de verificação "
                    "indicada no adesivo do tanque.",
                    "d) Drenagem do separador de água do combustível e do fundo do tanque.",
                    "e) Funcionamento de indicadores, medidores e alarme de deslocamento.",
                    "f) Estado do cinto de segurança.",
                    "g) Tensão das esteiras.",
                ]),
            ]),
            ("4", "PLANO DE MANUTENÇÃO PREVENTIVA", [
                ("p", "Intervalos adotados pela Apollo em horas de serviço (horímetro). "
                      "A tolerância e o controle de revisões vencidas seguem a POL-MAN-001."),
                ("tabela", ["Revisão", "Intervalo", "Serviços principais"], [
                    ["R250", "250 h", "Coleta de amostra de óleo do motor e do comando "
                                      "final para análise."],
                    ["R500", "500 h", "Troca de óleo e filtro do motor; troca do filtro "
                                      "primário (separador de água) e do filtro secundário "
                                      "de combustível; amostra do óleo hidráulico; "
                                      "lubrificação do mancal de giro, da lança e do braço."],
                    ["R1000", "1.000 h", "Troca do óleo do comando de giro; inspeção da "
                                         "correia; verificação da folga de válvulas; "
                                         "limpeza e reaperto dos bornes da bateria."],
                    ["R2000", "2.000 h", "Troca do óleo do comando final; lubrificação da "
                                         "engrenagem de giro; troca do filtro da tampa "
                                         "de combustível."],
                    ["R3000", "3.000 h", "Troca do filtro de retorno do óleo hidráulico."],
                    ["R6000", "6.000 h", "Troca do óleo hidráulico; adição de prolongador "
                                         "ao líquido arrefecedor."],
                ]),
            ]),
            ("5", "SISTEMA HIDRÁULICO", [
                ("sub", "5.1", "Sintomas típicos"),
                ("p", "Movimentos lentos de lança, braço ou caçamba; perda de força ao "
                      "escavar; aquecimento do óleo hidráulico; ruído na bomba; "
                      "vazamentos externos em mangueiras, conexões e cilindros."),
                ("sub", "5.2", "Lentidão ou perda de força após aquecimento (alarme TL-214)"),
                ("p", "Quando a perda de desempenho surge depois de algum tempo de "
                      "operação, a máquina funciona normalmente fria e o alarme TL-214 "
                      "aparece, a causa mais provável é a deficiência na troca térmica do "
                      "óleo hidráulico. O óleo quente perde viscosidade e aumenta o "
                      "vazamento interno de bombas e cilindros. Sequência de verificação:"),
                ("lista", [
                    "a) Conferir o nível do óleo hidráulico na posição de verificação.",
                    "b) Inspecionar a colmeia do arrefecedor de óleo e do radiador quanto a "
                    "obstrução por poeira ou lama e limpá-la.",
                    "c) Verificar o indicador de restrição e o estado do filtro de retorno.",
                    "d) Verificar o funcionamento e a rotação do ventilador de arrefecimento.",
                    "e) Persistindo o sintoma, medir as pressões de trabalho e de alívio e "
                    "verificar vazamento interno nos cilindros e na bomba principal. Este "
                    "item é serviço de mecânico especializado em hidráulica.",
                ]),
                ("p", "Se o alarme TL-214 voltar depois de limpeza do arrefecedor e troca "
                      "do filtro de retorno, repetir essas ações não resolve a causa. A "
                      "ocorrência deve ser tratada como falha recorrente conforme a "
                      "POL-MAN-001, avançando diretamente para o item e)."),
                ("p", "Peças associadas: APL-10021 Filtro de retorno do óleo hidráulico; "
                      "APL-10022 Kit de vedação do cilindro do braço; APL-10026 Óleo "
                      "hidráulico (litro)."),
                ("sub", "5.3", "Vazamentos externos"),
                ("p", "Para vazamento em mangueira, conexão ou haste de cilindro: limpar a "
                      "região, identificar o ponto exato, verificar o nível do óleo e "
                      "avaliar se a máquina pode operar até o reparo. Vazamento com jato "
                      "sob pressão exige parada imediata; nunca localizar o furo com a mão, "
                      "pelo risco de injeção de fluido na pele (PRO-SEG-001)."),
                ("p", "Peças associadas: APL-10022 Kit de vedação do cilindro do braço; "
                      "APL-10027 Mangueira de alta pressão do cilindro da caçamba."),
            ]),
            ("6", "MOTOR E COMBUSTÍVEL", [
                ("sub", "6.1", "Perda de potência"),
                ("p", "Verificar o indicador de restrição do filtro de ar (alarme TL-108), "
                      "o estado dos filtros de combustível e do separador de água e a "
                      "qualidade do combustível. Revisão R500 em atraso é causa frequente "
                      "de perda de potência na frota."),
                ("sub", "6.2", "Temperatura elevada do líquido arrefecedor (alarme TL-145)"),
                ("p", "Verificar nível do líquido arrefecedor, obstrução da colmeia do "
                      "radiador, tensão da correia e funcionamento do ventilador."),
                ("sub", "6.3", "Pressão baixa do óleo do motor (alarme TL-120)"),
                ("p", "Alarme de nível 3: desligar o motor imediatamente e não religar até "
                      "a inspeção. Verificar nível e vazamentos de óleo."),
                ("p", "Peças associadas: APL-10023 Filtro de óleo do motor; APL-10024 "
                      "Filtro primário de combustível (separador de água); APL-10025 Filtro "
                      "secundário de combustível; APL-10028 Elemento primário do filtro de ar."),
            ]),
            ("7", "MATERIAL RODANTE E GIRO", [
                ("p", "Esteira frouxa ou excessivamente tensionada acelera o desgaste de "
                      "roletes, rodas-guia e coroas. Ruído no giro: verificar o nível de "
                      "óleo do comando de giro e a lubrificação do mancal."),
            ]),
            ("8", "CRITÉRIOS DE PARADA", [
                ("p", "Parar a máquina e aplicar o PRO-SEG-001 nos seguintes casos: alarme "
                      "de nível 3; vazamento hidráulico com jato sob pressão; trinca na "
                      "lança, no braço ou no chassi; falha no freio de giro ou de "
                      "deslocamento; dano na cabine ou na estrutura de proteção."),
            ]),
        ],
    },
    # ------------------------------------------------------------------
    {
        "codigo": "FTM-CATD9T",
        "titulo": "Ficha Técnica de Manutenção — Trator de Esteiras Caterpillar D9T",
        "revisao": "Rev. 01",
        "aplicacao": "CAT D9T",
        "secoes": [
            ("1", "OBJETIVO E REFERÊNCIAS", [
                ("p", "Esta ficha consolida as orientações de inspeção, manutenção "
                      "preventiva e diagnóstico inicial dos tratores de esteiras "
                      "Caterpillar D9T da frota da Construtora Apollo."),
                ("p", REFERENCIA_FABRICANTE + " Referência: Manual de Operação e "
                      "Manutenção do trator D9T."),
            ]),
            ("2", "APLICAÇÃO NA FROTA", [
                ("p", "Os tratores D9T executam corte e empurre de material, escarificação "
                      "de rocha branda e conformação de praças e rampas. Em frentes de "
                      "terraplenagem pesada, normalmente não há outro equipamento capaz "
                      "de substituí-los no mesmo turno."),
            ]),
            ("3", "INSPEÇÕES DIÁRIAS DO OPERADOR", [
                ("lista", [
                    "a) Níveis do óleo do motor, do líquido arrefecedor, do óleo do trem de "
                    "força e do óleo hidráulico.",
                    "b) Drenagem do separador de água do combustível.",
                    "c) Indicador de restrição do filtro de ar.",
                    "d) Inspeção visual do material rodante, da lâmina e do escarificador.",
                    "e) Cinto de segurança e alarme de ré.",
                ]),
            ]),
            ("4", "NÍVEIS DE ALERTA DO PAINEL", [
                ("p", "O sistema de monitoramento da máquina classifica os eventos em três "
                      "níveis. No nível 1 basta a atenção do operador. No nível 2 é "
                      "preciso mudar a forma de operar ou providenciar manutenção. No "
                      "nível 3 o motor deve ser desligado imediatamente, com segurança. O "
                      "sistema Apollo Telemetria adota a mesma escala (CAT-ALM-001)."),
            ]),
            ("5", "PLANO DE MANUTENÇÃO PREVENTIVA", [
                ("tabela", ["Revisão", "Intervalo", "Serviços principais"], [
                    ["R250", "250 h", "Amostras de óleo do motor, do trem de força e do "
                                      "hidráulico; limpeza do pré-filtro de ar; lubrificação."],
                    ["R500", "500 h", "Troca de óleo e filtro do motor; troca dos filtros "
                                      "primário e secundário de combustível; troca do "
                                      "elemento primário do filtro de ar; drenagem do tanque."],
                    ["R1000", "1.000 h", "Troca dos filtros do trem de força e do sistema "
                                         "hidráulico; inspeção de correias."],
                    ["R2000", "2.000 h", "Troca do óleo do trem de força e dos comandos "
                                         "finais; troca do elemento secundário do filtro de ar."],
                ]),
            ]),
            ("6", "MOTOR — PERDA DE POTÊNCIA", [
                ("sub", "6.1", "Sintomas"),
                ("p", "Falta de força ao empurrar material, queda acentuada de rotação com "
                      "a lâmina carregada, fumaça escura no escapamento e aumento do "
                      "consumo de combustível."),
                ("sub", "6.2", "Sequência de verificação"),
                ("lista", [
                    "a) Consultar a situação da manutenção preventiva. Revisão R500 vencida, "
                    "com filtros de combustível e de ar saturados, é a causa mais frequente "
                    "deste sintoma na frota.",
                    "b) Verificar o indicador de restrição do filtro de ar e o histórico do "
                    "alarme TL-108. Limpeza do elemento com ar comprimido é medida "
                    "provisória e não substitui a troca.",
                    "c) Drenar o separador de água e verificar contaminação do combustível.",
                    "d) Inspecionar mangueiras de admissão e do pós-arrefecedor quanto a "
                    "vazamentos de ar.",
                    "e) Persistindo o sintoma com filtros novos, solicitar diagnóstico "
                    "eletrônico do motor por técnico especializado.",
                ]),
                ("p", "Fumaça escura no escapamento associada a filtro de ar restrito "
                      "indica combustão com falta de ar, e não incêndio. Fumaça dentro da "
                      "cabine ou cheiro de queimado são situações de bloqueio (PRO-SEG-001)."),
                ("p", "Peças associadas: APL-20011 Elemento primário do filtro de ar; "
                      "APL-20012 Elemento secundário do filtro de ar; APL-20013 Filtro "
                      "primário de combustível (separador de água); APL-20014 Filtro "
                      "secundário de combustível; APL-20015 Filtro de óleo do motor."),
            ]),
            ("7", "TREM DE FORÇA E FREIOS", [
                ("p", "Patinação, demora nas trocas de marcha ou temperatura alta do óleo "
                      "da transmissão (alarme TL-342) exigem verificação do nível do óleo e "
                      "limpeza do arrefecedor. Qualquer falha nos freios ou no freio de "
                      "estacionamento é situação de bloqueio (PRO-SEG-001)."),
            ]),
            ("8", "CRITÉRIOS DE PARADA", [
                ("p", "Alarme de nível 3; falha de freio ou de direção; vazamento de "
                      "combustível; fumaça na cabine ou cheiro de queimado; trinca na "
                      "estrutura da lâmina ou do escarificador."),
            ]),
        ],
    },
    # ------------------------------------------------------------------
    {
        "codigo": "FTM-CAT924H",
        "titulo": "Ficha Técnica de Manutenção — Carregadeira de Rodas Caterpillar 924H",
        "revisao": "Rev. 03",
        "aplicacao": "CAT 924H",
        "secoes": [
            ("1", "OBJETIVO E REFERÊNCIAS", [
                ("p", "Esta ficha consolida as orientações de inspeção, manutenção "
                      "preventiva e diagnóstico inicial das carregadeiras de rodas "
                      "Caterpillar 924H da frota da Construtora Apollo."),
                ("p", REFERENCIA_FABRICANTE + " As referências de peças entre parênteses "
                      "seguem o catálogo de peças do fabricante (publicação SEBP4617)."),
            ]),
            ("2", "APLICAÇÃO NA FROTA", [
                ("p", "Carregamento de agregados e solo em caminhões, manuseio de "
                      "materiais em pátios e alimentação de usinas. Opera próxima a "
                      "pessoas e outros veículos, o que torna os freios o item de "
                      "segurança mais crítico desta máquina."),
            ]),
            ("3", "INSPEÇÕES DIÁRIAS DO OPERADOR", [
                ("lista", [
                    "a) Níveis do óleo do motor, do líquido arrefecedor, do óleo hidráulico "
                    "e da transmissão.",
                    "b) Teste do freio de serviço e do freio de estacionamento em local "
                    "plano, no início do turno.",
                    "c) Pneus: pressão, cortes e desgaste.",
                    "d) Alarme de ré, luzes e cinto de segurança.",
                ]),
            ]),
            ("4", "PLANO DE MANUTENÇÃO PREVENTIVA", [
                ("tabela", ["Revisão", "Intervalo", "Serviços principais"], [
                    ["R250", "250 h", "Amostras de óleo; lubrificação das articulações "
                                      "da caçamba e da direção."],
                    ["R500", "500 h", "Troca de óleo e filtro do motor (APL-30011); troca "
                                      "dos filtros de combustível (APL-30012, APL-30013)."],
                    ["R1000", "1.000 h", "Troca dos filtros da transmissão e do hidráulico; "
                                         "inspeção do sistema de freios e dos acumuladores."],
                    ["R2000", "2.000 h", "Troca do óleo hidráulico e dos eixos; troca dos "
                                         "elementos do filtro de ar (APL-30014, APL-30015)."],
                ]),
            ]),
            ("5", "SISTEMA DE FREIOS", [
                ("sub", "5.1", "Descrição"),
                ("p", "Os freios de serviço são multidisco em banho de óleo, montados nos "
                      "eixos e acionados hidraulicamente pela válvula de controle do freio "
                      "de serviço. Acumuladores mantêm a reserva de pressão e uma bomba de "
                      "engrenagem alimenta o circuito de freio e o ventilador. Um sensor "
                      "monitora a pressão do óleo do freio e aciona o alarme TL-331."),
                ("sub", "5.2", "Sintomas"),
                ("p", "Pedal baixo ou esponjoso, aumento da distância de parada "
                      "(principalmente com a caçamba carregada), máquina puxando para um "
                      "lado e alarme TL-331 de pressão baixa do óleo do freio."),
                ("sub", "5.3", "Conduta e diagnóstico"),
                ("p", "Qualquer sintoma no freio de serviço implica bloqueio imediato da "
                      "máquina (PRO-SEG-001, seção 3). Com a máquina bloqueada, o mecânico "
                      "segue a sequência:"),
                ("lista", [
                    "a) Verificar o nível do óleo hidráulico que alimenta o circuito de freio.",
                    "b) Confirmar o alarme TL-331 e comparar a leitura do sensor de pressão "
                    "com um manômetro de teste, para descartar falha do próprio sensor.",
                    "c) Testar a carga de pré-pressão dos acumuladores.",
                    "d) Inspecionar a válvula de controle do freio de serviço quanto a "
                    "vazamento interno.",
                    "e) Medir a vazão da bomba de engrenagem do circuito de freio.",
                ]),
                ("p", "A liberação só ocorre após teste de frenagem aprovado e registrado "
                      "pelo encarregado de manutenção."),
                ("p", "Peças associadas: APL-30021 Válvula de controle do freio de serviço "
                      "(ref. 144-8521); APL-30022 Sensor de pressão do óleo do freio "
                      "(ref. 290-5825); APL-30023 Bomba de engrenagem do freio e do "
                      "ventilador (ref. 299-3941)."),
            ]),
            ("6", "MOTOR E COMBUSTÍVEL", [
                ("p", "Perda de potência: verificar filtro de ar (alarme TL-108), filtros "
                      "de combustível e separador de água. Pressão baixa do óleo do motor "
                      "(alarme TL-120) exige desligamento imediato."),
                ("p", "Peças associadas: APL-30011 Filtro de óleo do motor (ref. 269-8325); "
                      "APL-30012 Filtro primário de combustível e separador de água "
                      "(ref. 326-1644); APL-30013 Filtro secundário de combustível "
                      "(ref. 308-7480); APL-30014 Elemento primário do filtro de ar "
                      "(ref. 256-7902); APL-30015 Elemento secundário do filtro de ar "
                      "(ref. 256-7903)."),
            ]),
            ("7", "SISTEMA HIDRÁULICO E IMPLEMENTO", [
                ("p", "Lentidão de levante ou basculamento: verificar nível do óleo, "
                      "restrição do filtro de retorno (alarme TL-226) e vazamentos nos "
                      "cilindros. Folga excessiva nos pinos da caçamba deve ser registrada "
                      "para a próxima parada programada."),
            ]),
            ("8", "CRITÉRIOS DE PARADA", [
                ("p", "Qualquer anormalidade no freio de serviço, no freio de "
                      "estacionamento ou na direção; alarme de nível 3; vazamento de "
                      "combustível; pneu com corte profundo ou bolha; falha do alarme de ré."),
            ]),
        ],
    },
    # ------------------------------------------------------------------
    {
        "codigo": "FTM-MBCAM",
        "titulo": "Ficha Técnica de Manutenção — Caminhões Basculantes Mercedes-Benz "
                  "(Axor 3344 K e 2726 K)",
        "revisao": "Rev. 02",
        "aplicacao": "MB Axor 3344 K; MB 2726 K",
        "secoes": [
            ("1", "OBJETIVO E REFERÊNCIAS", [
                ("p", "Esta ficha consolida as orientações de inspeção, manutenção "
                      "preventiva e diagnóstico inicial dos caminhões basculantes "
                      "Mercedes-Benz da frota da Construtora Apollo."),
                ("p", REFERENCIA_FABRICANTE + " Referências: manuais de manutenção do "
                      "Axor e da linha 2423/2726."),
            ]),
            ("2", "CATEGORIA DE MANUTENÇÃO", [
                ("p", "Os fabricantes classificam como serviço severo os veículos que "
                      "operam em canteiro de obra, em vias não pavimentadas e com carga "
                      "máxima. Todos os basculantes da Apollo seguem essa categoria, com "
                      "controle por horímetro."),
            ]),
            ("3", "INSPEÇÕES DIÁRIAS DO MOTORISTA", [
                ("lista", [
                    "a) Nível do óleo do motor e do líquido arrefecedor.",
                    "b) Pressão do ar do sistema de freios e drenagem dos reservatórios.",
                    "c) Pneus: calibragem, cortes e aperto das porcas de roda.",
                    "d) Luzes, buzina, alarme de ré e funcionamento da caçamba.",
                    "e) Vazamentos visíveis sob o veículo.",
                ]),
            ]),
            ("4", "PLANO DE MANUTENÇÃO PREVENTIVA", [
                ("tabela", ["Revisão", "Intervalo", "Serviços principais"], [
                    ["R200", "200 h", "Lubrificação do chassi, da suspensão e da articulação "
                                      "da caçamba."],
                    ["R300", "300 h", "Troca de óleo e filtro do motor (APL-40011); troca "
                                      "do filtro de combustível (APL-40012)."],
                    ["R600", "600 h", "Troca do filtro do secador de ar; inspeção de lonas "
                                      "e tambores; regulagem dos freios."],
                    ["R1200", "1.200 h", "Troca do óleo da caixa de câmbio e dos "
                                         "diferenciais; troca do elemento do filtro de ar."],
                ]),
            ]),
            ("5", "RUÍDOS NA DIANTEIRA, FREIOS E SUSPENSÃO", [
                ("sub", "5.1", "Como direcionar o diagnóstico"),
                ("p", "Ruído na dianteira pode ter origem no freio, na suspensão, na "
                      "direção ou nos rolamentos de roda, e cada origem leva a uma "
                      "investigação diferente. Para direcionar a triagem, a ordem de "
                      "serviço precisa informar:"),
                ("lista", [
                    "a) Quando o ruído ocorre: ao frear, em buracos e irregularidades, em "
                    "curvas ou o tempo todo com o veículo em movimento.",
                    "b) Tipo de ruído: rangido metálico, batida seca, chiado ou zumbido.",
                    "c) Se há vibração no volante, desvio de trajetória ou alteração no "
                    "pedal de freio.",
                ]),
                ("p", "Sem essas informações não é possível indicar a provável origem, e a "
                      "ordem de serviço deve ser devolvida com essas perguntas (POL-MAN-001, "
                      "seção 3)."),
                ("sub", "5.2", "Origens mais comuns"),
                ("tabela", ["Quando ocorre", "Origem provável", "Peças associadas"], [
                    ["Ao frear", "Lonas de freio gastas ou tambor danificado",
                     "APL-40013 Kit de lonas de freio dianteiro"],
                    ["Em buracos", "Amortecedor, molas ou buchas da suspensão",
                     "APL-40014 Amortecedor dianteiro"],
                    ["Em curvas", "Terminais de direção ou rolamento de roda",
                     "APL-40015 Terminal de direção"],
                    ["Sempre em movimento", "Rolamento de roda", "Conforme inspeção"],
                ]),
                ("sub", "5.3", "Sinais de risco"),
                ("p", "Ruído acompanhado de perda de eficiência de frenagem, desvio de "
                      "trajetória, folga ou dureza na direção, ou alarme TL-350 (pressão "
                      "baixa do ar do freio) é situação de bloqueio (PRO-SEG-001)."),
            ]),
            ("6", "MOTOR", [
                ("p", "Perda de potência ou fumaça escura: verificar filtro de ar, filtro "
                      "de combustível e revisão R300. Pressão baixa do óleo do motor "
                      "(alarme TL-120) exige desligamento imediato."),
            ]),
            ("7", "SISTEMA DE BASCULAMENTO", [
                ("p", "Caçamba que não levanta ou desce sozinha: verificar tomada de força, "
                      "nível do óleo do sistema de basculamento e vedações do cilindro. "
                      "Nunca trabalhar sob a caçamba levantada sem o calço de segurança."),
            ]),
            ("8", "CRITÉRIOS DE PARADA", [
                ("p", "Falha de freio ou de direção; alarme TL-350 ou qualquer alarme de "
                      "nível 3; vazamento de combustível; pneu com corte profundo; caçamba "
                      "que não trava na posição abaixada."),
            ]),
        ],
    },
    # ------------------------------------------------------------------
    {
        "codigo": "CAT-ALM-001",
        "titulo": "Catálogo de Alarmes de Telemetria e Ocorrências",
        "revisao": "Rev. 04",
        "aplicacao": "geral",
        "secoes": [
            ("1", "OBJETIVO", [
                ("p", "O sistema Apollo Telemetria recebe os eventos dos equipamentos e os "
                      "converte em códigos padronizados TL-xxx, independentes do "
                      "fabricante. Este catálogo descreve cada código, o nível de alerta e "
                      "a ação inicial esperada. O código original do fabricante, quando "
                      "necessário, é consultado no manual do equipamento."),
            ]),
            ("2", "NÍVEIS DE ALERTA", [
                ("tabela", ["Nível", "Significado", "Ação esperada"], [
                    ["1", "Atenção", "Sem ação imediata; programar verificação."],
                    ["2", "Alerta", "Alterar a forma de operar e acionar a manutenção "
                                    "no mesmo turno."],
                    ["3", "Crítico", "Parar em local seguro e desligar; o retorno depende "
                                     "de liberação formal (PRO-SEG-001)."],
                ]),
            ]),
            ("3", "ALARMES DO MOTOR", [
                ("tabela", ["Código", "Descrição", "Nível", "Ação inicial"], [
                    ["TL-108", "Restrição do filtro de ar do motor", "1",
                     "Verificar e trocar o elemento; checar revisão preventiva."],
                    ["TL-120", "Pressão baixa do óleo do motor", "3",
                     "Desligar imediatamente; verificar nível e vazamentos."],
                    ["TL-145", "Temperatura elevada do líquido arrefecedor", "2",
                     "Verificar nível, colmeia do radiador, correia e ventilador."],
                    ["TL-152", "Água no combustível", "1",
                     "Drenar o separador de água; verificar o tanque."],
                ]),
            ]),
            ("4", "ALARMES DO SISTEMA HIDRÁULICO", [
                ("tabela", ["Código", "Descrição", "Nível", "Ação inicial"], [
                    ["TL-214", "Temperatura elevada do óleo hidráulico", "2",
                     "Verificar nível, colmeia do arrefecedor de óleo, filtro de retorno "
                     "e ventilador (FTM-CAT320, seção 5.2)."],
                    ["TL-226", "Restrição do filtro de retorno hidráulico", "1",
                     "Programar a troca do filtro de retorno."],
                    ["TL-233", "Nível baixo do óleo hidráulico", "2",
                     "Localizar vazamento e completar o nível antes de continuar."],
                ]),
            ]),
            ("5", "ALARMES DE FREIO E TREM DE FORÇA", [
                ("tabela", ["Código", "Descrição", "Nível", "Ação inicial"], [
                    ["TL-331", "Pressão baixa do óleo do freio de serviço", "3",
                     "Parar e bloquear; diagnóstico conforme FTM-CAT924H, seção 5.3."],
                    ["TL-335", "Freio de estacionamento acionado em deslocamento", "2",
                     "Verificar interruptor e circuito do freio de estacionamento."],
                    ["TL-342", "Temperatura elevada do óleo da transmissão", "2",
                     "Verificar nível e arrefecedor da transmissão."],
                    ["TL-350", "Pressão baixa do ar do sistema de freios", "3",
                     "Parar e bloquear; verificar compressor e vazamentos de ar."],
                ]),
            ]),
            ("6", "ALARMES ELÉTRICOS E DE TELEMETRIA", [
                ("tabela", ["Código", "Descrição", "Nível", "Ação inicial"], [
                    ["TL-402", "Tensão baixa do sistema elétrico", "1",
                     "Verificar bateria, bornes e alternador."],
                    ["TL-510", "Perda de comunicação do módulo de telemetria", "1",
                     "Não indica falha mecânica; verificar antena e alimentação do módulo."],
                ]),
            ]),
            ("7", "CÓDIGOS NÃO CATALOGADOS", [
                ("p", "Código ausente deste catálogo não deve ser interpretado por "
                      "analogia com códigos parecidos. O planejador registra o código "
                      "exatamente como informado, solicita foto do painel ao operador e "
                      "encaminha a ocorrência à Engenharia de Manutenção."),
            ]),
        ],
    },
    # ------------------------------------------------------------------
    {
        "codigo": "PRO-SEG-001",
        "titulo": "Procedimento de Segurança — Bloqueio e Impedimento de Operação "
                  "de Equipamentos",
        "revisao": "Rev. 05",
        "aplicacao": "geral",
        "secoes": [
            ("1", "OBJETIVO", [
                ("p", "Definir quando um equipamento deve ser impedido de operar, como "
                      "realizar o bloqueio de energias e quem pode liberá-lo após a "
                      "manutenção."),
            ]),
            ("2", "DEFINIÇÕES", [
                ("lista", [
                    "a) Impedimento de operação: proibição de uso do equipamento até "
                    "liberação formal.",
                    "b) Bloqueio de energias: isolamento das fontes de energia (elétrica, "
                    "hidráulica, pneumática e mecânica) com cadeado e etiqueta.",
                    "c) Liberação: autorização formal de retorno à operação, após reparo "
                    "e teste funcional.",
                ]),
            ]),
            ("3", "SITUAÇÕES DE BLOQUEIO OBRIGATÓRIO", [
                ("p", "O equipamento deve ser bloqueado até inspeção nas situações abaixo, "
                      "independentemente da urgência da obra:"),
                ("lista", [
                    "a) Qualquer falha ou anormalidade no freio de serviço, no freio de "
                    "estacionamento ou no freio de emergência.",
                    "b) Falha, folga ou dureza anormal na direção.",
                    "c) Alarme de nível 3 ativo (CAT-ALM-001).",
                    "d) Vazamento de combustível, fumaça dentro da cabine, cheiro de "
                    "queimado ou qualquer indício de incêndio.",
                    "e) Vazamento hidráulico com jato sob pressão.",
                    "f) Dano na cabine, na estrutura de proteção contra capotagem ou no "
                    "cinto de segurança.",
                    "g) Trinca estrutural em lança, braço, chassi, lâmina ou caçamba.",
                    "h) Alarme de ré inoperante em área com circulação de pessoas.",
                ]),
            ]),
            ("4", "OPERAÇÃO COM RESTRIÇÃO", [
                ("p", "Alarmes de nível 2 e anomalias sem risco à segurança permitem "
                      "operação com restrição, mediante autorização do encarregado da "
                      "frente de serviço: carga reduzida, pausas para resfriamento ou "
                      "limitação de tarefas, até a manutenção no mesmo turno."),
            ]),
            ("5", "PROCEDIMENTO DE BLOQUEIO", [
                ("lista", [
                    "a) Estacionar em local plano e seguro, com implementos apoiados no solo.",
                    "b) Acionar o freio de estacionamento e desligar o motor.",
                    "c) Aliviar as pressões residuais dos circuitos hidráulicos.",
                    "d) Desligar a chave geral e instalar o cadeado de bloqueio.",
                    "e) Fixar a etiqueta com data, número da ordem de serviço e responsável.",
                    "f) Comunicar o bloqueio ao encarregado da frente de serviço.",
                ]),
            ]),
            ("6", "LIBERAÇÃO", [
                ("p", "A liberação é feita exclusivamente pelo encarregado de manutenção, "
                      "após o reparo e o teste funcional. Intervenções no sistema de "
                      "freios exigem teste de frenagem registrado na ordem de serviço."),
            ]),
            ("7", "RESPONSABILIDADES", [
                ("p", "A decisão de bloquear ou liberar um equipamento é sempre de uma "
                      "pessoa habilitada. Sistemas de apoio à decisão, inclusive "
                      "assistentes automatizados de triagem, podem apenas recomendar e "
                      "devem adotar a recomendação mais conservadora em caso de dúvida."),
            ]),
        ],
    },
    # ------------------------------------------------------------------
    {
        "codigo": "POL-MAN-001",
        "titulo": "Política de Manutenção da Frota de Equipamentos",
        "revisao": "Rev. 03",
        "aplicacao": "geral",
        "secoes": [
            ("1", "OBJETIVO E ABRANGÊNCIA", [
                ("p", "Estabelecer as regras de triagem, priorização e execução da "
                      "manutenção dos equipamentos e caminhões de todas as obras da "
                      "Construtora Apollo."),
            ]),
            ("2", "FLUXO DA ORDEM DE SERVIÇO", [
                ("p", "O operador ou motorista abre a ordem de serviço. O planejador de "
                      "manutenção faz a triagem: identifica o equipamento, levanta o "
                      "histórico, a situação da preventiva e a disponibilidade de peças, "
                      "define a prioridade e indica o procedimento inicial. Em seguida, a "
                      "ordem é programada, executada e encerrada pelo encarregado."),
            ]),
            ("3", "DADOS MÍNIMOS E DEVOLUÇÃO DA ORDEM DE SERVIÇO", [
                ("p", "A ordem de serviço deve conter: identificação do equipamento pelo "
                      "prefixo da frota, obra, descrição do sintoma com as condições em "
                      "que ocorre e o código de alarme, se houver."),
                ("p", "Ordem sem identificação inequívoca do equipamento, ou com relato "
                      "que não permita direcionar a investigação, deve ser devolvida ao "
                      "solicitante com perguntas objetivas. Não é permitido deduzir o "
                      "equipamento por aproximação, por exemplo escolhendo uma máquina "
                      "parecida da mesma obra."),
            ]),
            ("4", "MATRIZ DE PRIORIDADE", [
                ("tabela", ["Prioridade", "Critério", "Início do atendimento"], [
                    ["P1 Emergencial", "Situação de bloqueio obrigatório (PRO-SEG-001), "
                     "ou equipamento de criticidade A parado sem substituto.", "Até 2 horas"],
                    ["P2 Alta", "Equipamento parado ou operando com restrição, de "
                     "criticidade A com substituto ou de criticidade B sem substituto.",
                     "No mesmo turno (até 8 horas)"],
                    ["P3 Normal", "Equipamento operando com anomalia sem risco à "
                     "segurança.", "Até 48 horas"],
                    ["P4 Programável", "Itens que podem aguardar a próxima parada "
                     "programada ou revisão preventiva.", "Até 7 dias"],
                ]),
                ("p", "Falha recorrente (seção 6) eleva a prioridade em um nível, "
                      "limitada a P2 quando não houver risco à segurança."),
            ]),
            ("5", "CRITICIDADE DOS EQUIPAMENTOS", [
                ("tabela", ["Classe", "Definição"], [
                    ["A", "Sem o equipamento, a frente de serviço para."],
                    ["B", "A parada reduz a produção, mas a frente continua."],
                    ["C", "Equipamento de apoio ou reserva."],
                ]),
            ]),
            ("6", "FALHA RECORRENTE", [
                ("p", "Três ou mais ocorrências corretivas no mesmo sistema do mesmo "
                      "equipamento em 90 dias, contando a ocorrência atual, caracterizam "
                      "falha recorrente. Nesse caso é obrigatória a análise de causa raiz "
                      "antes de nova intervenção, e é vedado repetir a troca de um "
                      "componente já substituído sem diagnóstico que a justifique."),
            ]),
            ("7", "MANUTENÇÃO PREVENTIVA", [
                ("p", "As revisões são controladas pelo horímetro, com tolerância de 10% "
                      "do intervalo. Acima da tolerância, a revisão está vencida. Quando "
                      "uma corretiva ocorre em equipamento com revisão vencida relacionada "
                      "ao sintoma, a revisão pendente deve ser executada na mesma parada."),
            ]),
            ("8", "PEÇAS E ESTOQUE", [
                ("p", "Verificar primeiro o almoxarifado da obra. Sem saldo, consultar os "
                      "demais almoxarifados, inclusive o central, para transferência antes "
                      "de requisitar compra. Registrar na triagem o prazo de reposição "
                      "quando não houver saldo em nenhum almoxarifado."),
            ]),
            ("9", "EQUIPAMENTO SUBSTITUTO", [
                ("p", "Para equipamento de criticidade A que precise parar, verificar a "
                      "existência de equipamento do mesmo tipo com status Disponível em "
                      "qualquer obra e indicar a possibilidade de remanejamento."),
            ]),
        ],
    },
]
