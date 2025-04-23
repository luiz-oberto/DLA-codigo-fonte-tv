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

# lISTA DE CAIXAS
caixas = [ 
    {
    "caixa": 1,
    "filaCaixa": [],
    "preferencial": True,
    "caixa Rapido": False,
    },

    {
    "caixa": 2,
    "filaCaixa": [],
    "preferencial": True,
    "caixa Rapido": False,
    },

    {
    "caixa": 3,
    "filaCaixa": [],
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

    {
    "caixa": 6,
    "filaCaixa": [],
    "preferencial": False,
    "caixa Rapido": False,
    },

    {
    "caixa": 7,
    "filaCaixa": [],
    "preferencial": False,
    "caixa Rapido": False,
    },

    {
    "caixa": 8,
    "filaCaixa": [],
    "preferencial": False,
    "caixa Rapido": False,
    },

    {
    "caixa": 9,
    "filaCaixa": [],
    "preferencial": False,
    "caixa Rapido": False,
    },

    {
    "caixa": 10,
    "filaCaixa": [],
    "preferencial": False,
    "caixa Rapido": False,
    },
]



# FUNÇÕES
# Acha os caixas PREFERÊNCIAIS
def acharCaixasPreferenciais():

    caixasPreferenciais = []

    for caixa in caixas:
        if caixa['preferencial']:
            caixasPreferenciais.append(caixa)

    return caixasPreferenciais


# acha os caixas NÃO PREFERÊNCIAIS
def acharCaixas():

    caixasNormais = []

    for caixa in caixas:
        if caixa['preferencial'] == False:
            caixasNormais.append(caixa)

    return caixasNormais


# Verifica o caixa com a menor fila para se adicionar o cliente
def verificarMenorFila(listaCaixas: list):

    indice = 0
    menorFila = {}

    while indice < len(listaCaixas):

        if menorFila == {}:
            menorFila = listaCaixas[indice]
        
        elif len(menorFila['filaCaixa']) > len(listaCaixas[indice]['filaCaixa']):
            menorFila = listaCaixas[indice]

        indice+=1

    return menorFila



# Adiciona um cliente a fila
def adicionarClienteFila(cliente: dict):

    if cliente['preferencial']:

        caixasPreferenciais = acharCaixasPreferenciais()

        menorFila = verificarMenorFila(caixasPreferenciais)

        menorFila["filaCaixa"].append(cliente)
    
    else:
        caixasNormais = acharCaixas()

        menorFila = verificarMenorFila(caixasNormais)

        menorFila['filaCaixa'].append(cliente)
        



# CRIAR CLIENTES
def gerarClientes(qtdClientes):
    clientes = []

    for i in range(1, qtdClientes + 1):
        cliente = {
            'cliente': i,
            'preferencial': random.choice([True, False])
        }

        clientes.append(cliente)
        adicionarClienteFila(cliente)

    print('\n----- EXIBINDO CLIENTES ---------')
    for c in clientes:
        print(c)



print()
gerarClientes(50)

for caixa in caixas:
    print(f'caixa {caixa['caixa']}')
    print(f'fila {caixa['filaCaixa']}\n')
