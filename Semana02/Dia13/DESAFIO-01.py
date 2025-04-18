'''
DESAFIO 01:
Controle de Tarefas Dinâmicas
com Prioridades
Neste desafio crie um controle que gerencia tarefas
com prioridade. O objetivo é simular um ambiente
onde tarefas urgentes podem surgir a qualquer
momento, exigindo reorganização rápida e eficiente
da fila de tarefas.

Esse desafio tem os seguintes objetivos:

1. Implementar um Deque para Tarefas: Que permita
inserções e remoções tanto no início quanto no final
da lista. Isso simulará a adição de tarefas com
diferentes prioridades.

2. Manipulação de Prioridades: Implementar 2
funções, que permitam aumentar e diminuir a
prioridade de uma tarefa específica dentro do deque.
Isso significa que você deve ser capaz de mover uma
tarefa para mais perto do início ou do final da fila,
dependendo da urgência.

3. Testar com Cenários Realistas: Você deve criar e
testar seu sistema com cenários que simulam a
realidade de um ambiente de trabalho, onde tarefas
com diferentes níveis de urgência podem ser
adicionadas a qualquer momento.
'''
tarefas = []

prioridades = [
    [0, "Emergência"],
    [1, "Urgência"],
    [2, "Rotina normal"]
]


def adicionarTarefa(tarefa, indicePrioridade: int):

    # Verifica se parametro prioridade é uma opção válida
    verificaSeInt = str(type(indicePrioridade))
    
    if verificaSeInt != "<class 'int'>":
        print('Isso não é um número inteiro')
        return
    
    
    # podemos usar match case que aprendemos na aula do dia 4
    match indicePrioridade:
        case 0:
            tarefas.insert(0, [tarefa, prioridades[indicePrioridade][1]])
        
        case 1:
            indice = 0

            for t in tarefas:  

                # verificar quais índices se encontra as tarefas de maior prioridade
                if "Emergência" in t:
                    indice+=1
            
            tarefas.insert(indice, [tarefa, prioridades[indicePrioridade][1]])

        case 2:
            tarefas.append([tarefa, prioridades[indicePrioridade][1]])

        case _:
            print('Prioridade inválida, por favor selecione números entre 0 e 2.')



def mudarPrioridade(indiceTarefa: int, indiceNovaPrioridade: int):
    
    # re-adicionando a tarefa com a nova prioridade
    adicionarTarefa(tarefas[indiceTarefa][0], indiceNovaPrioridade)

    # excluindo a tarefa com a antiga prioridade
    excluirTarefa(indiceTarefa)



def excluirTarefa(indiceTarefa):
    tarefaExcluida = tarefas.pop(indiceTarefa)
    return tarefaExcluida



def verTarefas():
    # numerar cada uma das tarefas e exibi-las
    print('\n--- Lista de Tarefas ---')
    enumerar = enumerate(tarefas)    
    for i in enumerar:
        print(f'{i[0]} - {i[1][0]}, {i[1][1]}')






adicionarTarefa('Verificar caixa de emails', 2)
adicionarTarefa('servidor com Error 503', 0)
# adicionarTarefa('servidor com Error 503', 0)
adicionarTarefa('servidor com Error 504', 0)
adicionarTarefa('Rede wifi com instabilidade', 1)

verTarefas()

print('\nA seguinte tarefa foi exlcuida:', excluirTarefa(1))

verTarefas()

mudarPrioridade(0,2)

verTarefas()
