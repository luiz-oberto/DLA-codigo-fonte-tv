'''
DESAFIO 02:
Fila de supermercado em código

O segundo desafio será codificar uma fila do mundo
real. Nós escolhemos uma fila de supermercado.
Esse conceito é interessante, pois em um
supermercado se forma a fila a partir de caixas
individuais, diferentemente dos bancos onde existe
apenas uma fila para diversos caixas.

Comece com a formação de uma fila a partir de um
único caixa em um mercado e depois, em outro
momento, vamos expandir o conceito para filas em
diversos caixas. Pense agora em quantas operações
podem existir nessa fila.

Dica: Nós entramos na fila e depois somos
atendidos. Ou seja, nós somos adicionados à fila e
depois nós saímos da fila.
'''

# fila
# fila = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# # caixa
# caixa_1 = []

# while len(fila) > 0:
#     primeiro = fila.pop(0)

#     caixa_1.append(primeiro)
#     print(f'Atendendo o cliente {primeiro}')

fila = []

def entrarNaFila(nome):
    fila.append(nome)
    print(f'{nome} entrou na fila')


def atenderCliente():
    while len(fila) > 0:

        primeiro = fila.pop(0)
        print(f'Atentendo o cliente {primeiro}')

    else:
        print('Não há clientes para atender.')


def mostrarFila():
    print(fila)
    

entrarNaFila('Luiz')
entrarNaFila('Laís')

mostrarFila()

atenderCliente()