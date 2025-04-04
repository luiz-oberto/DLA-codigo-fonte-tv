# DESAFIO 3: Transforme o código em uma condição ternária
""" *Código em JS*
let nota = 85;
let status;

if (nota >= 70) {
status = "aprovado";
} else {
status = "reprovado";

console.log(status);
}
"""
nota = 85
status = ""

status = "aprovado" if nota >= 70 else "reprovado"
print(status)