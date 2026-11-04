def pedido_atingiu_valor_minimo(valor_pedido):
    if valor_pedido < 0:
        raise ValueError("O valor do pedido não pode ser negativo.")

    if valor_pedido >= 30:
        return True
    else:
        return False