'''
DESAFIO 01:
Braço Mecânico para Empilhar Produtos

Vamos imaginar que você foi chamado para
programar um braço mecânico em uma indústria. Na
linha de produção, um braço mecânico automatizado
é encarregado de pegar produtos individuais que
chegam através de uma esteira e empilhá-los em
caixas para envio. Cada caixa pode conter até no
máximo 10 produtos. Uma vez que a caixa está
cheia, ela é enviada para ser selada e despachada.

Se ainda ficou com dúvida, vamos te ajudar citando
algumas das operações: Empilhar, Verificar a
Capacidade e criar uma Nova Pilha.

Dica: Pra simular a esteira faça um looping com a
chegada de mais de 20 produtos

Lembre-se de não complicar a solução. A simplicidade,
na grande parte das vezes, é o caminho para resolver
os desafios . ;)
'''

qtd_produtos = 20
esteira = []

# COLOCANDO PORDUTOS NA ESTEIRA
for i in range(qtd_produtos):
    esteira.append(i)
print(f'Produtos na esteira: \n{esteira}\n')


# Verificar se a caixa está cheia
def verificarQuantidade(pilha):
    if len(pilha) == 10:
        return True


# iniciar um novo empilhamento
def iniciarPilha(esteira):
    pilha = []
    i = 0

    while esteira:

        pilha.append(esteira.pop(i))

        verificarQtd = verificarQuantidade(pilha)

        print(f'pilha: {pilha}')
        print(f'Esteira: {esteira}\n')

        if verificarQtd == True:
            print('Enviando caixa para ser despachada.')
            print()
            pilha = []

            print('Iniciando nova pilha...\n') if esteira else print('Sem produtos para empilhar.')
        


iniciarPilha(esteira)
