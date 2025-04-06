"""
DESAFIO 01: Calcular IMC

Crie uma função que utiliza o peso e a altura como
parâmetros para calcular o IMC de uma pessoa. Só
lembrando que o IMC é o peso divido pela altura ao
quadro.
"""
def calcularimc(peso, altura):
    imc = peso/(altura**2)

    if imc < 18.5:
        print('Abaixo do peso')
    elif imc <= 24.9:
        print('Peso normal')
    elif imc <= 29.9:
        print('Sobrepeso')
    else:
        print('Conheço 9 caras gordos e só você é 7')

    return 


calcularimc(72, 1.72)
