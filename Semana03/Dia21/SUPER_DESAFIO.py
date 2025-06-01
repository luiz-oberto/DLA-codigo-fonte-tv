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
        # "chave": valor total de transferências
    } # Armazena total transferido por chave Pix
}

# operações pix
# ENVIAR PIX
def transferir(origem: dict, destino: dict, chavePix = '', valor = 0, mensagem = ''):
    # FAZER VERIFICAÇÃO DO LIMITE DIÁRIO
    # ...

    # atualizar VALORES
    origem["saldo"] =                   origem['saldo'] - valor
    origem["limiteDiario"] =            origem["limiteDiario"] - valor
    origem["totalTransferidoHoje"] =    origem["totalTransferidoHoje"] + valor

    # salvar historico
    transacao = {
        "tipo": "TRANSFERENCIA", # TRANSFERENCIA
        "valorTransferido": valor,
        "origem": origem["nome"],
        "destino": destino, # ["nome"]
        "chavePix": chavePix,
        "mensagem": mensagem
        # data
    }
    origem["historicoTransacoes"].append(transacao)

    # armazenar o total trasnferido por chave pix
    conta_1["totalPorChave"].update(dict.fromkeys([chavePix], valor))



# CANCELAR PIX
def cancelar(indice, conta: dict):
    # ir no histórico de transações e reverter aquele pix feito
    # somar o valor de volta ao saldo
    # somar o valor de volta ao limite diário
    historico = conta["historicoTransacoes"]
    print(historico[indice])
    transacao_a_cancelar = historico[indice]
    log = {
        "tipo": "ESTORNO",
        "valorEstornado": transacao_a_cancelar["valorTransferido"],
        "origem": None,
        "destino": None,
        "chavePix": None

    }
    conta["saldo"] += transacao_a_cancelar["valorTransferido"]
    conta["limiteDiario"] += transacao_a_cancelar["valorTransferido"]
    conta["historicoTransacoes"].append(log)

    # conta["tipo"] = "TRANSFERENCIA CANCELADA"

    return


def consulta(conta: dict):
    print("=== CONSULTAR DADOS ===")
    print(f'saldo:                      R${conta["saldo"]}') # substituir por .get()
    print(f'Limite diário:              R${conta["limiteDiario"]}')
    print(f'Total transferido - hoje:   R${conta["totalTransferidoHoje"]}')

    print(f'\n=== Histórico de Transações ===') # fazer uma condicional para val ESTORNADOS
    for i, index in enumerate(conta["historicoTransacoes"], 1):
        print('- Transação:', i)
        print(f'TIPO:                       {index["tipo"]}')
        print(f'ORIGEM:                     {index["origem"]}')
        print(f'DESTINO:                    {index["destino"]}')
        print(f'CHAVE PIX:                  {index["chavePix"]}')
        print(f'VALOR TRANSFERIDO:          R$ {index["valorTransferido"]}')
        print(f'MENSAGEM:                   {index["mensagem"]}\n')

    print(f'=== TOTAL POR CHAVE ===')
    total_por_chave = conta["totalPorChave"].items()
    for chave in total_por_chave:
        print(f'CHAVE PIX:                  {chave[0]}')
        print(f'VALOR TOTAL TRANSFERIDO:    R$ {chave[1]}\n')
        



transferir(conta_1, 'conta_2', 'zezinhoDaComeia@email.com', 500, 'mensagem de teste')
transferir(conta_1, 'conta_2', '123.456.789-00', 1100, 'mensagem de teste')
consulta(conta_1)

cancelar(0, conta_1)

consulta(conta_1)
