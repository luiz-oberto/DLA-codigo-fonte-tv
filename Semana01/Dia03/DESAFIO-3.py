"""
DESAFIO 3: Cálculo IMC
- Calcule o IMC de uma pessoa (que é pese divido pela altura ao quadrado). Se o resultado ficar menor
que 18,5, mostre que está abaixo do peso; se for maior ou igual a 18,5 e menor que 24,9, mostre que está
com o peso normal; se for maior ou igual a 24,9 e menor que 29.9, mostre que esrá com sobrepeso, senão mostre que é obesidade.
"""
peso = 60
altura = 1.73

imc = peso/(altura**2)

if imc < 18.5:
    print('Abaixo do peso')
elif imc >= 18.5 and imc <= 24.9:
    print('Peso normal')
elif imc >= 24.9 and imc <= 29.9:
    print('Sobrepeso')
else:
    print('Conheço 9 caras gordos e só você é 7')