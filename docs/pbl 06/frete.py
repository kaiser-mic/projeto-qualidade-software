DISTANCIA_LIMITE_TAXA_FIXA_KM = 3
TAXA_FIXA = 5.0
VALOR_POR_KM = 2.5


def calcular_taxa_entrega(distancia_km: float) -> float:
    """Calcula a taxa de entrega: fixa até o limite, proporcional acima dele."""
    if distancia_km < 0:
        raise ValueError("Distância inválida: não pode ser negativa")

    if distancia_km <= DISTANCIA_LIMITE_TAXA_FIXA_KM:
        return TAXA_FIXA

    return round(distancia_km * VALOR_POR_KM, 2)
