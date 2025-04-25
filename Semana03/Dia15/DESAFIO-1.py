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
        self.valor = valor
        self.proximo = None
    
class ListaEncadeada:
    def __init__(self):
        self.primeiro = None
    
    def adicionar(self, valor):
        
        novo_no = CriarNo(valor)
        
        if self.primeiro is None:
            self.primeiro = novo_no
        else:
            atual = self.primeiro

            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo_no
        # print(novo_no)

    def imprimir(self):
        atual = self.primeiro
        while atual is not None:
            print(atual.valor)
            atual = atual.proximo


listaEncadeada = ListaEncadeada()

listaEncadeada.adicionar('Vagão 1')
listaEncadeada.adicionar('Vagão 2')
listaEncadeada.adicionar('Vagão 3')

listaEncadeada.imprimir()

