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
    
    def insertFirst(self, valor):
        
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
        # print(novo_no)


######### IMPLEMENTAR AS PRÓXIMAS FUNÇÕES ##########

    # Inclui um nó no final da lista
    def insertLast(self):
        ...

    
    # que inclui um nó em uma determinada posição 
    def insertAt(self):
        ...


    # que exclui um nó em uma determinada posição
    def deleteAt(self):
        ...

    
    # que encontra um nó de acordo com a posição
    def searchAt(self):
        ...


    # que pecorre todos os nós
    def traversal(self):
        atual = self.head

        # declarar uma lista para retornar ela ao final com todos os nós inclusos nela
        listaNo = []

        while atual is not None:
            listaNo.append(atual) # salva o nó na lista
            atual = atual.next

        # retornar um lista enumerada

        return listaNo

    
    # que retorna a posição de acordo com o elemento do nó
    def indexOf(self, data):
        listaValores = self.traversal()

        i = 0

        while i < len(listaValores):
        
            if data == listaValores[i].data:
                return i
            else:
                i+=1
        
        return print('ERROR: Valor não encontrado entre os nós')




listaEncadeada = ListaEncadeada()

listaEncadeada.insertFirst('Vagão 1')
listaEncadeada.insertFirst('Vagão 2')
listaEncadeada.insertFirst('Vagão 3')
listaEncadeada.insertFirst('Vagão 3')

listaEncadeada.traversal()

indice = listaEncadeada.indexOf('Vagão 3')
print(indice)
