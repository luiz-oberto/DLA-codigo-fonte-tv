'''
DESAFIO 01:
Termine a implementação da
lista encadeada de um trem

O desafio é implementar as seguintes funções para
trabalhar com lista encadeada:

· insertLast que inclui um nó no final da lista;
· insertAt que inclui um nó em uma determinada
posição;
· deleteAt, que exclui um nó em uma determinada
posição;
· searchAt que encontra um nó de acordo com a
posição;
· o traversal que percorre todos os nós;
· e o indexOf que retorna a posição de acordo com
o elemento do nó.

O desafio é grande, mas lembre-se, por exemplo, que
ao implementar o insertAt a lógica é bem parecido
para o deleteAt e o searchAt.

Dica: Tente solucionar escrevendo em um papel e
depois passe a lógica para o código.
'''
class CriarNo:
    def __init__(self, valor):
        self.data = valor
        self.next = None
    
class ListaEncadeada:
    def __init__(self):
        self.head = None
    


######### IMPLEMENTAR AS PRÓXIMAS FUNÇÕES ##########

    # Inclui um nó no final da lista
    def insertFirst(self, data):
        
        novoNo = CriarNo(data)

        if self.head == None:
           self.head = novoNo
        else:
            atual = self.head
            novoNo.next = atual
            self.head = novoNo



    # Insere um valor no último nó
    def insertLast(self, valor):
        
        novoNo = CriarNo(valor)
        
        # Verifica se existe algum nó
        if self.head is None:
            
            # o primeiro nó recebe seu valor e a localização do próximo valor
            self.head = novoNo

        else:
            # Caso já exista um nó, vamos então verificar qual o nó que não possui a localização do próximo nó
            # OU SEJA, vamos atrá do úlitmo nó e acrescentar o valor do novo nó após ele
            atual = self.head

            while atual.next is not None:
                atual = atual.next
            atual.next = novoNo
    


    # inclui um nó em uma determinada posição
    # !!!!!!!!!! FALTA AJUSTAR PARA INSERIR UM NÓ AO INÍCIO E AO FINAL !!!!!!! 
    def insertAt(self, index: int, data):
        if isinstance(index, int):

            listaNo = self.traversal()

            if index <= len(listaNo)-1:
                # cria o novo nó a ser inserido
                novoNo = CriarNo(data)

                # salva o nó atual em que vamos inserir o novo nó
                noAtual = listaNo[index-1]
                # salva o next do nó atual
                nextDoNoAtual = noAtual.next

                # insere o novo nó na posição desejada
                noAtual.next = novoNo

                # salva no NEXT do novo nó, o próximo nó da sequencia
                novoNo.next = nextDoNoAtual

            else:
                return 'ERROR: Index out of range.'

        else:
            return 'ERROR: The index value must be an integer.'



    # exclui um nó em uma determinada posição
    def deleteAt(self):
        ...


    
    # encontra um nó de acordo com a posição
    def searchAt(self, index): # procure o valor da posição 3
        
        if isinstance(index, int):
            
            listaNo = self.traversal()
            
            # verificar se o índice se encontra no range da lista
            if index <= len(listaNo)-1:
                valor = listaNo[index]
                # retornar o valor de acordo com o ínidice procurado
                return valor.data
            else:
                return 'ERROR: Index out of range.'
        
        else:
            return 'ERROR: The index value must be an integer.'



    # pecorre todos os nós
    def traversal(self):
        atual = self.head

        # declarar uma lista para retornar ela ao final com todos os nós inclusos nela
        listaNo = []

        while atual is not None:
            listaNo.append(atual) # salva o nó na lista
            atual = atual.next

        return listaNo


    
    # retorna a posição de acordo com o elemento do nó
    def indexOf(self, data):
        listaValores = self.traversal()

        i = 0

        while i < len(listaValores):
        
            if data == listaValores[i].data:
                return i
            else:
                i+=1
        
        return print('ERROR: Valor não encontrado entre os nós')





################################## EXECUÇÃO DO CÓDIGO #########################################
listaEncadeada = ListaEncadeada()

# inserir no final
listaEncadeada.insertLast('Vagão 1')
listaEncadeada.insertLast('Vagão 2')
listaEncadeada.insertLast('Vagão 3')

# inserir no início
listaEncadeada.insertFirst('Vagão 4')
listaEncadeada.insertFirst('Vagão 5')
listaEncadeada.insertFirst('Vagão 6')

# inserir em
listaEncadeada.insertAt(6, 'Vagão N')

# printar lista encadeada
listaTraversal = listaEncadeada.traversal()
for i in listaTraversal:
    print(i.data)

# retornar o índice do valor procurado
print(listaEncadeada.indexOf('Vagão 3'))

# retornar o valor de acordo com o índice passado
print(listaEncadeada.searchAt(5))


############## RASCUNHO #############
# listaExemplo = [1,2, 3, 4]
# if 3 <= len(listaExemplo)-1:
#     print('True')
#     print(len(listaExemplo))
# else:
#     print('false')