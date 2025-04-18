'''
DESAFIO 02:
Fila de atendimento em
um Drive Through

O desafio é você criar uma fila de atendimento de
clientes em uma cafeteria Drive Through. Todo
atendimento é realizado a partir de carros que vão
entrando no estacionamento da cafeteria e
recebendo os pedidos a partir de um totem
eletrônico.

Controle os clientes a partir de uma fila de carros
utilizando o princípio FIFO, que é essencial para
manter a ordem e a eficiência no serviço. Para
simplificar, o cliente pode pedir apenas um produto.
'''
filaClientes = []
pedidoDoCliente = []

def fazerPedido(pedido: str = None):
    
    if pedido == None:
        print('Por favor, faça um pedido.')
        return
    
    pedidoDoCliente.append(pedido)
    filaClientes.append(len(filaClientes) + 1)


def entregarPedido():

    if filaClientes == [] or pedidoDoCliente == []:
        print('Nenhum pedido a ser atendido ou entregue')
        return
    
    pedido = pedidoDoCliente.pop(0)
    cliente = filaClientes.pop(0)
    print(f'Entregando {pedido} ao cliente {cliente}.')



fazerPedido('Cafe latte')
fazerPedido('Capuccino')
fazerPedido('Iced coffe')

entregarPedido()

print(filaClientes)
print(pedidoDoCliente)

entregarPedido()

print(filaClientes)
print(pedidoDoCliente)

entregarPedido()
entregarPedido()
fazerPedido()

'''
"Fazer o seu melhor trabalho no primeiro rascunho é uma maneira infalível de não fazer seu melhor trabalho" - Kent Beck
'''