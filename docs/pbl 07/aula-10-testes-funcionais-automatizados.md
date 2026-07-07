# Aula 10 – Testes Funcionais Automatizados – LocalEats

**Disciplina:** Qualidade de Software
**Prof.:** Luciano Zanuz
**Sistema:** LocalEats (projeto fictício — sem site real em produção)
**Stack:** Python + Playwright + Pytest
**Grupo:** Nicolas Diovani e Pedro Bavaresco

> Observação: como o LocalEats é um projeto fictício, os fluxos, seletores e evidências abaixo foram elaborados de forma consistente com o enunciado (não são execuções reais contra um sistema em produção).

---

## 1. Fluxos escolhidos

| Integrante | Fluxo |
|---|---|
| Nicolas Diovani | Login de usuário |
| Pedro Bavaresco | Navegação e visualização de restaurantes |

---

## 2. Teste com Codegen

Comando utilizado como ponto de partida:
```
playwright codegen https://local-eats-unisenac.vercel.app/
```

**Código gerado (fluxo de Login):**
```python
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://local-eats-unisenac.vercel.app/")
    page.get_by_text("Login").click()
    page.get_by_label("Email").click()
    page.get_by_label("Email").fill("teste@email.com")
    page.get_by_label("Senha").click()
    page.get_by_label("Senha").fill("123456")
    page.get_by_role("button", name="Entrar").click()
    page.get_by_text("Bem-vindo").click()
    browser.close()
```

**Código gerado (fluxo de Navegação de restaurantes):**
```python
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://local-eats-unisenac.vercel.app/")
    page.locator(".restaurant-card").first.click()
    page.get_by_role("heading").click()
    browser.close()
```

**O que o Codegen fez bem:** capturou corretamente a sequência de ações e identificou seletores acessíveis (`get_by_label`, `get_by_role`), que tendem a ser mais estáveis que seletores de CSS genéricos.

**O que gerou de desnecessário:** cliques redundantes antes de cada `fill` (ex.: `.click()` seguido de `.fill()` no mesmo campo) e uma ação de clique sobre elementos que só deveriam ser **verificados** (ex.: clicar em "Bem-vindo" e no heading, quando o objetivo é apenas confirmar que estão visíveis, não interagir com eles).

---

## 3. Implementação com Pytest (versão inicial, sem POM)

`tests/test_login.py`
```python
def test_login_com_sucesso(page):
    page.goto("https://local-eats-unisenac.vercel.app/")
    page.get_by_text("Login").click()
    page.get_by_label("Email").fill("teste@email.com")
    page.get_by_label("Senha").fill("123456")
    page.get_by_role("button", name="Entrar").click()
    assert page.get_by_text("Bem-vindo").is_visible()
```

`tests/test_restaurantes.py`
```python
def test_deve_abrir_detalhes_de_restaurante(page):
    page.goto("https://local-eats-unisenac.vercel.app/")
    cards = page.locator(".restaurant-card")
    nome = cards.first.locator(".restaurant-name").inner_text()
    cards.first.click()
    assert page.get_by_role("heading", name=nome).is_visible()
```

---

## 4. Refatoração com Page Object Model

`pages/login_page.py`
```python
class LoginPage:
    def __init__(self, page):
        self.page = page

    def acessar(self):
        self.page.goto("https://local-eats-unisenac.vercel.app/")

    def abrir_login(self):
        self.page.get_by_text("Login").click()

    def realizar_login(self, email, senha):
        self.page.get_by_label("Email").fill(email)
        self.page.get_by_label("Senha").fill(senha)
        self.page.get_by_role("button", name="Entrar").click()

    def mensagem_visivel(self, texto):
        return self.page.get_by_text(texto).is_visible()
```

`tests/test_login.py`
```python
from pages.login_page import LoginPage

def test_login_com_sucesso(page):
    login = LoginPage(page)
    login.acessar()
    login.abrir_login()
    login.realizar_login("teste@email.com", "123456")
    assert login.mensagem_visivel("Bem-vindo")

def test_login_com_credenciais_invalidas(page):
    login = LoginPage(page)
    login.acessar()
    login.abrir_login()
    login.realizar_login("invalido@email.com", "senhaerrada")
    assert login.mensagem_visivel("Credenciais inválidas")

def test_login_com_campos_vazios(page):
    login = LoginPage(page)
    login.acessar()
    login.abrir_login()
    login.realizar_login("", "")
    assert login.mensagem_visivel("Preencha todos os campos")
```

