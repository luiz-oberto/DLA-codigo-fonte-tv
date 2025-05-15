def selection_sort(lista: list):

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

#
album = [
    {
    "name": "wake",
    "artist": "Linkin Park",
    "reproductionTime": "1:43"
    },
    {
    "name": "Given Up",
    "artist": "Linkin Park",
    "reproductionTime": "3:11"
    },
    {
    "name": "Leave Out All the Rest",
    "artist": "Linkin Park",
    "reproductionTime": "3:31"
    },
    {
    "name": "Bleed It Out",
    "artist": "Linkin Park",
    "reproductionTime": "2:46"
    },
    {
    "name": "Shadow of the Day",
    "artist": "Linkin Park",
    "reproductionTime": "4:52"
    },
    {
    "name": "What I've Done",
    "artist": "Linkin Park",
    "reproductionTime": "3:28"
    }
]

musica1 = album[0]
musica2 = album[1]
# print(musica1)
# print(musica2)
# print(musica1['reproductionTime'] < musica2['reproductionTime'])
# print(musica1['name'] > musica2['name']) # quanto maior a letra, maior o valor
# ex: 'e' > 'a' ==> True
palavra1 = 'what'
palavra2 = 'wake' # em nosso caso a palavra1 deveria vir antes da palavra2
print(palavra2[0])
# se primeira letra da palavra1 é igual a primeira letra da palavra2
# Então, verifique a ordem entre as segundas letras de cada palavra
if palavra1[0] == palavra2[0]:
    print(palavra1[1] < palavra2[1])

# produtos_organizado = selection_sort(produtos)

# for i in produtos_organizado:
#     print(i)