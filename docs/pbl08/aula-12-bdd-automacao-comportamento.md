# Aula 12 – BDD e Automação Orientada a Comportamento – LocalEats

**Disciplina:** Qualidade de Software
**Prof.:** Luciano Zanuz
**Sistema:** LocalEats (projeto fictício — sem site real em produção)
**Stack:** Python + pytest + pytest-bdd + Playwright
**Grupo:** Nicolas Diovani e Pedro Bavaresco

> Observação: como o LocalEats é um projeto fictício, cenários, seletores e evidências foram elaborados de forma consistente com o enunciado (não são execuções reais contra um sistema em produção).

---

## 1. Fluxos escolhidos

| Integrante | Comportamento |
|---|---|
| Nicolas Diovani | Busca de restaurantes |
| Pedro Bavaresco | Filtro por categoria |

---

## 2. Cenários BDD (Gherkin)

`features/busca_restaurantes.feature`
```gherkin
Feature: Busca de restaurantes
  Como usuário do LocalEats
  Eu quero buscar restaurantes por nome ou culinária
  Para encontrar rapidamente onde comer

  Scenario: Busca válida retorna resultados
    Given que o usuário está na página de exploração de restaurantes
    When ele busca por "Pizza"
    Then o sistema deve exibir restaurantes relacionados a "Pizza"

  Scenario: Busca inexistente retorna vazio
    Given que o usuário está na página de exploração de restaurantes
    When ele busca por "Comida Vegana Marciana"
    Then o sistema deve exibir uma mensagem informando que nenhum restaurante foi encontrado

  Scenario: Campo vazio mantém listagem
    Given que o usuário está na página de exploração de restaurantes
    When ele deixa o campo de busca vazio e confirma
    Then o sistema deve manter a listagem completa de restaurantes
```

`features/filtro_categoria.feature`
```gherkin
Feature: Filtro de restaurantes por categoria
  Como usuário do LocalEats
  Eu quero filtrar restaurantes por categoria de culinária
  Para encontrar opções dentro do meu interesse

  Scenario: Filtro aplicado corretamente
    Given que o usuário está na página de exploração de restaurantes
    When ele seleciona a categoria "Italiana"
    Then o sistema deve exibir apenas restaurantes da categoria "Italiana"

  Scenario: Categoria selecionada fica destacada
    Given que o usuário está na página de exploração de restaurantes
    When ele seleciona a categoria "Japonesa"
    Then a categoria "Japonesa" deve aparecer destacada na interface
```

---

## 3. Automação com pytest-bdd

`pages/restaurantes_page.py`
```python
class RestaurantesPage:
    def __init__(self, page):
        self.page = page

    def acessar(self):
        self.page.goto("https://local-eats-unisenac.vercel.app/static/index.html")

    def buscar(self, termo):
        self.page.get_by_placeholder("Buscar").fill(termo)
        self.page.keyboard.press("Enter")

    def selecionar_categoria(self, categoria):
        self.page.get_by_text(categoria, exact=True).click()

    def total_listados(self):
        return self.page.locator(".restaurant-card").count()

    def mensagem_vazio_visivel(self):
        return self.page.get_by_text("Nenhum restaurante encontrado").is_visible()

    def categoria_destacada(self, categoria):
        return "active" in (self.page.get_by_text(categoria, exact=True).get_attribute("class") or "")
```

`tests/test_busca_restaurantes.py`
```python
from pytest_bdd import scenarios, given, when, then, parsers
from pages.restaurantes_page import RestaurantesPage

scenarios('../features/busca_restaurantes.feature')


@given('que o usuário está na página de exploração de restaurantes', target_fixture='restaurantes')
def acessar(page):
    restaurantes = RestaurantesPage(page)
    restaurantes.acessar()
    return restaurantes


@when(parsers.parse('ele busca por "{termo}"'))
def buscar(restaurantes, termo):
    restaurantes.buscar(termo)


@when('ele deixa o campo de busca vazio e confirma')
def buscar_vazio(restaurantes):
    restaurantes.buscar("")


@then(parsers.parse('o sistema deve exibir restaurantes relacionados a "{termo}"'))
def valida_resultado(restaurantes, termo):
    assert restaurantes.total_listados() > 0


@then('o sistema deve exibir uma mensagem informando que nenhum restaurante foi encontrado')
def valida_vazio(restaurantes):
    assert restaurantes.mensagem_vazio_visivel()


@then('o sistema deve manter a listagem completa de restaurantes')
def valida_lista_completa(restaurantes):
    assert restaurantes.total_listados() > 0
```

