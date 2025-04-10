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

6. Fazer a conversão do saldo (que está em R$) para dólar (US$)
7. Exibir o limite disponível

Só para complicar um pouco, se ao efetuar um
depósito em uma conta ela estiver usando um limite,
desconte do valor a ser depositado 15%.
"""
conta_1 = 0.0
conta_2 = 10.0
limite = 0


# 1. Calcular o saldo total das contas - FEITO
def saldo_total():
    total = conta_1 + conta_2
    return total

# Apenas exibe o saldo das contas
def exibir_saldo():
    print(f"Conta 1: R${conta_1:.2f}")
    print(f"Conta 2: R${conta_2:.2f}")
    print(f'Limite no cartão: R${limite:.2f}')
    total = saldo_total()
    print(f"Saldo total das contas: R${total:.2f}\n")
    return

# 2. Exibir um alerta caso alguma conta esteja sem saldo ou utilizando o limite
def verificar_conta():
    if conta_1 == 0 and conta_2 == 0:
        print('SEM SALDO NAS CONTAS.')
    elif conta_1 == 0:
        print('Conta 1: SEM SALDO.')
    elif conta_2 == 0:
        print('Conta 2: SEM SALDO.')
    else:
        print("Contas OK.")
    # falta verificar limite!!!
    return

# 3. Fazer depósito em alguma das contas - FEITO
def depositar(valor: float, conta):
    print(f'Depositando R${valor:.2f}\n')
    conta += valor
    return conta

# 4. Efetuar débito em alguma das contas - FEITO
def debitar(valor: float, conta, limite):
    print("Efetuando pagamento...")
    if valor > conta:
        print("Saldo insuficiente, utilizando limite disponível...")
        limite -= valor
        return conta, limite

    print(f'Debitando R${valor:.2f}\n')
    conta -= valor
    return conta

# 5. Transferir um determinado valor de uma conta para outra, somente se tiver saldo disponível - FEITO
def trasferencia(valor: float, conta_origem, conta_destino, limite):
    conta_origem = debitar(valor, conta_origem,limite)
    conta_destino = depositar(valor, conta_destino)
    return conta_origem, conta_destino

# Verifica o aumento de limite
def aumentar_limite():
    if saldo_total() >= 1000:
        print("Seu limite aumentou em 10%")
        limite = saldo_total() * 0.10
        print(f'Limite atual {limite:.2f}\n')
    else:
        print("Aumento de limite não autorizado.\n")
    return limite


verificar_conta()

# Depositando dinheiro
conta_1  = depositar(1000, conta_1)

# Debitando dinehro
conta_1 = debitar(10, conta_1, limite)

# Transferência
print("Efetuando transferencia...")
conta_1, conta_2 = trasferencia(40, conta_1, conta_2, limite)

# Verificando aumento de limite
exibir_saldo()
print("Verificando limite...")
limite = aumentar_limite()
exibir_saldo()
verificar_conta()

conta_2, limite = debitar(70, conta_2, limite)
exibir_saldo()