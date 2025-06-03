'''
4. Existirá um total armazenado de todos os pix
realizados para uma mesma chave **totalPorChave**.
Quando esse total, independente do tempo,
ultrapassar o limite diário de pix, essa chave estará
liberada para receber transferências acima do limite
diário, tendo como novo limite para transações o
total já transferido para essa chave.

    Então se chave, por exemplo, receber mais de R$
10.000 no total, ela "desbloqueia" esse limite para
transferências futuras.
'''
# utilizar um histórico dentro das contas não deve ser uma prática muito boa...
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

conta_2 = {
    "nome": "conta 2",
    "saldo": 30000,
    "limiteDiario": 10000, # 8000 se esta conta receber mais de 8 mil em pix, o seu limite será atualizado para transnferir 8k + valor recebido
    "totalTransferidoHoje": 0,
    "historicoTransacoes": [], 
    "totalPorChave": {}
}

# ENVIAR PIX
def transferir(origem: dict, destino: dict, chavePix = '', valor = 0, mensagem = ''):

    if origem["totalTransferidoHoje"] + valor > origem["limiteDiario"]:
        return print('Limite de pix atingido, transferência cancelada.')
    
    if valor < 0:
        return print("Valor inserido inválido")

    # atualizar VALORES DA ORIGEM
    origem["saldo"] =                   origem['saldo'] - valor
    origem["totalTransferidoHoje"] =    origem["totalTransferidoHoje"] + valor

    # atualizar VALORES DO DESTINO
    destino["saldo"] =                  destino['saldo'] + valor

    # salvar historico
    transacao = {
        "tipo": "TRANSFERENCIA",
        "valorTransferido": valor,
        "origem": origem["nome"],
        "destino": destino["nome"], # ["nome"]
        "chavePix": chavePix,
        "mensagem": mensagem
    }
    transacao_recebida = transacao.copy()
    transacao_recebida["tipo"] = "RECEBIMENTO"
    origem["historicoTransacoes"].append(transacao)
    destino["historicoTransacoes"].append(transacao_recebida)

    # armazenar o total trasnferido por chave pix
    if chavePix in origem["totalPorChave"]:
        origem["totalPorChave"][chavePix] += valor
    else:
        origem["totalPorChave"].update(dict.fromkeys([chavePix], valor))



# CANCELAR PIX
def cancelar(indice, conta: dict):
    try:
        print("\n==== CANCELANDO TRANSFERÊNCIA ====\n")
        # ir no histórico de transações e reverter aquele pix feito
        historico = conta["historicoTransacoes"]
        log = {
            "tipo": "ESTORNO",
            "valorEstornado":   historico[indice]["valorTransferido"],
            "origem":           historico[indice]["origem"],
            "destino":          historico[indice]["destino"],
            "chavePix":         historico[indice]["chavePix"],
            "mensagem":         historico[indice]['mensagem']

        }
        # somar o valor de volta ao saldo
        conta["saldo"] += historico[indice]["valorTransferido"]
        conta["historicoTransacoes"].append(log) # adiciona ação de cancelar ao histórico
        # FAZER O ESTORNO DA CONTA DESTINO
    except:
        return print("Conta ou ídice refereniado inválidos.")


def consulta(conta: dict):
    try:
        print("===== CONSULTAR DADOS =====")
        print(f'CONTA:                      {conta.get('nome')}')
        print(f'saldo:                      R${conta["saldo"]}') # substituir por .get()
        print(f'Limite diário:              R${conta["limiteDiario"]}')
        print(f'Total transferido - hoje:   R${conta["totalTransferidoHoje"]}')

        print(f'\n=== Histórico de Transações ===') # fazer uma condicional para val ESTORNADOS
        for i, index in enumerate(conta["historicoTransacoes"], 1):
            if index["tipo"] == "ESTORNO":
                print('-> Registro:', i)
                print(f'TIPO:                       {index["tipo"]}')
                print(f'ORIGEM:                     {index["origem"]}')
                print(f'DESTINO:                    {index["destino"]}')
                print(f'CHAVE PIX:                  {index["chavePix"]}')
                print(f'VALOR ESTORNADO:            R$ {index["valorEstornado"]}')
                print(f'MENSAGEM:                   {index["mensagem"]}\n')
            else:
                print('- Registro:', i)
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
    except:
        return print("Conta inválida")      



transferir(conta_1, conta_2, 'zezinhoDaComeia@email.com', 500, 'mensagem de teste')
transferir(conta_1, conta_2, '123.456.789-00', 1000, 'mensagem de teste')
transferir(conta_1, conta_2, '123.456.789-00', 8500, 'mensagem de teste')
transferir(conta_1, conta_2, '(71)91234-5678)', 1, 'mensagem de teste')
# consulta(conta_1)

cancelar(0, conta_1)

consulta(conta_1)
consulta(conta_2)
