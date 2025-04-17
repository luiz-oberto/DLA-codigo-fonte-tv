saldoContas = [1000, 10000, 500, 30, 78.10, 65, 9.99]

def calcularSaldoTotal(contas):
    total = 0

    for i in contas:
        total += i
    
    return total


saldoTotal = calcularSaldoTotal(saldoContas)
print(saldoTotal)