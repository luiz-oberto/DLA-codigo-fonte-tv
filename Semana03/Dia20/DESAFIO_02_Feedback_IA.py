mensagens = [
    {
        "nome": "Ana",
        "mensagem": "Oi, você viu o relatório que mandei ontem?",
        "telefone": "11999999999",
        "data": "2025-04-01"
    },
    {
        "nome": "Bruno",
        "mensagem": "Vamos almoçar juntos amanha?",
        "telefone": "11988888888",
        "data": "2025-04-15"
    },
    {
        "nome": "Carlos",
        "mensagem": "Segue o RELATÓRIO atualizado.",
        "telefone": "11977777777",
        "data": "2025-04-20"
    },
    {
        "nome": "Daniela",
        "mensagem": "Relatório final enviado. Verifique!",
        "telefone": "11966666666",
        "data": "2025-04-20"
    },
    {
        "nome": "Vanessa Weber",
        "mensagem": "Está chegando ao fim do Desafio do Código Fonte TV",
        "telefone": "12977445588",
        "data": "2025-04-21"
    }
]

def buscar_palavra(lista, buscarValor=None, indice=0, encontrados=None):
    if buscarValor is None:
        print(-1)
        return

    if not isinstance(buscarValor, str):
        to_string = str(buscarValor)
    else:
        to_string = buscarValor

    if encontrados is None:
        encontrados = []

    if indice >= len(lista):
        for val in encontrados:
            print(val[0])
            print(f"Nome: {val[1]['nome']}")
            print(f"Mensagem: {val[1]['mensagem']}")
            print(f"Telefone: {val[1]['telefone']}")
            print(f"Data: {val[1]['data']}\n")
        return encontrados

    for valor in lista[indice].values():
        if to_string.lower() in str(valor).lower():
            encontrados.append((indice, lista[indice]))
            break

    return buscar_palavra(lista, buscarValor, indice + 1, encontrados)

# Exemplo de uso
buscar_palavra(mensagens, "1")
