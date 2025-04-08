"""
SUPER DESAFIO:
Aplicação de Finanças

Como ainda não estudamos estrutura de dados e
nem o conceito de listas e arrays, então o que iremos
fazer, é criar 2 variáveis que controlam o saldo de 2
contas bancárias. As contas compartilham de um
limite (que também será um outra variável), porém
começa com 0.

A partir do momento que o saldo total das contas
atingir R$1000, o limite será de 10%. Utilizando um
saldo inicial dessas contas, efetue alguns cálculos
através de funções que façam o seguinte:

1. Calcular o saldo total das contas
2. Exibir um alerta caso alguma conta esteja sem
saldo ou utilizando o limite
3. Fazer depósito em alguma das contas
4. Efetuar débito em alguma das contas
5. Transferir um determinado valor de uma conta
para outra, somente se tiver saldo disponível
6. Fazer a conversão do saldo (que está em R$) para
dólar (US$)
7. Exibir o limite disponível

Só para complicar um pouco, se ao efetuar um
depósito em uma conta ela estiver usando um limite,
desconte do valor a ser depositado 15%.
"""
conta_1 = 1.0
conta_2 = 10.0
limite = 0

def saldo_total():
    total = conta_1 + conta_2
    print(f"Saldo total das contas: R${total}")
    return

def verificar_conta():
    if conta_1 == 0 and conta_2 == 0:
        print('SEM SALDO NAS CONTAS.')
    elif conta_1 == 0:
        print('Conta 1: SEM SALDO.')
    elif conta_2 == 0:
        print('Conta 2: SEM SALDO.')
    # falta verificar limite!!!
    return

# FALTA AJUSTES!!!
def depositar(valor: float, conta):
    print(f"Efutando depósito de R${valor:.2f}")
    conta += valor
    print(f"Depósito efetuado.\n \nSaldo: R${conta}\n")
    return conta

def debitar(valor: float, conta):
    print(f"Efutando débito de R${valor:.2f}")
    conta -= valor
    print(f"Débito efetuado.\n \nSaldo: R${conta}\n")

# saldo_Total()
# verificar_conta()
depositar(100, conta_2)
debitar(10, conta_2)