Atividade PBL – Aula 5: Testes Caixa-Preta e Caixa-Branca
🔹 1. Funcionalidade Selecionada
Funcionalidade: Busca de restaurantes.

O que a funcionalidade faz: Permite que o usuário pesquise restaurantes cadastrados no sistema através de uma barra de texto, utilizando palavras-chave (como o nome do local ou o tipo de culinária).

O que o usuário espera dela: O usuário espera digitar um termo e receber, de forma rápida, uma lista de restaurantes relevantes. Espera também que o sistema seja tolerante a pequenos erros de digitação e que, caso não exista o restaurante, retorne uma mensagem clara (ex: "Nenhum resultado encontrado") em vez de uma tela quebrada ou carregamento infinito.

🔹 2. Testes Caixa-Preta (Visão do Usuário)
Pensando sem conhecer o código, focamos nas entradas e saídas (comportamento da interface).

Quais testes faríamos:

Buscar por um restaurante que sabemos que existe.

Buscar por um termo genérico (ex: "Pizza") para ver se retorna múltiplos resultados.

Buscar por um termo que não existe.

Enviar o campo de busca totalmente em branco.

Inserir caracteres especiais (ex: !@#$%) ou textos muito longos.

Comportamentos esperados e Entradas:

Entrada: "Hamburgueria" (Termo válido). Comportamento: A tela exibe os cards de todas as hamburguerias cadastradas.

Entrada: "Xptz999" (Termo inexistente). Comportamento: A tela exibe a mensagem amigável: "Ops! Não encontramos nada com esse nome."

Entrada: [Em branco] e clicar em buscar. Comportamento: O sistema ignora a ação ou recarrega a lista padrão de restaurantes.

Situações de erro (Bugs que poderíamos encontrar):

O sistema travar (Infinite Loading) ao buscar um termo que não existe.

A busca diferenciar letras maiúsculas e minúsculas (ex: achar "Pizza", mas não achar "pizza").

Quebra do layout (UI) se o nome do restaurante retornado for muito grande.

🔹 3. Testes Caixa-Branca (Visão do Sistema)
Agora, imaginando que temos acesso ao código-fonte e à arquitetura do backend.

Como essa funcionalidade poderia estar implementada:
A barra de busca no Frontend (React/Vue) envia uma requisição GET para uma API no Backend (Node/Java). O backend recebe essa string, faz uma validação e executa uma consulta (query) no Banco de Dados (ex: SELECT * FROM restaurantes WHERE nome LIKE '%termo%'). Depois, retorna um Array (lista) no formato JSON para o Frontend desenhar na tela.

Possíveis estruturas lógicas (if, validações, regras):

if (input == null || input.trim() == ""): Regra para barrar buscas vazias antes mesmo de bater no banco de dados (evita processamento desnecessário).

try { //busca no banco } catch (Exception e) { //trata o erro }: Estrutura para evitar que a API "caia" se o banco de dados estiver fora do ar.

Funções de sanitização: Lógica para remover scripts maliciosos do texto digitado antes de pesquisar.

Situações que precisam ser testadas no código (Cobertura de rotas lógicas):

Segurança (SQL Injection): Testar se a variável da query está parametrizada ou se aceita comandos como ' OR 1=1 --.

Exceções de Banco: Simular uma queda de conexão com o banco e verificar se o bloco catch retorna o HTTP Status correto (ex: 500 Internal Server Error) ao invés de expor a stack trace (dados sensíveis do servidor) para o frontend.

Performance: Testar como o laço de repetição (for ou map) se comporta se a query retornar 10.000 restaurantes. Existe paginação implementada no código?

🔹 4. Comparação entre as abordagens
Qual a principal diferença?
A grande diferença está no foco da validação. O Teste Caixa-Preta avalia O QUÊ o sistema faz (se ele atende aos requisitos do negócio e à expectativa do usuário). Já o Teste Caixa-Branca avalia COMO o sistema faz (se o código é seguro, eficiente, se os loops funcionam corretamente e se todas as linhas de código foram exercitadas).

Que tipo de problema cada abordagem ajuda a encontrar?

Caixa-Preta: Encontra problemas de usabilidade, falhas em regras de negócio (ex: cupom de desconto aplicando valor errado), fluxos travados na tela e erros de tradução/layout.

Caixa-Branca: Encontra problemas de arquitetura, vulnerabilidades de segurança (injeção de código), vazamento de memória (memory leaks), código morto (variáveis não utilizadas) e falhas em tratamentos de exceção (NullPointerException).

🔹 5. Reflexão no contexto do LocalEats
Qual abordagem parece mais útil para os problemas atuais do sistema?
O contexto relata: "Funcionalidades inconsistentes, comportamentos inesperados e falhas em cenários específicos". Neste momento inicial, a abordagem Caixa-Preta é a mais urgente e útil. Precisamos mapear as dores do usuário, descobrir exatamente onde o sistema quebra na interface e criar uma documentação de cenários reprodutíveis para a equipe de desenvolvimento saber o que precisa ser corrigido do ponto de vista do produto.

Apenas uma abordagem seria suficiente?
Não. Elas são estritamente complementares. Se usarmos apenas a Caixa-Preta, o desenvolvedor pode até consertar o bug na tela (ex: fazer a busca não travar o app), mas o código por trás pode continuar ruim, lento e vulnerável a ataques. Por outro lado, testes de Caixa-Branca garantem que o código está perfeito, mas não garantem que o botão na tela da cor correta ou que a navegação faça sentido para quem está com fome querendo pedir comida. Para uma verdadeira Qualidade de Software, o LocalEats precisa das duas perspectivas trabalhando juntas
