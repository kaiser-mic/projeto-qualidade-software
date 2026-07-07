def calcular_total_pedido(itens: list[dict], valor_minimo: float) -> float:
    """Soma o preço dos itens do pedido e valida o valor mínimo do restaurante."""
    total = sum(item["preco"] for item in itens)

    if total < valor_minimo:
        raise ValueError(
            f"Valor mínimo do pedido não atingido: total R$ {total}, mínimo R$ {valor_minimo}"
        )

    return total
