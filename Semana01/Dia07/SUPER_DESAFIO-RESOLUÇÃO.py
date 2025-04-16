# Saldo das contas
saldoConta1 = 600
saldoConta2 = 400

# Limite inicial, juros e configurções de limite
limite = 0
jurosLimite = 0
percetualLimite = 0.10
saldoMinimoLimite = 1000

# Taxa de conversão do dólar -> Real
taxaConversaoDolar = 5.23

def saldoTotal():
    total = saldoConta1 + saldoConta2

    if total >= saldoMinimoLimite:
        limite = total * percetualLimite


def alertaSaldo():
    if saldoConta1 <= 0:

        print('Conta 1 está sem saldo ou utilizand o limite.')
    
    elif saldoConta2 <= 0:
        
        print('Conta 2 ésta sem saldo ou utilizando o liimite.')


def depositar(conta, valor):
    if conta == 1:
        if saldoConta1 < 0:
            jurosLimite += valor * 0.15
            valor *= 0.85
        saldoConta1 += valor
    elif conta == 2:
        if saldoConta2 < 0:
            jurosLimite += valor * 0.15
            valor *= 0.85
        saldoConta2 += valor 


def debitar(conta, valor):
    if conta == 1 and valor <= (saldoConta1 + limite):
        saldoConta1 -= valor
    elif conta == 2 and valor <= (saldoConta2 + limite):
        saldoConta2 -= valor
    else:
        print(f'saldo insuficiene para débito na conta {conta}')


def trasnferir(valor, contaOrigem, contaDestino):
    if contaOrigem == 1 and valor <= saldoConta1:
        debitar(1, valor)
        depositar(contaDestino, valor)
    elif contaOrigem == 2 and valor <= saldoConta2:
        debitar(2, valor)
        depositar(contaDestino, valor)
    else:
        print(f'Saldo insuficiente para transferência na conta {contaOrigem}')


def converterSaldoParaDolar(conta):
    if conta == 1:
        return saldoConta1 / taxaConversaoDolar
    elif conta  == 2:
        return saldoConta2 / taxaConversaoDolar


def exibirLimite():
    return limite

def exibirJurosLimite():
    return jurosLimite