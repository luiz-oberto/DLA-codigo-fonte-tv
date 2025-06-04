conta_1 = {
    "nome": "conta 1",
    "saldo": 50000,
    "limiteDiario": 10000,
    "totalTransferidoHoje": 0,
    "historicoTransacoes": [],
    "totalPorChave": {}
}

conta_2 = {
    "nome": "conta 2",
    "saldo": 30000,
    "limiteDiario": 5000,
    "totalTransferidoHoje": 0,
    "historicoTransacoes": [], 
    "totalPorChave": {}
}


def transferir(origem: dict, destino: dict, chavePix='', valor=0, mensagem=''):
    if origem["totalTransferidoHoje"] + valor > origem["limiteDiario"]:
        return print('Limite de pix atingido, transferência cancelada.')

    if valor < 0:
        return print("Valor inserido inválido")

    origem["saldo"] -= valor
    origem["totalTransferidoHoje"] += valor
    destino["saldo"] += valor

    transacao = {
        "tipo": "TRANSFERENCIA",
        "valorTransferido": valor,
        "origem": origem["nome"],
        "destino": destino["nome"],
        "chavePix": chavePix,
        "mensagem": mensagem
    }
    transacao_recebida = transacao.copy()
    transacao_recebida["tipo"] = "RECEBIMENTO"
    origem["historicoTransacoes"].append(transacao)
    destino["historicoTransacoes"].append(transacao_recebida)

    if chavePix in origem["totalPorChave"]:
        origem["totalPorChave"][chavePix] += valor
    else:
        origem["totalPorChave"][chavePix] = valor


def aumentar_limite(conta):
    valor_total = 0
    for i in conta["historicoTransacoes"]:
        if i["tipo"] == "ESTORNO":
            valor_total -= i["valorEstornado"]
        else:
            valor_total += i.get("valorTransferido", 0)

    if valor_total > conta["limiteDiario"]:
        conta["limiteDiario"] = valor_total
        print(f'\n=== Novo limite liberado! === \nSeu novo limite é: R${valor_total}\n')


def cancelar(indice, conta_origem: dict, conta_destino: dict):
    try:
        print("\n==== CANCELANDO TRANSFERÊNCIA ====\n")
        historico = conta_origem["historicoTransacoes"]
        transacao = historico[indice]

        log = {
            "tipo": "ESTORNO",
            "valorEstornado": transacao["valorTransferido"],
            "origem": transacao["origem"],
            "destino": transacao["destino"],
            "chavePix": transacao["chavePix"],
            "mensagem": transacao["mensagem"]
        }

        conta_origem["saldo"] += transacao["valorTransferido"]
        conta_origem["historicoTransacoes"].append(log)
        conta_destino["saldo"] -= transacao["valorTransferido"]
        conta_destino["historicoTransacoes"].append(log)
    except Exception as e:
        print("Erro ao cancelar transferência:", e)


def consulta(conta: dict):
    try:
        print("===== CONSULTAR DADOS =====")
        print(f'CONTA:                      {conta.get("nome")}')
        print(f'saldo:                      R${conta["saldo"]}')
        print(f'Limite diário:              R${conta["limiteDiario"]}')
        print(f'Total transferido - hoje:   R${conta["totalTransferidoHoje"]}')

        print(f'\n=== Histórico de Transações ===')
        for i, index in enumerate(conta["historicoTransacoes"], 1):
            print(f'{"->" if index["tipo"] == "ESTORNO" else "-"} Registro: {i}')
            print(f'TIPO:                       {index["tipo"]}')
            print(f'ORIGEM:                     {index["origem"]}')
            print(f'DESTINO:                    {index["destino"]}')
            print(f'CHAVE PIX:                  {index["chavePix"]}')
            print(f'{"VALOR ESTORNADO" if index["tipo"] == "ESTORNO" else "VALOR TRANSFERIDO"}: R$ {index.get("valorEstornado", index.get("valorTransferido"))}')
            print(f'MENSAGEM:                   {index["mensagem"]}\n')

        print(f'=== TOTAL POR CHAVE ===')
        for chave, total in conta["totalPorChave"].items():
            print(f'CHAVE PIX:                  {chave}')
            print(f'VALOR TOTAL TRANSFERIDO:    R$ {total}\n')
    except Exception as e:
        print("Erro ao consultar conta:", e)


# Testes
transferir(conta_1, conta_2, 'zezinhoDaComeia@email.com', 500, 'mensagem de teste')
transferir(conta_1, conta_2, '123.456.789-00', 1000, 'mensagem de teste')
transferir(conta_1, conta_2, '123.456.789-00', 5500, 'mensagem de teste')
transferir(conta_1, conta_2, '(71)91234-5678)', 1, 'mensagem de teste')

cancelar(0, conta_1, conta_2)

consulta(conta_1)
consulta(conta_2)

aumentar_limite(conta_2)
transferir(conta_1, conta_2, 'zezinhoDaComeia@email.com', 200, 'mensagem de teste')
aumentar_limite(conta_2)
