"""
DESAFIO 06: Sistema de PDV (ponto de venda)

Suponha que você está programando um sistema PDV e precisa calcular o desconto aplicado a um
produto.

O desconto é dado com base no tipo do produto:
"Alimentos" têm um desconto de 5%, 
"Eletrônicos" têm um desconto de 10%, 
"Roupas" têm um desconto de 20% e 
"Livros" têm um desconto de 50%.
Se o tipo do produto não estiver na lista, não há desconto. Crie um código usando switch que
calcule e imprima o valor final do produto após a aplicação do desconto, com base no tipo do produto.
"""
# produtos_com_desconto = ["Alimentos", "Eletrônicos", "Roupas", "Livros"]

tipo_do_produto = "Livros"
preco = 100.00
desconto = 0

# Com match case (cujo a existêcia eu não sabia até 10 minutos atrás quando fiz esse código)
match tipo_do_produto:
    case "Alimentos":
        desconto = 0.05
    case "Eletrônicos":
        desconto = 0.10
    case "Roupas":
        desconto = 0.20
    case "Livros":
        desconto = 0.50
    case _:
        desconto = 0

valor_final = preco * (1 - desconto)
print(f'O valor final do produto é R${valor_final:.2f}')

# Com if-elif-else (O clássico)
# if tipo_do_produto not in produtos_com_desconto:
#     print("Produto sem desconto")
# elif tipo_do_produto == "Alimentos":
#     print("Desconto de 5%")
# elif tipo_do_produto == "Eletrônicos":
#     print("Desconto de 10%")
# elif tipo_do_produto == "Roupas":
#     print("Desconto de 20%")
# elif tipo_do_produto == "Livros":
#     print("Desconto de 50%")
# else:
#     print("Produto com desconto")
