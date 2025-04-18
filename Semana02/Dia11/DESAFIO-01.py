'''
DESAFIO 01:
Controle de Navegação
em Navegadores Web

O desafio é simular a navegação entre páginas em
um navegador e implementar os botões "voltar" e
"avançar" usando pilhas e as regras dessa
funcionalidade tão comum em nosso dia a dia.

Dicas:

1. Crie 3 funções, uma que controle o voltar, uma para
o avançar e outra para navegar para um endereço.

2. Controle a partir de 2 pilhas e uma variável que
armazena o endereço da página atual.

3. Nesse caso, se você achar necessário, pode
utilizar as funções de arrays: push e pop ;)
'''
paginaAtual = ''
paginaAnterior = []
proximaPagina = []
historico = []

def navegarPara(url: str):
    # RELEMBRANDO: No python é necessário que informe a função que, quando queremos lidar
    # com uma variável global, devemos informar da forma a seguir, senão a função retornará um erro:
    global paginaAtual
    
    print(f'Navegando para {url}')
    
    if paginaAtual == '':
        paginaAtual = url

        historico.append(paginaAtual)

    else:
        paginaAnterior.append(paginaAtual)
        paginaAtual = url

        historico.append(paginaAtual)

    return 
        

def voltar():

    global paginaAtual

    proximaPagina.append(paginaAtual)
    paginaAtual = paginaAnterior.pop()
    print(f'voltando para {paginaAtual}')


def avancar():
    
    global paginaAtual
    
    paginaAtual = proximaPagina.pop()
    print(f'Avançando para {paginaAtual}')


navegarPara('cnn.com')
navegarPara('google.com')
navegarPara('terra.com.br')

voltar()

avancar()

print(historico)