"""
DESAFIO 01:
Renovação da CNH

Vamos supor que estamos criando um sistema para controlar a renovação da carteira de motorista e
precisamos saber em quanto tempo a mesma irá vencer de acordo com a legislação.

1. De acordo com a lei, se você está tirando a carteira pela 1a vez (independentemente da sua idade), o
tempo de vencimento dela é de 1 ano;
2. Se você tem idade inferior a 50 anos o vencimento é de 10 anos;
3. Se for igual ou superior a 50 anos ou inferior a 70 anos o vencimento é de 5 anos;
4. Mas se for igual ou superior a 70 anos o vencimento será de 3 anos.

Você deve criar variáveis e estruturas condicionais
para controlar esse vencimento.
"""
idade = 71
via_1 = False

if via_1 == True:
    print('Sua carteira possui validade de 1 ano')
elif idade < 50:
    print('Sua carteira possui validade de 10 anos')
elif idade >= 50 and idade < 70:
    print('Sua carteira possui validade de 5 anos')
elif idade >= 70:
    print('Sua carteira possui validade de 3 anos')
