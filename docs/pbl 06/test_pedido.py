from pedido import calcular_total_pedido
import pytest


def test_deve_calcular_total_quando_valor_minimo_e_atingido():
    itens = [{"preco": 10}, {"preco": 20}]
    valor_minimo = 15
    resultado = calcular_total_pedido(itens, valor_minimo)
    assert resultado == 30


def test_deve_calcular_total_quando_total_e_exatamente_igual_ao_minimo():
    itens = [{"preco": 15}]
    valor_minimo = 15
    resultado = calcular_total_pedido(itens, valor_minimo)
    assert resultado == 15


def test_deve_lancar_erro_quando_total_e_menor_que_valor_minimo():
    itens = [{"preco": 5}, {"preco": 3}]
    valor_minimo = 15
    with pytest.raises(ValueError):
        calcular_total_pedido(itens, valor_minimo)
