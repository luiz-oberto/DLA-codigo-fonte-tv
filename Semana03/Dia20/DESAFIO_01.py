'''
DESAFIO 01:

Implementar a busca binária de um array de
números, porém utilizando recursividade, assim
como mostramos na busca linear. Teste também
com um array com nomes para ver como funcionará.
'''
# Exemplos - BUSCA BINÁRIA
def busca_binaria_recursiva(lista: list, valor, inicio = 0, fim = None):
    if fim == None:
        fim = len(lista)

    if inicio > fim:
        return -1 # caso base: valor não encontrado

    MEIO = (inicio + fim)//2

    if lista[MEIO] == valor:
        return MEIO # caso base: valor encontrado
    
    if valor < lista[MEIO]:
        return busca_binaria_recursiva(lista, valor, inicio, MEIO - 1)

    return busca_binaria_recursiva(lista, valor, MEIO + 1, fim)        



lista = [10, 20, 30, 40, 50, 60]

print(busca_binaria_recursiva(lista, 20))