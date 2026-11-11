# Atividade 4 Qualidade de Software

**Identificação**
Turma: Qualidade Software noite
Modalidade: dupla
Repositório: [colar o link do repositório]
Diretório da atividade: [colar o link direto para este diretório]
Data da última execução: [dd/mm/aaaa]

**Integrantes**
Rene Arthur Rocha de Souza
Felipe Tatsuya Aso

## Tabela de testes

| ID | Integrante | Tipo | Comportamento verificado | Arquivo e função |
| --- | --- | --- | --- | --- |
| TU01 | Rene | Unitário | Valor mínimo do pedido | tests/test_pedido.py::test_pedido_reconhece_valor_minimo_corretamente 
| TU02 | Rene | Unitário | Valor negativo do pedido | tests/test_pedido.py::test_pedido_valor_negativo_levanta_excecao 
| TF01 | Rene | Funcional | Favorita restaurante e exclui restaurante favorito | tests/test_favorito.py::test_favorito 
| TU03 | Felipe | Unitário | Cálculo de desconto do pedido | tests/test_regras_localeats.py::test_calcular_desconto_aplicavel
| TU04 | Felipe | Unitário | Pedido abaixo do limite de desconto | tests/test_regras_localeats.py::test_calcular_sem_desconto
| TF02 | Felipe | Funcional | Seleção de categoria no LocalEats | tests/test_localeats.py::test_selecionar_categoria

## TDD de Rene Arthur Rocha de Souza

**Regra escolhida:** 
- "Regra 1: verificar valor mínimo do pedido"

**Primeiro teste escrito:**
- test_pedido_reconhece_valor_minimo_corretamente

**Por que o teste falhou inicialmente:** Pois não estava implementado

**Implementação mínima realizada:**

```python
def pedido_atingiu_valor_minimo(valor_pedido):
    if valor_pedido >= 30:
        return True
    else:
        return False
```

**Segundo teste escrito:**
- test_pedido_valor_negativo_levanta_excecao

**Melhoria ou refatoração realizada:** (adicionado a exceção)

```python
def pedido_atingiu_valor_minimo(valor_pedido):
    if valor_pedido < 0:
        raise ValueError("O valor do pedido não pode ser negativo.")

    if valor_pedido >= 30:
        return True
    else:
        return False
```

## TDD de Felipe Tatsuya Aso

**Regra escolhida:** 
- "Regra 2: calcular o desconto do pedido"

**Primeiro teste escrito:**
- `test_calcular_desconto_aplicavel` (verifica se pedidos de R$ 100,00 ou mais recebem 10% de desconto)

**Por que o teste falhou inicialmente:** 
- Pois a função `calcular_desconto` ainda não havia sido implementada na suíte de testes[cite: 4, 5].

**Implementação mínima realizada:**

```python
def calcular_desconto(valor_pedido):
    if valor_pedido >= 100.0:
        return valor_pedido * 0.10
    return 0.0
```

**Segundo teste escrito:**
- test_calcular_desconto_valor_negativo

**Melhoria ou refatoração realizada:** (adicionado a exceção)

```python
def calcular_desconto(valor_pedido):
    if valor_pedido < 0:
        raise ValueError("O valor do pedido não pode ser negativo.")

    if valor_pedido >= 100.0:
        return valor_pedido * 0.10
    return 0.0
```
## Uso de inteligência artificial

**Ferramenta utilizada:** ChatGPT

**Como a ferramenta foi utilizada:** Duvidas pontuais

**Uma sugestão que precisou ser alterada ou rejeitada:** No código apenas um comando "to_be_empty" do playwright que descobri por meio de uma dúvida. E também foi convertido o comando "python -m pytest -v | Tee-Object -FilePath relatorio-pytest.txt" para "python -m pytest -v | tee relatorio-pytest.txt", o equivalente no Linux.

**Como o código sugerido foi verificado:** Não deu erro de sintaxe de código, e também foi colocado o "" antes de excluir o restaurante como favorito, e deu erro pois a div não estava vazia "AssertionError: Locator expected to be empty", então o comando funciona como esperado.
