'''
DESAFIO 02:
Um Novo Slice

O segundo desafio será recriar o Slice e fazer o seu
dá sua maneira. Lembre-se que se nenhum
parâmetro for fornecido ele simplesmente copia o
array original inteiro.

Dica: Para funcionar parecido com o original, será
necessário enviar como primeiro parâmetro o próprio
array. O índice de início e fim podem receber valores
por padrão também.
'''
carroMaisVendidos = [
    'Fiat Strada',
    'Fiat Argo',
    'Hyundai HB20' ,
    'Chevrolet Onix',
    'Volkswagen Gol',
    'Renault Kwid',
    'Fiat Mobi',
    'Jeep Renegade' ,
    'Volkswagen T-Cross',
    'Toyota Corolla'
]


def extrairPorcao(lista: list, inicio=0, fim=None):
    if inicio == None and fim == None:
        return lista

    if fim is None:
        fim = len(lista)
    return lista[inicio:fim]


top5CarrosMaisVendidos = extrairPorcao(carroMaisVendidos, 0, 5)

teste = extrairPorcao(carroMaisVendidos)
    
print(top5CarrosMaisVendidos)

print(teste)