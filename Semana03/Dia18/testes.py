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
    "name": "Wake",
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

musica1 = album[0]['name']
musica2 = album[5]['name']

for i in range(len(musica1)):
    if musica1[i] < musica2[i]:
        print(f'{musica1[i]} < {musica2[i]}')
        print(f'a música {musica1} vem antes da música {musica2}')
        # break
    
    elif musica1[i] > musica2[i]:
        print(f'{musica1[i]} < {musica2[i]}')
        print(f'a música {musica2} vem depois da música {musica1}')

    else:
        print(f'{musica1[i]} == {musica2[i]}')
        print(f'a música {musica1} possui a mesma letra da música {musica2}')
        print('Seguindo pra próxima letra')

# print('w' < 'G')