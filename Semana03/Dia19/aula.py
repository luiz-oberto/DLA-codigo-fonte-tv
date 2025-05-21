'''
# Recursão
- Função que chama a si mesmo até chegar num caso base

-Recursão é uma técnica de programação onde uma função chama a si mesma para resolver um problema.

A ideia é dividir um problema maior em subproblemas menores do mesmo tipo. Cada chamada recursiva trabalha com uma versão mais simples do problema, até que se atinja um caso base (ou caso de parada), onde a função não se chama mais e a execução começa a voltar (o famoso "desempilhamento").

A recursão pode ser feita de forma direta:
'''
def fatorial(n):
    if n == 0: # caso base
        return 1
    
    return n * fatorial(n-1) # chamada recursiva

print(fatorial(5)) # 120

'''
E pode ser feita de forma indireta
'''
def joao(numero):
    if numero <= 0:
        print('Fim do atendimento.')
        return

    if numero % 2 == 0:
        print('João atendeu o número', numero)
        maria(numero-1)
        return

    maria(numero)

def maria(numero):
    if numero <= 0:
        print('Fim do atendimento.')
        return

    if numero % 2 != 0:
        print('Maria atendeu o número', numero)
        joao(numero-1)
        return
    
    joao(numero)

joao(5)

