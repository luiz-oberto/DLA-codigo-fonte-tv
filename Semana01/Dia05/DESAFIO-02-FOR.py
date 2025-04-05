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
import os


# Contagem usando For
for segundos in range(10, 0, -1):
    (os.system("cls"), print(f"ATENÇÃO, {segundos} segundo(s) para o lançamento"), sleep(1)) if segundos <= 3 else (os.system("cls"), print(f"Contagem regressiva para o lançamento: {segundos}"), sleep(1))

print("\n### LAÇAMENTO AUTORIZADO. ### \n")
