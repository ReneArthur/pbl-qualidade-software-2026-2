import pytest

from src.main import calcular_desconto 

#======================================================
# Responsável: [Felipe Tatsuya Aso]

def test_calcular_desconto_aplicavel():
    """Testa se pedidos de R$ 100,00 ou mais retornam 10% de desconto."""
    resultado = calcular_desconto(150.0)
    assert resultado == 15.0

def test_calcular_sem_desconto():
    """Testa se pedidos abaixo de R$ 100,00 retornam zero de desconto."""
    resultado = calcular_desconto(80.0)
    assert resultado == 0.0

def test_calcular_desconto_valor_negativo():
    """Testa se valores negativos geram ValueError na função de desconto."""
    with pytest.raises(ValueError):
        calcular_desconto(-10.0)