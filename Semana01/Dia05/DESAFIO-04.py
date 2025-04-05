"""
DESAFIO 04:
Compra parcelada

Suponha que você comprou um produto e optou por
parcelar o valor em 12 vezes sem juros. Escreva um
código que imprima o valor de cada parcela e o valor
restante a ser pago.
"""
valor_produto = 1000
qtd_parcelas = 12

valor_parcela = valor_produto / qtd_parcelas

for parcela in range(1, qtd_parcelas+1):
    valor_atualizado = valor_produto if parcela == 1 else valor_atualizado - valor_parcela
    print(f"Parcela {parcela}: R${valor_parcela:.2f}")
    print(f"Falta pagar R${valor_atualizado:.2f}")
    print()

