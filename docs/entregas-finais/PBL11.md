# Aula 16 – Qualidade em Metodologias Ágeis – LocalEats

**Disciplina:** Qualidade de Software  
**Prof.:** Luciano Zanuz  
**Grupo:** Pedro Henrique Bavaresco dos Santos e Nicolas Diovani Oliveira Dias  

---

## 🔹 1. Análise de Práticas Ágeis no Processo

| Prática | Existe no processo? | Como é aplicada atualmente? | Pode ser melhorada? |
| :--- | :--- | :--- | :--- |
| **Planejamento iterativo** | Parcialmente | O projeto iniciou como um MVP apressado para atender ao prazo de um evento, gerando ações reativas para resolver bugs críticos. | Sim. A equipe pode adotar Sprints formais (Scrum) para planejar as correções e novas features em ciclos curtos e sustentáveis. |
| **Priorização de funcionalidades** | Sim | A equipe já prioriza ações baseadas no risco de negócio e impacto ao usuário (ex: prioridade máxima para problemas na "Busca e Filtragem" e "Avaliações"). | Sim. O papel do Product Owner (PO) deve ser consolidado para gerenciar e refinar constantemente o Product Backlog. |
| **Entregas incrementais** | Sim | Entregas são divididas entre os membros (ex: Nicolas focando no pedido, Pedro no frete). | Sim. Garantir que cada incremento seja totalmente testável antes de ir para a produção, evitando que novas funcionalidades quebrem o sistema. |
| **Feedback frequente** | Parcialmente | Atualmente o feedback vem na forma de reclamações de usuários e comerciantes apontando falhas. | Sim. Implementar reuniões de Revisão de Sprint com os stakeholders para alinhar expectativas antes que falhas cheguem aos usuários. |
| **Trabalho colaborativo** | Sim | Os desenvolvedores dividem a implementação das regras e os cenários de testes. | Sim. Formalizar a prática de Revisão de Código (Code Review) onde um dev valida o trabalho do outro. |
| **Controle visual das atividades** | Não | Não há menção explícita de um quadro visual no fluxo atual da equipe de desenvolvimento. | Sim. A adoção de ferramentas como GitHub Projects ajudará a evitar que o registro formal de bugs seja esquecido. |
| **Melhoria contínua** | Sim | A equipe mapeou a Dívida Técnica inicial e introduziu práticas de qualidade (QA) e BDD. | Sim. Instituir Retrospectivas de Sprint (Scrum) para analisar não apenas o código, mas as próprias falhas do processo da equipe. |

**Conclusão:**
O processo de desenvolvimento do LocalEats sofreu inicialmente pela cultura de "entregar rápido" decorrente de um lançamento de MVP apressado, acumulando dívida técnica grave. No entanto, a equipe possui maturidade técnica e capacidade de adaptação visíveis pela introdução de testes automatizados (unitários e BDD) para frear regressões. A maior oportunidade de melhoria está na adoção formal de ritos ágeis estruturados — como o uso do Kanban para controle visual e o refinamento prévio pelo PO —, transformando um desenvolvimento historicamente reativo em um processo colaborativo, previsível e orientado à segurança operacional do sistema.

---

## 🔹 2. Propostas de Melhoria Ágil

| Melhoria Proposta | Metodologia Relacionada | Benefício Esperado |
| :--- | :--- | :--- |
| **Instituir Code Review em todos os Pull Requests** | XP (Extreme Programming) | Um desenvolvedor sempre revisa o código do outro antes de enviar para a produção, evitando que bugs passem despercebidos e compartilhando o conhecimento da arquitetura. |
| **Utilizar um quadro visual para rastrear bugs e features** | Kanban | Maior visibilidade sobre o andamento das tarefas ("A Fazer", "Em Teste", "Concluído"), evitando que o registro formal de defeitos seja ignorado pela equipe. |
| **Garantir a execução da Pirâmide de Testes no CI** | XP / Integração Contínua | Como o foco deve ser maior nos testes unitários e de integração, a automação garante feedback rápido a cada commit, prevenindo o problema relatado de "novas funcionalidades quebrarem o sistema". |
| **Escrever especificações orientadas a comportamento (Gherkin) antes do código** | BDD / Lean | Cria uma documentação viva alinhando QA, negócio e desenvolvimento. Garante que os desenvolvedores codifiquem apenas o que entrega valor imediato e evita retrabalho e ambiguidades nos requisitos. |

---

## 🔹 3. Definition of Ready (DoR)

Para garantir que a equipe não comece a desenvolver de forma apressada (mitigando dívida técnica), a tarefa deve atender aos seguintes critérios antes de entrar na coluna "Em Desenvolvimento":

1. O requisito possui Critérios de Aceite definidos de forma clara pelo Product Owner (PO).
2. A funcionalidade foi priorizada com base no risco e impacto no negócio (ex: afeta o fluxo principal de checkout ou busca).
3. Em fluxos de interface, o protótipo visual (UI/UX) correspondente está disponível.
4. Possíveis cenários de Testes de Caixa-Preta (exceções, buscas vazias, etc) foram mapeados precocemente na concepção da tarefa.
5. O esforço técnico foi discutido pela equipe de desenvolvimento e cabe no ciclo atual da iteração.

---

## 🔹 4. Definition of Done (DoD)

Para considerar uma funcionalidade 100% pronta e evitar os problemas históricos do LocalEats onde o sistema quebrava em produção, ela deve atender aos seguintes requisitos:

1. O código desenvolvido passou por Revisão de Código (Code Review) por ao menos um outro desenvolvedor do grupo.
2. Testes unitários foram escritos e executados com sucesso, garantindo a correção lógica de regras críticas (como frete ou total do pedido).
3. Todos os critérios de aceite definidos pelo PO foram testados e validados pelo Analista de Qualidade/QA.
4. Testes funcionais/BDD executaram com sucesso na pipeline e cobrem o "caminho feliz" estipulado.
5. Não foram detectados bugs ou vazamentos que comprometam os atributos de Adequação Funcional e Usabilidade (ISO/IEC 25010).
