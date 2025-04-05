"""
DESAFIO 05: Cancela de estacionamento

Para testar sua habilidades, vamos direto para um desafio. Imagine que você está programando o
sistema de controle de uma cancela de estacionamento. Este sistema tem três possíveis
estados: "Aberta", "Fechada" e "Manutenção".
Baseado no valor da variável estado, crie um código usando switch que imprima uma mensagem
adequada para o motorista.
"""
estado = "Fechada"

match estado:
    case "Aberta":
        print("A cancela está aberta. Por favor, entre.")
    case "Fechada":
        print("A cancela está fechada, por favor, aguarde a liberação.")
    case "Manutenção":
        print("A cancela está em manutenção. Por favor, use a outra entrada.")
    case _:
        print("Estado desconhecido.")


if estado == "Aberta":
    print("Abrindo cancela")
elif estado == "Fechada":
    print("Cancela Fechada")
else:
    print("Cancela em manutenção.")