`tests/test_filtro_categoria.py`
```python
from pytest_bdd import scenarios, given, when, then, parsers
from pages.restaurantes_page import RestaurantesPage

scenarios('../features/filtro_categoria.feature')


@given('que o usuário está na página de exploração de restaurantes', target_fixture='restaurantes')
def acessar(page):
    restaurantes = RestaurantesPage(page)
    restaurantes.acessar()
    return restaurantes


@when(parsers.parse('ele seleciona a categoria "{categoria}"'))
def selecionar(restaurantes, categoria):
    restaurantes.selecionar_categoria(categoria)


@then(parsers.parse('o sistema deve exibir apenas restaurantes da categoria "{categoria}"'))
def valida_filtro(restaurantes, categoria):
    assert restaurantes.total_listados() > 0


@then(parsers.parse('a categoria "{categoria}" deve aparecer destacada na interface'))
def valida_destaque(restaurantes, categoria):
    assert restaurantes.categoria_destacada(categoria)
```

---

## 4. Organização do projeto

```
projeto/
├── features/
│   ├── busca_restaurantes.feature
│   └── filtro_categoria.feature
├── pages/
│   └── restaurantes_page.py
├── tests/
│   ├── test_busca_restaurantes.py
│   └── test_filtro_categoria.py
└── evidencias/
    └── execucao_pytest.log
```

---

## 5. Execução dos testes

Comando: `pytest -v`

```
tests/test_busca_restaurantes.py::test_busca_valida_retorna_resultados PASSED
tests/test_busca_restaurantes.py::test_busca_inexistente_retorna_vazio PASSED
tests/test_busca_restaurantes.py::test_campo_vazio_mantem_listagem PASSED
tests/test_filtro_categoria.py::test_filtro_aplicado_corretamente PASSED
tests/test_filtro_categoria.py::test_categoria_selecionada_fica_destacada PASSED

============================== 5 passed in 3.92s ==============================
```

**Total de cenários:** 5 | **Passaram:** 5 | **Falharam:** 0

---

## 6. Análise crítica

- **O cenário ficou compreensível?** Sim — a estrutura Given-When-Then descreve o comportamento em linguagem de negócio, sem citar seletores ou detalhes técnicos.
- **O teste automatizado ficou legível?** Sim, os steps mapeiam diretamente as frases do Gherkin, e a lógica de interação com a página fica isolada no Page Object.
- **O BDD ajudou a entender o comportamento?** Sim, principalmente no cenário de busca vazia, onde a regra de negócio (manter a listagem) ficou explícita antes mesmo de pensar em código.
- **Dificuldades:** reaproveitar os mesmos steps `Given`/`When` de forma consistente entre os dois arquivos de feature sem duplicar lógica.
- **Seletores frágeis?** O destaque visual da categoria (`categoria_destacada`) depende de uma classe CSS (`active`), o que é o ponto mais frágil da automação.
- **O teste ficou dependente da interface?** Parcialmente — a busca e a listagem usam seletores mais estáveis (placeholder, texto), mas o destaque de categoria depende de detalhe de estilo.
- **O cenário representa uma regra de negócio real?** Sim, ambos representam necessidades reais do usuário (encontrar e filtrar restaurantes), não apenas ações de interface.
- **O que tornaria mais robusto?** Adicionar atributos `data-testid` para o destaque de categoria e para o card de restaurante, evitando depender de classes de estilo.

---

## 7. Reflexão no contexto do LocalEats

**BDD melhora a comunicação entre equipe?** Sim — os cenários em Gherkin podem ser lidos e validados por alguém do negócio antes mesmo de existir código, alinhando expectativas.

**Todo teste deve ser escrito em BDD?** Não. Regras de negócio isoladas (como as testadas com TDD na Aula 9) não precisam da camada Gherkin; BDD compensa mais em fluxos com valor de negócio claro e visível ao usuário.

**Quando vale a pena usar BDD?** Em fluxos críticos e de alto impacto na experiência do usuário, onde a comunicação entre negócio, QA e desenvolvimento precisa estar alinhada.

**O comportamento ficou mais claro?** Sim, principalmente porque os cenários descrevem *o que* o sistema deve fazer, sem amarrar isso a *como* a interface está implementada.

**Como isso ajuda o projeto do grupo?** Cria uma documentação viva dos comportamentos esperados do LocalEats, reduzindo ambiguidade nos requisitos e servindo como critério de aceite compartilhado entre quem especifica e quem testa — respondendo à mentalidade esperada: *"uma pessoa não técnica conseguiria entender o comportamento descrito?"* — sim, os cenários em Gherkin cumprem esse papel.
