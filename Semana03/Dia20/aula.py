'''
# Buscar é a mágina da programação
A ferramenta de busca é uma das ferramentas mais imortantes da programação. Toda hora estamos buscando algo, seja um diretório, uma música, um livro, etd. Existem na programação alguns tipos de busca:

- Busca Linear
    Pecorre todos os elementos de uma lista (ou array) um por um, do início ao fim, até encontrar o valor desejado ou até acabar a lista.
    "É como procurar página por página uma palavra no dicionário."

- Busca Binária
    Só funciona em listas ordenadas. Ela divide a lista ao meio repetidamente para eliminar metade dos elementos a cada passo, procurando o valor desejado de forma muito mais eficiente.

'''

# Exemplos - BUSCA LINEAR
NOMES = ["Ana", "Bruno", "Carlos", "Daniela"]

def busca_linear(lista, valor):
    for nome in range(0, len(lista)-1):
        if lista[nome] == valor:
            return nome
        
    return -1 # se não encontrar


def busca_linear_recursiva(lista, valor, indice = 0):
    if indice >= len(lista):
        return -1
    if lista[indice] == valor:
        return indice
    
    return busca_linear_recursiva(lista, valor, indice + 1)


print(busca_linear(NOMES, "Carlos"))

# Exemplos - BUSCA BINÁRIA
def busca_binaria(lista, valor):
    inicio = 0
    fim = len(lista)-1

    while inicio <= fim:
        MEIO = (inicio + fim)// 2

        if lista[MEIO] == valor:
            return MEIO
        
        if lista[MEIO] < valor:
            inicio = MEIO + 1
        else:
            fim = MEIO - 1
    
    return -1

lista = [10, 20, 30, 40, 50, 60]
print(busca_binaria(lista, 10))