'''
1. Vamos fornecer uma estrutura inicial em JSON
com o saldo, o limite diário para transferências (que
será de R$ 10.000), teremos um controle para saber
o quanto já foi transferido no dia, um histórico de
transações por Pix e também um total já transferido
por chave Pix.

2. Você deverá implementar 2 operações Pix, uma
para enviar o Pix e outra para cancelar (ou seja, fazer
o reembolso). Para isso você deve utilizar a
**chavePix**, o **valor** a ser transferido e uma
**mensagem** de referência. Para cancelar, basta utilizar
o **indice** da transação para facilitar.
'''
# VOU TER QUE CRIAR CLASSES!!!
conta_1 = {
    "nome": "conta 1",
    "saldo": 50000,
    "limiteDiario": 10000,
    "totalTransferidoHoje": 0,
    "historicoTransacoes": [],
    "totalPorChave": {
        "chavePix": 0,
        "totalTransferido": 0
    } # Armazena total transferido por chave Pix
}


# operações pix
# ENVIAR PIX
def transferir(origem: dict, destino: dict, chavePix = '', valor = 0, mensagem = ''):
    # atualizar VALORES
    origem["saldo"] =                   origem['saldo'] - valor
    origem["limiteDiario"] =            origem["limiteDiario"] - valor
    origem["totalTransferidoHoje"] =    origem["totalTransferidoHoje"] + valor

    # salvar historico
    transacao = {
        "valorTransferido": valor,
        "origem": origem["nome"],
        "destino": destino, # ["nome"]
        "chavePix": chavePix,
        "mensagem": mensagem
        # data
    }
    origem["historicoTransacoes"].append(transacao)

    # armazenar o total trasnferido por chave pix
    totalPorChave = {

    }



# CANCELAR PIX
def cancelar():
    return

def consulta(conta: dict):
    print("=== CONSULTAR DADOS ===")
    print(f'saldo:                      R${conta["saldo"]}')
    print(f'Limite diário:              R${conta["limiteDiario"]}')
    print(f'Total transferido - hoje:   R${conta["totalTransferidoHoje"]}')
    print(f'Histórico de Transações:    {conta["historicoTransacoes"]}')
    print(f'Total por chave:            {conta["totalPorChave"]}')

transferir(conta_1, 'conta_2', 'zezinhoDaComeia@email.com', 500, 'mensagem de teste')

consulta(conta_1)