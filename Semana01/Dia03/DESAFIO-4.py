"""
DESAFIO 4: Cálculo de distância de viagem e custo de combustível
- Suponha que você está planejando uma viajem de carro. Seu carro faz 12km por litro de gasolina, e você quer calular o número
de litros de combustível que você precisará para a viagem, bem como o custo total de combustível.
- Os dados qu você tem são:
    - Distância total da viagem em quilômetros
    - preço do litro de gasolina em reais

- O desafio é escrever um programa que recebe a distância da viajem e o preço da gasolina e calcula:
    a.Quantos litros de gasolina serão necessários para a viajem (considerando que o carro faz 12km por litro)
    b.Quanto vai custar para abastecer o carro para a viagem

"""
# Desafio A
distancia_total = input('Insira a distância da viajem: ')
preco_ltr_gasolina = input('Insira o valor da gasolina: ')

distancia_total_float = float(distancia_total) 
preco_ltr_gasolina_float = float(preco_ltr_gasolina)

qtd_litros_gas = distancia_total_float / 12

print(f'\nSerão necessários {qtd_litros_gas} litros para a viagem.')

# Desafio B
valor_da_viagem = qtd_litros_gas * preco_ltr_gasolina_float

print(f'Custo total: {valor_da_viagem}\n')