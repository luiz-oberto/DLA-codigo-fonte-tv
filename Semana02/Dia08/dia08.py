'''
# Entidades

# Principais estruturas de dados
- arrays ou vetor
- Objetos
- Listas encadeadas
- Pilhas
- Filas
- deques
- Conjuntos
- Dicionários
- Tabelas Hash
- Árvores 
- Grafos

Em python, trabalhar com arrays só é possível a partir do uso de uma biblioteca chamada Numpy, 
na qual é voltada para computação vetorizada.

As listas são como arrays, a diferença é que arrays suportam apenas um tipo de dado enquanto listas aceitam 
guardar vários tipos de dados em diferentes índices

array = [1, 2, 3, 4]

lista =  ['uma string', 2, True, 5.463]

'''

# import numpy as np

NUMERO_CONTAS = 10
saldos = []
# saldos = np.arange(NUMERO_CONTAS)

# # print(type(saldos))
# # print(saldos)

# # saldo da conta 5
# print(saldos[4])

# vamos imaginar quee listas são arrays
for i in range(NUMERO_CONTAS):
    saldos.append(0)

print(saldos)

print(saldos[4])

print(len(saldos))
