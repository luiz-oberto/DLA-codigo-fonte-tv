"""
DESAFIO 02:
Contagem regressiva para
lançamento de foguete

Imagine que você é um engenheiro da NASA e está
prestes a lançar um foguete. Você precisa fazer uma
contagem regressiva a partir de 10 até o lançamento.
No entanto, quando chegar nos últimos 3 segundos,
é importante dar um aviso, então inclua o texto
"Atenção!" junto à contagem. Quando a contagem
terminar mostre a mensagem: "Lançamento do
foguete!"
"""
from time import sleep


print("Contagem regressiva para o lançamento.")

# Contagem usando While
segundos = 10
while segundos != 0:
    if segundos <= 3:
        print(f"ATENÇÃO, {segundos} para o lançamento")
        segundos-=1
        sleep(1)

    else:
        print(segundos)
        segundos-=1
        sleep(1)

print("\n### Lançamento autorizado. ### \n")
