'''
DESAFIO 01:
Fila de Atendimento em Call Center
Nesse desafio você deve criar um código que
gerencie uma fila para um call center.

Use funções simples para adicionar chamadas à fila
e para atender chamadas.

Lembre-se de que fizemos exatamente esse desafio
junto com você para te ensinar os conceitos.
'''
filaCallCenter = []

def adicionarChamada(chamada):
    filaCallCenter.append(chamada)


def atenderChamada():
    
    if filaCallCenter == []:
        print('Nenhuma chamada para ser atendida.')
        return

    filaCallCenter.pop(0)



adicionarChamada('chamada_1')
adicionarChamada('chamada_2')
adicionarChamada('chamada_3')

atenderChamada()
atenderChamada()
atenderChamada()
atenderChamada()

print(filaCallCenter)