Estratégia Inicial de Testes – LocalEats
1. Funcionalidades Principais
Com base no escopo e nos problemas relatados, selecionamos as 4 funcionalidades que representam o Core Business (coração do negócio) do LocalEats:

Busca e Filtragem: Busca de restaurantes por tipo de culinária, localização e preço.

Sistema de Avaliações: Criação, exibição e persistência das avaliações dos usuários.

Catálogo de Restaurantes: Visualização de cardápios e fotos.

Gestão de Favoritos: Ação de salvar e listar locais favoritos.

2. Níveis de Teste
Abaixo detalhamos o que será validado em cada camada para as funcionalidades escolhidas:

Funcionalidade 1: Busca e Filtragem
Teste Unitário: Validar a lógica matemática/algoritmo dos filtros (ex: se a função que filtra "preço < R$50" está retornando o array correto).

Teste de Integração: Validar a comunicação entre o serviço de busca (Backend) e o banco de dados, garantindo que a query retorne os restaurantes corretos.

Teste de Sistema: Testar o fluxo na interface: o usuário preenche os filtros, clica em buscar e a tela renderiza a lista de restaurantes.

Teste de Aceitação: Validar se os resultados retornados fazem sentido para a intenção real do usuário (ex: se pesquisar "barato e perto", ele não deve ver um restaurante caro a 20km de distância).

Funcionalidade 2: Sistema de Avaliações
Teste Unitário: Validar regras de validação (ex: a função impede dar nota maior que 5 ou enviar texto vazio?).

Teste de Integração: Validar se, ao enviar uma avaliação via API, ela é corretamente gravada e mantida no banco de dados (atacando o problema das avaliações que "desaparecem").

Teste de Sistema: Preencher o formulário de avaliação na UI, submeter e verificar se a nota é atualizada na página do restaurante.

Teste de Aceitação: Validar se a experiência de compartilhar a avaliação é fácil, intuitiva e gera confiança no usuário.

Funcionalidade 3: Catálogo de Restaurantes
Teste Unitário: Validar funções de formatação (ex: transformar o dado 25.5 no texto R$ 25,50 para o cardápio).

Teste de Integração: Validar a comunicação com o serviço de armazenamento de imagens (AWS S3, por exemplo) para garantir que as fotos carreguem.

Teste de Sistema: Navegar da home até a página do restaurante e verificar se o cardápio e fotos abrem corretamente, sem quebrar o layout.

Teste de Aceitação: Garantir que o usuário consegue ler o cardápio facilmente para decidir seu pedido, sem se frustrar com telas confusas.

Funcionalidade 4: Gestão de Favoritos
Teste Unitário: Validar a lógica de adicionar/remover o ID de um restaurante da lista de favoritos na memória.

Teste de Integração: Validar se a API sincroniza corretamente os favoritos da conta do usuário, para garantir que o que foi salvo no Web apareça no Mobile.

Teste de Sistema: Clicar no ícone de "salvar/favoritar" e verificar se o item vai para a aba correta na interface.

Teste de Aceitação: Garantir que o usuário consegue acessar rapidamente seus lugares preferidos para futuras visitas.

3. Prioridades e Riscos
Pensando na crise de imagem atual e nas reclamações, a priorização deve ser baseada em risco de negócio e impacto ao usuário final.

Prioridade Máxima (Crítica): Busca e Filtragem. * Justificativa: É a porta de entrada. Se a busca traz "resultados incorretos", o usuário não acha o restaurante e abandona o app imediatamente (Churn alto).

Prioridade Alta: Sistema de Avaliações.

Justificativa: A dor mais grave relatada pela associação de comerciantes é a "reputação". Avaliações sumindo destroem a confiança tanto do dono do restaurante quanto do cliente. Isso precisa ser estabilizado com urgência.

Prioridade Média: Catálogo e Menus.

Justificativa: Erros aqui dificultam ações simples, mas se a busca e a confiança (avaliações) estiverem funcionando, o usuário tem um pouco mais de tolerância para tentar recarregar uma foto que não abriu.

Prioridade Baixa: Favoritos.

Justificativa: É uma funcionalidade de retenção, não de aquisição. Se falhar, é frustrante, mas não impede a função central do app (conectar cliente e restaurante).

4. Pirâmide de Testes
Onde concentrar maior quantidade de testes? (Base da Pirâmide)
A maior concentração deve ser nos Testes Unitários e de Integração (backend/APIs).

Justificativa: Como temos "inconsistências entre versão web e mobile" e "avaliações que desaparecem", o problema real está na persistência de dados e nas APIs, não apenas nas telas. Testes nessas camadas são baratos, executam em milissegundos e garantem que as regras de negócio funcionam para todas as plataformas.

Onde usar menos testes? (Topo da Pirâmide)
A menor quantidade deve estar nos Testes de Sistema/E2E (Ponta a Ponta) e UI.

Justificativa: Eles são fundamentais para validar fluxos cruciais (como a "dificuldade para concluir ações simples"), mas são muito caros de manter, rodam devagar e quebram facilmente quando o design muda. Devem ser focados apenas nos "caminhos felizes" das prioridades máximas.

5. Testes em Produção
O sistema deveria usar testes em produção? Sim, absolutamente indispensável para a realidade do LocalEats.

Em quais situações e por quê?

Testes de Carga e Monitoramento (Observabilidade): O sistema sofre com "lentidão em horários de pico". O ambiente de homologação raramente simula o volume exato do horário de almoço/jantar de um evento gastronômico real. Monitorar a performance em produção é crucial para escalar servidores na hora certa.

Testes de Dispositivos Reais (Beta Testing/Analytics): Como há "falhas em determinados smartphones", é impossível a equipe de QA ter todos os aparelhos do mundo no escritório. Usar ferramentas de captura de crash (Crashlytics) em produção ajuda a mapear quais modelos exatos estão falhando.

A/B Testing ou Feature Flags: Para resolver o problema de "telas confusas e pouco intuitivas", novas interfaces devem ser lançadas aos poucos (ex: liberar a tela nova para apenas 10% dos usuários) em produção. Assim, medimos a aceitação real sem impactar 100% da base caso a nova versão seja pior.
