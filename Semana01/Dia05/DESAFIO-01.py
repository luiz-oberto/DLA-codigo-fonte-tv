"""
DESAFIO 01:
Rendimento de aplicação financeira

Suponha que você investiu R$ 1.000 em uma aplicação
financeira que rende 12% ao ano. Usando um loop for,
podemos calcular como esse investimento cresce ao
longo do tempo, vamos supor nos próximos 10 anos.
Mostre o valor no console por ano.
"""
dinheiro = 1000.00
rendimento = 0.12
tempo_anos = 10
dinheiro_com_rendimentos = 0

for ano in range(1, tempo_anos+1):
    dinheiro_com_rendimentos = (dinheiro * rendimento) + dinheiro if dinheiro_com_rendimentos == 0 else (dinheiro_com_rendimentos * rendimento) + dinheiro_com_rendimentos

    print(f'Ano {ano}, Total: R${dinheiro_com_rendimentos:.2f}')
