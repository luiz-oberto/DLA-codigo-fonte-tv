'''
SUPER DESAFIO:
Controlar filas de vários
caixas de supermercado
Lembra que no dia 8 você resolveu um problema
envolvendo o controle de uma fila de caixa de
supermercados? Vamos voltar nesse desafio, mas
agora para controlar várias filas ao mesmo tempo, ou
seja, teremos a simulação real de um supermercado
com vários caixas.

As funções deverão ser adaptadas para essa nova
realidade. Imagine, um supermercado com 10 caixas,
e consequentemente, 10 filas.
'''
import random

random.seed(40)


caixas = [ 
    {
    "caixa": 1,
    "filaCaixa": [1],
    "preferencial": True,
    "caixa Rapido": False,
    },

    {
    "caixa": 2,
    "filaCaixa": [1,2, 3],
    "preferencial": True,
    "caixa Rapido": False,
    },

    {
    "caixa": 3,
    "filaCaixa": [1],
    "preferencial": True,
    "caixa Rapido": False,
    },

    {
    "caixa": 4,
    "filaCaixa": [],
    "preferencial": False,
    "caixa Rapido": False,
    },

    {
    "caixa": 5,
    "filaCaixa": [],
    "preferencial": False,
    "caixa Rapido": False,
    },
]



# FUNÇÕES
def verificarCaixasPreferenciais():

    caixasPreferenciais = []

    for caixa in caixas:
        if caixa['preferencial']:
            caixasPreferenciais.append(caixa)

    return caixasPreferenciais



def verificarMenorFila(listaCaixas: list):
    print('LISTA DOS CAIXAS ',listaCaixas)
    lista = []
    indice = 0
    menorFila = {}

    while indice < len(listaCaixas):

        if menorFila == {}:
            menorFila = listaCaixas[indice]
        
        elif len(menorFila['filaCaixa']) > len(listaCaixas[indice]['filaCaixa']):
            menorFila = listaCaixas[indice]

        indice+=1

    print(f'A menor fila é {menorFila}')
    print()
    return menorFila

        

        
        

# passo o cliente com informação se é preferencial ou não e a lista de caixas
def adicionarClienteFila(cliente: dict):

    if cliente['preferencial']:
        # print(f'O cliente {cliente['cliente']} é preferencial')

        caixasPreferenciais = verificarCaixasPreferenciais()

        # menorFila = 
        verificarMenorFila(caixasPreferenciais)

        # print(f'o caixa com menor fila é {caixas[menorFila]}')

        # caixas[menorFila]["filaCaixa"].append(cliente)


        return
    
    else:
        # adicionar clientes sem preferências aos caixas normais
        print(f'Adicionando cliente {cliente['cliente']} ao caixa normal...')
        



clientes = []


for i in range(1, 3):
    cliente = {
        'cliente': i,
        'preferencial': random.choice([True, False])
    }

    adicionarClienteFila(cliente)
    clientes.append(cliente)

print('\n----- EXIBINDO CLIENTES ---------')
for c in clientes:
    print(c)

print()
print(caixas[0])



# ------ CÓDIGO RASCUNHO -----------
# i = 3

# retorna apenas as chaves dentro do dicionário
# chaves = caixas.keys()
# print(chaves)

# for key in chaves:
#     print(key)

# BLOCO QUE PODE SER ÚTIL
# if f"caixa{i}" in chaves:
#     print(f'Caixa {i} existe :))')
# else:
#     print('Caixa inexistente')

# caixas[f"filaCaixa{i}"].append('cliente1')
# v = caixas[f"filaCaixa{i}"]
# print(v)