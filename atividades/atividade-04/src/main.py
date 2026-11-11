def pedido_atingiu_valor_minimo(valor_pedido):
    if valor_pedido < 0:
        raise ValueError("O valor do pedido não pode ser negativo.")

    if valor_pedido >= 30:
        return True
    else:
        return False


#funcao felipe

# src/regras_localeats.py

def calcular_desconto(valor_pedido):
    """
    Calcula o desconto do pedido:
    - Pedidos abaixo de R$ 100,00 não recebem desconto (retorna 0).
    - Pedidos de R$ 100,00 ou mais recebem 10% de desconto (retorna o valor do desconto).
    - Valores negativos geram ValueError.
    """
    if valor_pedido < 0:
        raise ValueError("O valor do pedido não pode ser negativo.")
    
    if valor_pedido >= 100.0:
        return valor_pedido * 0.10
    return 0.0