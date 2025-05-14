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
["Café", 15.30],
["Açúcar", 4.89],
["Sal", 3.25],
["Macarrão", 5.79],
["Manteiga", 9.99]
]

# talvez mude para selection sort
def selection_sort(lista: list):
    if isinstance(lista, list):

        i, j = 0, 0
        temp = lista[i]

        while j != len(lista)-1:
            
            if temp[1] > lista[i+1][1]:
                temp = lista[i+1]

            i+=1

            if i == len(lista)-1:
                menor_valor = lista.pop(lista.index(temp))
                lista.insert(j, menor_valor)
                j+=1
                temp = lista[j]
                i=j

    return lista

# ORGANIZANDO E EXIBINDO PRODUTOS
produtos_organizado = selection_sort(produtos)

for i in produtos_organizado:
    print(i)

'''
# SAÍDA:
['Sal', 3.25]
['Açúcar', 4.89]
['Macarrão', 5.79]
['Leite', 6.49]
['Pão', 7.0]
['Óleo', 8.99]
['Manteiga', 9.99]
['Feijão', 12.5]
['Café', 15.3]
['Arroz', 25.99]
'''