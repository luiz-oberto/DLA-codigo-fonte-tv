saldoContas = [
    ["Banco 1", "Agencia 1", "Conta 1", 1000],
    ["Banco 1","Agencia 1", "Conta 2", 10000],
    ["Banco 2","Agencia 1", "Conta 3", 500],
    ["Banco 2","Agencia 2", "Conta 4", 30],
    ["Banco 3","Agencia 1", "Conta 5", 78.10],
    ["Banco 4", "Agencia 1", "Conta 6", 65],
    ["Banco 4","Agencia 1", "Conta 7",9.99]
]

def calcularSaldoPorBanco(contas, nomeBanco):
    saldoTotal = 0

    for conta in contas:
        banco = conta[0]
        saldoConta = conta[3]

        if banco == nomeBanco:
            saldoTotal += saldoConta

    return saldoTotal


saldoBanco1 = calcularSaldoPorBanco(saldoContas, "Banco 1")
print(f'Saldo total do banco 1: R${saldoBanco1:.2f}')

saldoBanco2 = calcularSaldoPorBanco(saldoContas, "Banco 2")
print(f'Saldo total do banco 2: R${saldoBanco2:.2f}')