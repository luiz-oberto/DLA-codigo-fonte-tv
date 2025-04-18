'''
# Desafios Desafiadores com Deque
- O que é Deque?
-> é uma fila de duas pontas
Em outras palavras, é uma Fila que permite a inserção e a remoção de elementos tanto no ínicio com no final

-> Um Deque é como se fosse a combinação de uma fila com uma pilha

exemplos:
- fila de atendimento em uma clínica para retirar sangue

# Operações básicas do Deque:
- InsertFront - adiciona um item na frente do Deque
- InsertLast - adiciona item na cauda do deque
- deleteFront - deleta um item na frente do Deque
- DeleteLast - Deleta um item na cauda do Deque
- front - retorna o item que tá na frente
- rear - retornar o item que tá na cauda
- isEmpty - Verifica se o array tá vazio
- getItens - retorna todos os itens do array ou uma cópia do array

'''
itens = [] # Deque

# Inserir no início
def inserirInicio(item):
    itens.insert(0, item)

# Inserir no fim
def inserirFim(item):
    itens.append(item)

# remover do Início
def removerIncio():
    return itens.pop(0)

# remover do fim
def removerFim():
    return itens.pop()

# obter o primeiro item
def primeiro():
    return itens[0]

# Obter o último elemento
def ultimo():
    return itens[-1]

# verificar se está vaxio
def estaVazio():
    return len(itens) == 0

# obter itens
def obterItens():
    return itens.copy()


print(estaVazio())

inserirInicio('Fulano')
inserirFim('maça')
inserirInicio('banana')

print(primeiro())
print(ultimo())

print(itens)

removerIncio()

itemCopy = obterItens()

removerFim()

print(itens)

print(estaVazio())

print(itemCopy)









# --- PARTE DO CÓDIGO QUE EU ESTAVA FAZERNDO PARA O DESAFIO ANTES DE PERCEBER QUE SERIA INÚTIL ---

    # print('\n-- Mudar prioridade de uma tarefa --')
   
    # # Ver tarefas da lista
    # verTarefas()
    
    # print()

    # # escolher uma tarefa da lista
    # escolhaTarefa = int(input('Número da tarefa que deseja mudar a prioridade: '))
    
    # # salvando a tarefa a ser altereda
    # tarefa = tarefas[escolhaTarefa]

    # print(f'\nVoce selecionou: \n')
    # print(f'-> {tarefas[escolhaTarefa][0]} - {tarefas[escolhaTarefa][1]}\n')
    
    # # Exibir opções para mudar a prioridade da tarefa
    # print('Selecione uma das opções ou não digite nada para cancelar\n', '1 - mudar para "Emergência"\n', '2 - mudar para "Urgência"\n', '3 - mudar para "Rotina normal"')
    # opcaoPrior = input(': ')

    # match opcaoPrior:
    #     case 1:
    #         if tarefa[1] != "Emergência":
    #             tarefa[1] = "Emergência"   
    #             print(tarefa)         