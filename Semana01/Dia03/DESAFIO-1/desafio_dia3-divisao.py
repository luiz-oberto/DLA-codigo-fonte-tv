# DESAFIOS PARA DIVISÃO

# 1. Calcule a média de quatro notas
notas = {
    "nota_01": 8.1,
    "nota_02": 9.0,
    "nota_03": 6.7,
    "nota_04": 10.0
}

soma = 0
indice = 0
for nota in notas.values():
    soma = soma + nota
    indice+=1

media = soma/indice
print(f'Média das notas: {media}')


# 2. Converter a distância de metros para quilômetros.
metros = 23500.0

conversao = metros / 1000

print(f"{metros} metros equivale a {conversao} km")