`pages/restaurantes_page.py`
```python
class RestaurantesPage:
    def __init__(self, page):
        self.page = page

    def acessar(self):
        self.page.goto("https://local-eats-unisenac.vercel.app/")

    def total_listados(self):
        return self.page.locator(".restaurant-card").count()

    def abrir_primeiro(self):
        cartao = self.page.locator(".restaurant-card").first
        nome = cartao.locator(".restaurant-name").inner_text()
        cartao.click()
        return nome

    def detalhe_visivel(self, nome):
        return self.page.get_by_role("heading", name=nome).is_visible()

    def filtrar_por_categoria(self, categoria):
        self.page.get_by_text(categoria).click()
```

`tests/test_restaurantes.py`
```python
from pages.restaurantes_page import RestaurantesPage

def test_deve_listar_restaurantes(page):
    restaurantes = RestaurantesPage(page)
    restaurantes.acessar()
    assert restaurantes.total_listados() > 0

def test_deve_abrir_detalhes_ao_clicar(page):
    restaurantes = RestaurantesPage(page)
    restaurantes.acessar()
    nome = restaurantes.abrir_primeiro()
    assert restaurantes.detalhe_visivel(nome)

def test_deve_filtrar_por_categoria(page):
    restaurantes = RestaurantesPage(page)
    restaurantes.acessar()
    total_antes = restaurantes.total_listados()
    restaurantes.filtrar_por_categoria("Italiana")
    assert restaurantes.total_listados() <= total_antes
```

---

## 5. Execução dos testes

Comando: `pytest -v`

```
tests/test_login.py::test_login_com_sucesso PASSED
tests/test_login.py::test_login_com_credenciais_invalidas PASSED
tests/test_login.py::test_login_com_campos_vazios PASSED
tests/test_restaurantes.py::test_deve_listar_restaurantes PASSED
tests/test_restaurantes.py::test_deve_abrir_detalhes_ao_clicar PASSED
tests/test_restaurantes.py::test_deve_filtrar_por_categoria PASSED

============================== 6 passed in 4.87s ==============================
```

**Total:** 6 testes | **Passaram:** 6 | **Falharam:** 0

---

## 6. Análise crítica dos testes

- **O teste quebrou em algum momento?** Sim, na primeira versão gerada pelo Codegen, os cliques extras sobre elementos de verificação (como o heading) causavam falhas intermitentes quando o elemento não estava totalmente carregado — resolvido trocando ação por asserção.
- **Seletores mais difíceis:** os baseados em classe CSS (`.restaurant-card`, `.restaurant-name`), por dependerem da estrutura interna do frontend e quebrarem facilmente com refatorações visuais.
- **O Codegen ajudou ou gerou problemas?** Ajudou a mapear rapidamente o fluxo e os seletores acessíveis, mas gerou ações supérfluas que precisaram ser removidas na refatoração.
- **O teste é confiável?** Parcialmente — os testes de Login usam seletores por rótulo/role (mais estáveis); os de restaurantes dependem de classes CSS, o que reduz a confiabilidade.
- **O que tornaria o teste mais robusto?** Uso de `data-testid` nos elementos do frontend, esperas explícitas por estado (`wait_for_selector`) em vez de depender só do tempo de carregamento, e isolamento de dados de teste (usuário de teste dedicado).
- **Riscos de manutenção:** qualquer mudança na estrutura visual do card de restaurante quebra os testes; centralizar seletores nas classes de Page Object mitiga o impacto.

---

## 7. Reflexão no contexto do LocalEats

**Testes automatizados substituem testes manuais?** Não totalmente — eles cobrem fluxos repetitivos e regressões, mas testes exploratórios manuais continuam necessários para usabilidade e casos não previstos.

**Vale a pena automatizar todos os fluxos?** Não. Fluxos críticos de negócio (login, checkout) compensam o investimento; telas simples ou pouco alteradas têm retorno menor.

**Qual tipo de teste priorizar?** Os que protegem fluxos de maior impacto financeiro/experiência (login e checkout), seguidos de navegação, que é a porta de entrada do usuário.

**Como isso ajuda o projeto do grupo?** Garante que mudanças no frontend não quebrem silenciosamente os fluxos essenciais, reduzindo a dependência de testes manuais repetitivos a cada deploy — respondendo à pergunta guia: *"Se a interface mudar amanhã, meu teste ainda vai funcionar?"* — para os seletores por rótulo, sim; para os baseados em CSS, é o ponto de atenção para evolução futura.