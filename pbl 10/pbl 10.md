# Aula 15 – Modelos de Maturidade – LocalEats

**Centro Universitário Senac-RS**  
**Curso:** ADS – Análise e Desenvolvimento de Sistemas / SPI – Sistemas para Internet  
**Unidade Curricular:** Qualidade de Software  
**Professor:** Luciano Zanuz

## Integrantes

- Nicolas Diovani
- Pedro Bavaresco

---

# 1. Diagnóstico de Maturidade

A seguir, apresentamos uma avaliação do processo de desenvolvimento utilizado pela equipe durante o projeto **LocalEats**, considerando conceitos de maturidade de processos inspirados nos modelos **CMMI** e **MPS.BR**.

| Critério | Sim | Parcial | Não |
|----------|:---:|:-------:|:---:|
| Os requisitos são documentados? | | ✔ | |
| Existe controle de mudanças? | ✔ | | |
| Há atividades de teste definidas? | ✔ | | |
| Os defeitos são registrados? | | ✔ | |
| O processo de desenvolvimento é conhecido por toda a equipe? | ✔ | | |
| As tarefas são planejadas e acompanhadas regularmente? | ✔ | | |
| Existe padronização para implementação de funcionalidades? | | ✔ | |
| Os testes são executados antes da entrega das funcionalidades? | ✔ | | |
| Há revisão de código ou validação por outro integrante da equipe? | | ✔ | |
| A equipe utiliza ferramentas para gerenciamento das atividades? | ✔ | | |
| Os artefatos do projeto (requisitos, testes e código) são organizados e versionados? | ✔ | | |
| Existe rastreabilidade entre requisitos e funcionalidades implementadas? | | ✔ | |
| A equipe realiza reuniões ou retrospectivas para identificar melhorias? | | ✔ | |
| Existem indicadores ou métricas para acompanhar a qualidade do projeto? | | | ✔ |

---

## Classificação do Processo

### **Nível de Maturidade: Gerenciado**

### Justificativa

O processo da equipe pode ser classificado como **Gerenciado**, pois existe planejamento das atividades, controle de versões, organização do trabalho e execução de testes antes das entregas. Entretanto, ainda existem oportunidades de melhoria relacionadas à documentação dos requisitos, utilização de métricas, revisão sistemática de código e definição de padrões mais formais para o desenvolvimento. O processo já é seguido pelos integrantes, mas ainda não está completamente padronizado e continuamente melhorado, características presentes em níveis mais elevados de maturidade.

---

# 2. Lacunas Identificadas

| Lacuna | Impacto |
|--------|---------|
| Ausência de métricas de qualidade | Dificulta medir produtividade, qualidade e evolução do projeto. |
| Documentação parcial dos requisitos | Pode gerar dúvidas durante o desenvolvimento e retrabalho. |
| Revisão de código sem um processo formal | Aumenta a possibilidade de erros permanecerem no código. |
| Rastreabilidade parcial entre requisitos e funcionalidades | Torna mais difícil identificar quais requisitos foram atendidos. |
| Poucas reuniões de retrospectiva | Reduz a identificação de melhorias contínuas no processo. |

---

# 3. Propostas de Melhoria

| Melhoria | Benefício |
|----------|-----------|
| Implementar revisões de código (Code Review) antes de cada entrega | Redução de defeitos e compartilhamento de conhecimento entre os integrantes. |
| Definir um padrão para documentação dos requisitos | Melhor compreensão das funcionalidades e redução de retrabalho. |
| Utilizar métricas de qualidade (bugs encontrados, cobertura de testes, tempo de desenvolvimento) | Permite acompanhar a evolução do projeto e tomar decisões baseadas em dados. |
| Criar uma matriz de rastreabilidade entre requisitos, testes e funcionalidades | Facilita a manutenção e validação do sistema. |
| Realizar retrospectivas ao final de cada ciclo de desenvolvimento | Promove melhoria contínua e aperfeiçoamento do processo. |

---

# Relação com os Modelos CMMI e MPS.BR

Os modelos **CMMI** e **MPS.BR** demonstram que a qualidade do software depende diretamente da qualidade do processo utilizado para desenvolvê-lo. No caso da equipe do LocalEats, já existem práticas importantes, como planejamento, testes e controle de versões, que indicam um processo organizado.

Entretanto, ainda há espaço para evoluir por meio da formalização de procedimentos, utilização de métricas e adoção de práticas de melhoria contínua. Essas ações aproximariam o processo dos níveis mais altos de maturidade, tornando o desenvolvimento mais previsível, eficiente e confiável.

---

# Conclusão

A análise mostrou que o processo de desenvolvimento da equipe apresenta um bom nível de organização, podendo ser classificado como **Gerenciado**. Os integrantes seguem um fluxo definido para implementar funcionalidades, realizar testes e entregar o software.

Apesar disso, ainda existem oportunidades para aumentar a maturidade do processo, principalmente na padronização das atividades, documentação, uso de métricas e realização de revisões formais. A adoção dessas melhorias contribuirá para reduzir falhas, aumentar a produtividade da equipe e elevar a qualidade do produto final.