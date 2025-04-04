"""
DESAFIO 02:
Performance de aluno

Crie um algoritmo que precisa dizer para um aluno como foi sua performance em uma prova a partir da
nota que ele tirou.

As regras são:

1. Se a nota for menor que 5, então mostre que foi
"Insuficiente";
2. Se foi menor que 6, então mostre "Regular";
3. Se foi menor que 7.5, mostre "Bom"
4. Se foi menor que 9, "Muito bom";
5. E finalmente se for maior ou igual a 9, mostre
"Excelente".
"""
nota = 9

if nota < 5:
    print('Insuficiente')
elif nota < 6:
    print('Regular')
elif nota < 7.5:
    print('Bom')
elif nota < 9:
    print('Muito bom')
elif nota >= 9:
    print('Excelente')

idade = 15
situcao = "Menor diade" if idade < 18 else "maior idade"
print(situcao)
