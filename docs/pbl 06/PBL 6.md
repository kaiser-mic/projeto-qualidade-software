# Aula 9 – Testes Unitários Automatizados e TDD – LocalEats

**Disciplina:** Qualidade de Software
**Prof.:** Luciano Zanuz
**Sistema:** LocalEats — https://local-eats-unisenac.vercel.app/
**Stack utilizada nos testes:** Python 3.12 + pytest 9.1.1
**Grupo:** Nicolas Diovani e Pedro Bavaresco.

---

## 1. Funcionalidades escolhidas

| Integrante | Funcionalidade | Arquivo |
|---|---|---|
| Nicolas | Cálculo do total do pedido com valor mínimo | `pedido.py` / `test_pedido.py` |
| Pedro | Cálculo de taxa de entrega por distância | `frete.py` / `test_frete.py` |

### 1.1 Cálculo do total do pedido com valor mínimo

**O que faz:** soma os preços dos itens do pedido e verifica se o total atinge o valor mínimo exigido pelo restaurante.

**Problema que resolve:** evita que pedidos abaixo do valor mínimo avancem no fluxo de compra.

**Importância:** é uma regra central do checkout — está diretamente ligada à receita mínima por pedido do restaurante.

**Regras de negócio:**
- Total = soma do preço de todos os itens
- Se total < valor mínimo → erro (`ValueError`)
- Se total ≥ valor mínimo → retorna o total (pedido válido)

### 1.2 Cálculo de taxa de entrega por distância

**O que faz:** calcula o valor da entrega com base na distância entre restaurante e cliente.

**Problema que resolve:** padroniza a cobrança de frete, evitando cálculos manuais ou inconsistentes entre restaurantes.

**Importância:** impacta diretamente o valor final pago pelo cliente e a percepção de transparência do app.

**Regras de negócio:**
- Distância até 3 km → taxa fixa de R$ 5,00
- Distância acima de 3 km → taxa proporcional (R$ 2,50 por km)
- Distância negativa → erro (`ValueError`), pois é um dado inválido

---

## 2. Testes Unitários

### 2.1 Nicolas — `pedido.py`

**Teste 1 (happy path)**
- **Nome descritivo:** `test_deve_calcular_total_quando_valor_minimo_e_atingido`
- **Cenário testado:** soma de itens cujo total é maior que o valor mínimo
- **Dados de entrada:** `itens = [{"preco": 10}, {"preco": 20}]`, `valor_minimo = 15`
- **Resultado esperado:** retorna `30`, sem erro

```python
def test_deve_calcular_total_quando_valor_minimo_e_atingido():
    itens = [{"preco": 10}, {"preco": 20}]
    valor_minimo = 15
    resultado = calcular_total_pedido(itens, valor_minimo)
    assert resultado == 30
```

**Teste 2 (happy path / borda)**
- **Nome descritivo:** `test_deve_calcular_total_quando_total_e_exatamente_igual_ao_minimo`
- **Cenário testado:** total exatamente igual ao valor mínimo (limite da regra "≥")
- **Dados de entrada:** `itens = [{"preco": 15}]`, `valor_minimo = 15`
- **Resultado esperado:** retorna `15`, sem erro

```python
def test_deve_calcular_total_quando_total_e_exatamente_igual_ao_minimo():
    itens = [{"preco": 15}]
    valor_minimo = 15
    resultado = calcular_total_pedido(itens, valor_minimo)
    assert resultado == 15
```

**Teste 3 (erro)**
- **Nome descritivo:** `test_deve_lancar_erro_quando_total_e_menor_que_valor_minimo`
- **Cenário testado:** total abaixo do valor mínimo exigido
- **Dados de entrada:** `itens = [{"preco": 5}, {"preco": 3}]`, `valor_minimo = 15`
- **Resultado esperado:** lança `ValueError`

```python
def test_deve_lancar_erro_quando_total_e_menor_que_valor_minimo():
    itens = [{"preco": 5}, {"preco": 3}]
    valor_minimo = 15
    with pytest.raises(ValueError):
        calcular_total_pedido(itens, valor_minimo)
```

### 2.2 Pedro — `frete.py`

**Teste 1 (happy path)**
- **Nome descritivo:** `test_deve_aplicar_taxa_fixa_para_distancia_ate_3km`
- **Cenário testado:** distância dentro do intervalo de taxa fixa
- **Dados de entrada:** `distancia_km = 2`
- **Resultado esperado:** retorna `5.0`

