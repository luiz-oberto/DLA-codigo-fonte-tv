'''
DESAFIO 01:
Ordenação: organizando a bagunça

Imagine que nós temos uma lista de produtos em um
mercado em um array onde temos o nome e o preço
de venda. Ou seja, nós teremos um array dentro de
outro array. Como esse no código abaixo:

const produtos = [
["Arroz", 25.99],
["Feijão", 12.50],
["Leite", 6.49],
["Óleo", 8.99],
["Pão", 7.00],
["Café", 15.30],
["Açúcar", 4.89],
["Sal", 3.25],
["Macarrão", 5.79],
["Manteiga", 9.99]
];

O desafio será criar a função de ordenação desse
array. Fique à vontade para escolher algum dos
algoritmos que te explicamos.

Lembretes!

1. Disponibilizamos para você baixar esse array com
os dados para serem ordenado;
2. Baixe o PDF com o material adicional para
conhecer o código e as explicações dos outros
algoritmos de ordenação;
3. Confira o vídeo sobre recursividade do Código
Fonte TV: https://youtu.be/NKymAD4pJZI
'''

produtos = [
["Arroz", 25.99],
["Feijão", 12.50],
["Leite", 6.49],
["Óleo", 8.99],
["Pão", 7.00],
# ["Café", 15.30],
# ["Açúcar", 4.89],
# ["Sal", 3.25],
# ["Macarrão", 5.79],
# ["Manteiga", 9.99]
]


def selection_sort(lista):

    i, j = 0, 0

    while j < len(lista):

        min_value_position = j
        min_value = produtos[j]

        while i < len(lista):
                            
            if i == len(lista)-1:
                break

            if lista[i+1][1] > min_value[1]:
                print(lista[i+1])
                i+=1

            else:
                min_value = lista[i+1]
                print('valor mínimo: ',min_value)
                min_value_position = i + 1
                i+=1
        
        temp_new_value = lista.pop(min_value_position)
        temp_old_value = lista.pop(j) # ERRO
        lista.insert(j, temp_new_value)
        lista.insert(min_value_position, temp_old_value)

        
        j+=1
        i = 0
        print(lista)

    return


selection_sort(produtos)

# produtos.insert(1, ["café", 15.30])
# print(produtos)