from frete import calcular_taxa_entrega
import pytest


def test_deve_aplicar_taxa_fixa_para_distancia_ate_3km():
    resultado = calcular_taxa_entrega(2)
    assert resultado == 5.0


def test_deve_aplicar_taxa_fixa_no_limite_de_3km():
    resultado = calcular_taxa_entrega(3)
    assert resultado == 5.0


def test_deve_aplicar_taxa_proporcional_para_distancia_acima_de_3km():
    resultado = calcular_taxa_entrega(10)
    assert resultado == 25.0


def test_deve_lancar_erro_para_distancia_negativa():
    with pytest.raises(ValueError):
        calcular_taxa_entrega(-5)
