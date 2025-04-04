# DESAFIOS PARA SOMA

# 1. Adicione uma nova pontução a um total de pontos existente em um jogo fictício
pontos = 0
pontos_ganhos = 1

total_de_pontos = pontos + pontos_ganhos
print(f'você ganhou {pontos_ganhos} ponto! Total: {total_de_pontos}')


# 2.Para cada dia da semana defina a quantidade de horas trabalhadas e some o total
dias_da_semana = ['Segunda-feira', 'terca-feira', 'quarta-feira', 'quinta-feira', 'sexta-feira', 'sabado']
total_de_horas = 0

for dia in dias_da_semana:
    horas_trabalhadas = input(f'Insira as horas trabalhadas na(o) {dia} ')
    
    if horas_trabalhadas is '':
        horas_trabalhadas = '0'

    inteiro = int(horas_trabalhadas)
    total_de_horas = total_de_horas + inteiro 

print(f'Total de {total_de_horas} horas trabalhadas na semana.')

# 3. Imagine que na sua casa 3 pessoas ganham salários diferentes, some eles para saber o ganho total
salario_pessao_1 = 3500.90
salario_pessao_2 = 5050.33
salario_pessao_3 = 2033.25

total_salarios = salario_pessao_1 + salario_pessao_2 + salario_pessao_3
print('Total de dinhero ganho: ', total_salarios)