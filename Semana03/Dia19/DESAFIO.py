'''
DESAFIO 01:
Desafio parcelas fatura
cartão de crédito:

Imagine que você foi contratado por uma fintech para
criar um sistema que simula o cálculo do valor total
de uma fatura de cartão de crédito. A diferença é que
nesse sistema, algumas compras podem ter
parcelas, e cada parcela pode conter outras
sub-parcelas (como se fossem "compras dentro de
compras").

Você precisa usar recursão para encontrar o valor
total de uma fatura, considerando todas as compras
diretas e as sub-parcelas que elas possam ter.

Para não sair do zero, vamos fornecer essa estrutura
em JSON já com algumas compras e parcelas para
você poder percorrer. Você pode baixar o JSON, aqui

const fatura = [
  {
    descricao: "Celular",
    valor: 1200.00,
    parcelas: [
      { descricao: "Seguro", valor: 100.00 },
      { descricao: "Película", valor: 30.00 }
    ]
  },
  {
    descricao: "Notebook",
    valor: 3000.00,
    parcelas: [
      {
        descricao: "Assistência técnica",
        valor: 200.00,
        parcelas: [
          { descricao: "Visita técnica", valor: 50.00 }
        ]
      }
    ]
  },
  {
    descricao: "Livro",
    valor: 89.90
  }
];


Esse desafio mostra o poder da recursão em resolver
problemas com estrutura em camadas, como
faturas, hierarquias ou qualquer item que se repete
dentro de si mesmo.

Esse mesmo tipo de estrutura pode muito bem estar
presente em apps como Nubank, PicPay, Mercado
Pago e outros bancos digitais, onde é preciso somar
valores de forma dinâmica.
'''
fatura = [
  {
    "descricao": "Celular",
    "valor": 1200.00,
    "parcelas": [
      { "descricao": "Seguro", "valor": 100.00 },
      { "descricao": "Película", "valor": 30.00 }
    ]
  },
  {
    "descricao": "Notebook",
    "valor": 3000.00,
    "parcelas": [
      {
        "descricao": "Assistência técnica",
        "valor": 200.00,
        "parcelas": [
          { "descricao": "Visita técnica", "valor": 50.00 }
        ]
      }
    ]
  },
  {
    "descricao": "Livro",
    "valor": 89.90
  }
]


# Você precisa usar recursão para encontrar o valor total de uma fatura, considerando todas as compras diretas e as sub-parcelas que elas possam ter.
def valor_total_fatura(fatura: list):
    valor_total = 0
    for conta in fatura:
        print(conta["valor"])
        valor_total += conta["valor"]
        
        if conta.get("parcelas"):
            parcelas = valor_total_fatura(conta.get("parcelas"))
            valor_total+=parcelas
        
    return valor_total

# print('Valor total da Fatura é:')
valor = valor_total_fatura(fatura) # deve retornar: 4.669,90 (não esquecer de formatar o texto de saída)
print(f'Valor total da fatura é : R$ {valor:.2f}')