```python
def test_deve_aplicar_taxa_fixa_para_distancia_ate_3km():
    resultado = calcular_taxa_entrega(2)
    assert resultado == 5.0
```

**Teste 2 (happy path / borda)**
- **Nome descritivo:** `test_deve_aplicar_taxa_fixa_no_limite_de_3km`
- **Cenário testado:** distância exatamente no limite de 3 km
- **Dados de entrada:** `distancia_km = 3`
- **Resultado esperado:** retorna `5.0` (ainda taxa fixa, pois a regra é "até 3 km")

```python
def test_deve_aplicar_taxa_fixa_no_limite_de_3km():
    resultado = calcular_taxa_entrega(3)
    assert resultado == 5.0
```

**Teste 3 (happy path)**
- **Nome descritivo:** `test_deve_aplicar_taxa_proporcional_para_distancia_acima_de_3km`
- **Cenário testado:** distância acima do limite, cobrança proporcional
- **Dados de entrada:** `distancia_km = 10`
- **Resultado esperado:** retorna `25.0` (10 × 2,5)

```python
def test_deve_aplicar_taxa_proporcional_para_distancia_acima_de_3km():
    resultado = calcular_taxa_entrega(10)
    assert resultado == 25.0
```

**Teste 4 (erro)**
- **Nome descritivo:** `test_deve_lancar_erro_para_distancia_negativa`
- **Cenário testado:** distância negativa (dado inválido)
- **Dados de entrada:** `distancia_km = -5`
- **Resultado esperado:** lança `ValueError`

```python
def test_deve_lancar_erro_para_distancia_negativa():
    with pytest.raises(ValueError):
        calcular_taxa_entrega(-5)
```

---

## 3. Aplicação do TDD (Red → Green → Refactor)

Ciclo completo aplicado nas duas funcionalidades. Abaixo, o detalhamento para a funcionalidade do **Nicolas** (cálculo do total do pedido); o mesmo processo foi repetido para a funcionalidade do Pedro (taxa de entrega).

### 🔴 Red — teste escrito antes do código, com falha demonstrada

Antes de existir qualquer implementação, o arquivo `test_pedido.py` já importava `calcular_total_pedido` de um módulo `pedido.py` inexistente. Ao rodar os testes, o resultado foi falha de coleta:

```
ImportError while importing test module 'test_pedido.py'.
E   ModuleNotFoundError: No module named 'pedido'
=========================== short test summary info ============================
ERROR test_pedido.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.12s ===============================
```

Isso confirma que o teste foi escrito **antes** do código de produção e que, de fato, falha sem ele.

### 🟢 Green — implementação mínima para os testes passarem

```python
def calcular_total_pedido(itens, valor_minimo):
    total = 0
    for item in itens:
        total = total + item["preco"]
    if total < valor_minimo:
        raise ValueError("erro")
    return total
```

Resultado da execução:

```
test_pedido.py::test_deve_calcular_total_quando_valor_minimo_e_atingido PASSED [ 33%]
test_pedido.py::test_deve_calcular_total_quando_total_e_exatamente_igual_ao_minimo PASSED [ 66%]
test_pedido.py::test_deve_lancar_erro_quando_total_e_menor_que_valor_minimo PASSED [100%]
============================== 3 passed in 0.01s ===============================
```

Código propositalmente "cru": usa laço `for` manual e mensagem de erro genérica (`"erro"`), só o suficiente para os testes passarem.

### 🔵 Refactor — melhoria mantendo os testes verdes

```python
def calcular_total_pedido(itens: list[dict], valor_minimo: float) -> float:
    """Soma o preço dos itens do pedido e valida o valor mínimo do restaurante."""
    total = sum(item["preco"] for item in itens)

    if total < valor_minimo:
        raise ValueError(
            f"Valor mínimo do pedido não atingido: total R$ {total}, mínimo R$ {valor_minimo}"
        )

    return total
```

Após a refatoração, os 3 testes continuaram passando, sem nenhuma alteração no arquivo de testes — prova de que o comportamento externo da função não mudou, apenas sua implementação interna.

---

## 4. Refatoração — melhorias realizadas

