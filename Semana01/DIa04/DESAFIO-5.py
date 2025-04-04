"""
DESAFIO 05: Cancela de estacionamento

Para testar sua habilidades, vamos direto para um desafio. Imagine que você está programando o
sistema de controle de uma cancela de estacionamento. Este sistema tem três possíveis
estados: "Aberta", "Fechada" e "Manutenção".
Baseado no valor da variável estado, crie um código usando switch que imprima uma mensagem
adequada para o motorista.
"""
# ********************** NÃO EXISTE SWITCH CASE EM PYTHON ********************************

estado = "Fechada"
if estado == "Aberta":
    print("Abrindo cancela")
elif estado == "Fechada":
    print("Cancela Fechada")
else:
    print("Cancela em manutenção.")