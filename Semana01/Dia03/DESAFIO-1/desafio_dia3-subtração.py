# DESAFIOS PARA SUBTRAÇÃO

"""
1.Imagine que você tem algumas variáveis com compras no cartão de crédito, e uma com um valor a ser 
estornado de uma compra errada, calcule o total de fatura atualizado
"""
compra_01 = 100.50
compra_02 = 100.50
compra_a_ser_estornada = 50.50
fatura_total = compra_01 + compra_02 + compra_a_ser_estornada
print(f'Valor total da fatura: {fatura_total}')
print(f'Valor após estorno: {fatura_total - compra_a_ser_estornada}')


# 2.Calcule a sua idade a partir de duas variáveis contendo o ano de nascimento e o ano atual.
ano_nascimento = 1998
ano_atual = 2025
sua_idade = ano_atual - ano_nascimento
print(f'Sua idade atual é {sua_idade}')


"""
3. Imagine que em um jogo você tenha um total de moedas e para cada vez que você compra um artefato
você gasta um determindao número de moedas. Calcule a quantidade final de moedas.
"""
qtd_moedas = 2034
pocao_de_vida = 35

while True:
    escolha = input('Deseja comprar uma poção de vida? S/N ')
    if escolha == 'S':
        qtd_moedas = qtd_moedas - pocao_de_vida
        print(f'Compra realizada! moedas: {qtd_moedas}')
    else:
        print('Obrigado pela visita a nossa loja. Volte sempre!')
        break
