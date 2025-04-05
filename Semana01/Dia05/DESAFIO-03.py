"""
DESAFIO 03:
Cálculo de juros

Vamos calcular quanto tempo (em anos) levará para
que um investimento inicial dobre, considerando uma
taxa de juros de 5% ao ano. Use um loop while para
realizar os cálculos.
"""
juros = 0.05
investimento_incial = 1000
valor_total = 0
ano = 0

while valor_total < investimento_incial*2:
    if valor_total == 0:
        valor_total = (investimento_incial * juros) + investimento_incial
        ano += 1

        print(f"Ano {ano}, Valor: R${valor_total:.2f}")

    else:
        valor_total += valor_total * juros
        ano += 1
        
        print(f"Ano {ano}, Valor: R${valor_total:.2f}")

print(f'Levou {ano} anos para alcançar o dobro do valor investido')