| Função | Antes | Depois | Justificativa |
|---|---|---|---|
| `calcular_total_pedido` | Laço `for` manual acumulando total | `sum()` com generator expression | Mais legível e idiomático em Python |
| `calcular_total_pedido` | Mensagem de erro genérica `"erro"` | Mensagem descritiva com os valores envolvidos | Facilita debug e dá contexto de negócio ao erro |
| `calcular_total_pedido` | Sem type hints | Assinatura tipada (`list[dict]`, `float`) | Deixa o contrato da função explícito |
| `calcular_taxa_entrega` | Números mágicos (`3`, `5.0`, `2.5`) espalhados no corpo da função | Constantes nomeadas (`DISTANCIA_LIMITE_TAXA_FIXA_KM`, `TAXA_FIXA`, `VALOR_POR_KM`) | Se a regra de negócio mudar (ex.: novo valor por km), a alteração é feita em um único lugar, sem "caçar" números no código |
| `calcular_taxa_entrega` | Estrutura `if/else` redundante | `if` com `return` antecipado (guard clause) | Reduz aninhamento e melhora a leitura do fluxo |
| Ambas | Sem docstring | Docstring de uma linha explicando a regra | Documenta a intenção da função para quem for mantê-la |

Nenhuma refatoração alterou o comportamento externo das funções — isso foi validado reexecutando a suíte de testes após cada mudança, sem qualquer alteração nos testes em si.

---

## 5. Execução dos Testes

**Comando executado:** `python -m pytest -v`

```
============================= test session starts ==============================
platform linux -- Python 3.12.3, pytest-9.1.1, pluggy-1.6.0
collecting ... collected 7 items

test_frete.py::test_deve_aplicar_taxa_fixa_para_distancia_ate_3km PASSED [ 14%]
test_frete.py::test_deve_aplicar_taxa_fixa_no_limite_de_3km PASSED       [ 28%]
test_frete.py::test_deve_aplicar_taxa_proporcional_para_distancia_acima_de_3km PASSED [ 42%]
test_frete.py::test_deve_lancar_erro_para_distancia_negativa PASSED      [ 57%]
test_pedido.py::test_deve_calcular_total_quando_valor_minimo_e_atingido PASSED [ 71%]
test_pedido.py::test_deve_calcular_total_quando_total_e_exatamente_igual_ao_minimo PASSED [ 85%]
test_pedido.py::test_deve_lancar_erro_quando_total_e_menor_que_valor_minimo PASSED [100%]

============================== 7 passed in 0.01s ===============================
```

**Resumo:**
- **Total de testes:** 7
- **Passaram:** 7
- **Falharam:** 0

---

## 6. Reflexão no contexto do LocalEats

**Foi difícil escrever testes antes do código?**
No início exige uma mudança de hábito: é preciso pensar na *regra de negócio* e nos seus casos-limite antes de pensar em "como implementar". Depois de definir bem as regras (o que já havíamos feito em aulas anteriores de planejamento de testes), escrever os testes primeiro ficou natural — eles funcionaram quase como uma especificação executável da funcionalidade.

**O TDD ajudou no desenvolvimento?**
Sim. Ao escrever o teste da taxa de entrega para distância exatamente igual a 3 km, por exemplo, ficamos obrigados a decidir explicitamente se o limite era inclusivo ou exclusivo — uma ambiguidade que passaria despercebida se o código fosse escrito primeiro e os testes depois, apenas "confirmando" o que o código já fazia.

**Os testes aumentaram a confiança no código?**
Sim, principalmente durante a refatoração. Trocar o laço `for` por `sum()`, ou extrair os números mágicos da taxa de entrega para constantes, foram mudanças feitas com segurança porque a suíte de testes validava, em menos de um segundo, que nada tinha quebrado.

**O que melhoraríamos?**
- Adicionar mais testes de borda (ex.: pedido com lista de itens vazia, distância igual a 0)
- Validar tipos de entrada (ex.: preço negativo em um item, o que hoje não é tratado)
- Medir cobertura de código com `pytest-cov` para identificar caminhos não testados

**Como isso ajuda no projeto do grupo?**
Regras de negócio como valor mínimo do pedido e cálculo de frete são exatamente os pontos onde bugs de regressão mais aparecem conforme o LocalEats evolui (ex.: alguém muda a taxa por km e esquece de atualizar o limite de distância). Ter esses testes automatizados significa que qualquer alteração futura nessas funções será validada em segundos, sem depender de teste manual, e qualquer regressão será detectada imediatamente — respondendo diretamente à pergunta guia da atividade: *"Se eu mudar esse código amanhã, meus testes vão garantir que nada quebre?"* — sim, para essas duas regras, vão.
