"""
DESAFIO 03: Aplicação Financeira

Para o desafio 3, quero que você volte ao dia 5 no
desafio 1 sobre rendimento de aplicação financeira e
crie uma função que fará todo o cálculo, conforme
detalhamos no desafio.

Você tem um valor inicial de uma aplicação
financeira que rende um percentual ao ano. Calcule
como esse investimento cresce ao longo do tempo
ao ano.
"""
def verRendimento(valor_incial: float, taxa_aa: float, anos: int, titulo: str):
    print(f"Previsão do investimento: {titulo}")
    for ano in range(1, anos+1):
        valor_incial += taxa_aa * valor_incial
        print(f'Ano {ano}, Total: R${valor_incial:.2f}')

    return


verRendimento(1000, 0.12, 10, 'Reserva de Emergência')
