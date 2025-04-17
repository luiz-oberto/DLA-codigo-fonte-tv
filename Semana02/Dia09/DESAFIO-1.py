'''
DESAFIO 01:
Recrie funções uteis em Arrays

Imagine que você tenha um ranking de carros mais
vendidos no Brasil em um determinado ano. Esta
lista contém 10 carros, mas você deseja manipular
um array com apenas os Top 5.

O desafio é reescrever o que fazem essas três
funções no JavaScript: indexOf, includes e
lastIndexOf.

Dicas: O indexOf retorna um número inteiro que é a
posição do índice no array do primeiro elemento
encontrado no array. Caso esse elemento não seja
encontrado, devemos retornar "-1".

No includes o objetivo é saber se um elemento
existe ou não dentro de um array. Para isso a função
retorna true ou false, ou seja, um valor booleano.

E o lastIndexOf verifica o índice da última
ocorrência de um elemento no array. Se não for
encontrado, devemos retornar "-1".
'''

carroMaisVendidos = [
    'Fiat Strada',
    'Fiat Argo',
    'Hyundai HB20' ,
    'Chevrolet Onix',
    'Volkswagen Gol',
    'Renault Kwid',
    'Fiat Mobi',
    'Jeep Renegade' ,
    'Volkswagen T-Cross',
    'Toyota Corolla'
]


# Indexof - retorna o index do elemento procurado
def indexOf(nome: str, lista: list):
    
    indice = 0

    while indice < len(lista):
        
        if nome == lista[indice]:
            return print(indice)
        else:
            indice+=1
    
    print('-1')



def includes(nome: str, lista: list):
    
    indice = 0

    while indice < len(lista):
        
        if nome == lista[indice]:
            return print('True')
        else:
            indice+=1
    
    print('False')
    


def lastIndexOf(nome: str, lista: list):
    indice = -1

    for i in lista:
        if nome == lista[indice]:

            indexOf(nome, lista)

            return
        
        else:
            indice -= 1

    print('-1')



indexOf('Volkswagen Gol', carroMaisVendidos)

includes('Volkswagen Gol', carroMaisVendidos)

lastIndexOf('Volkswagen T-Cross', carroMaisVendidos)