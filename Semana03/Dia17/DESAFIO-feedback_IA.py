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

def selection_sort(lista: list) -> list:
    n = len(lista)
    for i in range(n):
        indice_menor = i
        for j in range(i+1, n):
            if lista[j][1] < lista[indice_menor][1]:
                indice_menor = j
        if indice_menor != i:
            lista[i], lista[indice_menor] = lista[indice_menor], lista[i]
    return lista

produtos_organizado = selection_sort(produtos)
for nome, preco in produtos_organizado:
    print(f"{nome}: R$ {preco:.2f}")

"""
⚠️ Pontos de Melhoria:
1. Uso de variáveis i e j confuso
O uso simultâneo de i e j de forma dinâmica torna o código mais difícil de entender.

No Selection Sort, normalmente percorremos a lista a partir de um índice i e buscamos o menor elemento nos 
índices seguintes (i+1 até o fim), depois trocamos com i.

2. Modificações diretas com pop() e insert()
Essas operações mudam a lista enquanto ela está sendo percorrida, o que pode causar confusão ou até bugs em outras situações.

O Selection Sort clássico faz apenas troca de elementos (swap), e não remoções/inserções.

3. Nome da função
selection_sort é um nome ótimo, mas se for usada em outro contexto, uma docstring explicando que ordena uma lista de 
sublistas com base no segundo item seria útil.

4. Checagem de tipo não é essencial
A checagem com isinstance(lista, list) não é muito útil aqui, pois se não for uma lista, o código quebraria 
de qualquer forma. Prefira lançar um erro (raise TypeError(...)) se quiser algo robusto.
"""