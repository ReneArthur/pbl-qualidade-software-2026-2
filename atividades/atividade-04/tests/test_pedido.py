import pytest

from src.main import pedido_atingiu_valor_minimo 

# Por: Rene Arthur Rocha de Souza
def test_pedido_reconhece_valor_minimo_corretamente():
    assert pedido_atingiu_valor_minimo(30) == True
    assert pedido_atingiu_valor_minimo(29) == False

# Por: Rene Arthur Rocha de Souza
def test_pedido_valor_negativo_levanta_excecao():
    with pytest.raises(ValueError):
        pedido_atingiu_valor_minimo(-1)
