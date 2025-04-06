"""
DESAFIO 02: Dia da Semana por Extenso

Vamos agora transformar aquele código que criamos
no dia 4, sobre os dias de semana utilizando switch
em uma função chamada obterDiaDaSemana,
onde receberemos um número que representa o dia
da semana que vai de 1 a 7 e ele retornará esse dia
por extenso.

A ideia é que a lógica fique dentro de uma função.
Faça várias chamadas da função para ver o
resultado.
"""
def obterDiaSemana(dia: int):
    match dia:
        case 1:
            diaNome = "Domingo"
        case 2:
            diaNome = "Segunda-feira"
        case 3:
            diaNome = "terça-feira"
        case 4:
            diaNome = "Quarta-feira"
        case 5:
            diaNome = "Quinta-feira"
        case 6:
            diaNome = "Sexta-feira"
        case 7:
            diaNome = "Sábado"
        case _:
            ...
    return print(diaNome)


obterDiaSemana(1)
obterDiaSemana(2)
obterDiaSemana(3)
obterDiaSemana(4)
obterDiaSemana(5)
obterDiaSemana(6)
obterDiaSemana(7)
