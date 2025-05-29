'''
DESAFIO 02:

Realizar uma busca linear, utilizando recursividade.
Porém ao invés de retornar o índice apenas do
primeiro item que foi encontrado, você deve
encontrar todos os índices que contém uma
determinada palavra.

No fim você deverá listar as mensagens encontradas
contendo: o nome, telefone e data de quem as
enviou.

Vamos simular aqui, uma lista de mensagens do
WhatsApp em um JSON, contendo: nome,
mensagem, numero telefone e data da mensagem.
Você pode baixar esse JSON aqui

const mensagens = [
{

nome: "Ana",
mensagem: "Oi, você viu o relatório que mandei ontem?",
telefone: "11999999999",
data: "2025-04-01"

},
{

nome: "Bruno",
mensagem: "Vamos almoçar juntos amanha?",
telefone: "11988888888",
data: "2025-04-15"

{

nome: "Carlos",
mensagem: "Segue o relatório atualizado.",
telefone: "11977777777",
data: "2025-04-20"

{

nome: "Daniela",
mensagem: "Relatório final enviado. Verifique!",
telefone: "11966666666",
data: "2025-04-20"

},
{

nome: "Vanessa Weber",
mensagem: "Está chegando ao fim do Desafio do Código Fonte TV",
telefone: "12977445588",
data: "2025-04-21"
}
];

Dica: Podemos utilizar a funçao toLowerCase() de
uma string para forçar toda a mensagem a ficar com
letras minúsculas, assim facilita a busca. Devemos
também colocar o termo a ser buscado em
minúsculo.

Outra dica também é utilizar a função includes do
JavaScript. Assim você consegue encontrar qualquer
palavra dentro de uma mensagem rapidamente. O
uso é feito dessa forma:


const mensagem = "Oi, você já terminou o relatório?";
const palavraProcurada = "relatório";

if (mensagem. includes(palavraProcurada)) {
    console. log("Palavra encontrada na mensagem!");
} else {
    console. log("X Palavra não encontrada." );
}
'''
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

# busca linear RECURSIVA que vai buscar TODAS as ocorrências da palavra pesquisada
def buscar_palavra(lista, buscarValor = None, indice = 0):
    '''
    ⚠️ Problemas e melhorias sugeridas:
    1. Os valores encontrados são sobrescritos a cada chamada recursiva
    valores_achados é redefinido a cada chamada da função. Isso faz com que apenas um resultado por chamada seja impresso, e não uma lista acumulada de todos os resultados.

    💡 Solução:

    Você deve acumular os resultados de forma global (fora da função) ou passar valores_achados como argumento para a recursão.

    2. Retorno vazio da função
    Sua função só imprime os valores, mas não retorna uma lista ou dicionário com os resultados encontrados. Isso pode limitar a reutilização da função.

    💡 Solução (opcional):

    Retornar valores_achados ao final da execução completa.
    '''

    # verifica se buscarValor esttá vazio
    if buscarValor is None:
        return print(-1)
    
    # Tratamento do valor recebido para string
    if not isinstance(buscarValor, str):
        to_string = str(buscarValor)
    else:
        to_string = buscarValor

    valores_achados = []

    # Recursão
    if indice >= len(lista):
        return
    
    todos_os_valores_dict = lista[indice].values()

    for valor in todos_os_valores_dict:

        if to_string.lower() in valor.lower():
            valor_achado = (indice, lista[indice])
            valores_achados.append(valor_achado)
            break
    

    # Listar os valores achados com o valor procurado
    for val in valores_achados:
        print(val[0])
        print(f"Nome: {val[1]['nome']}")
        print(f"Mensagem: {val[1]['mensagem']}")
        print(f"Telefone: {val[1]['telefone']}")
        print(f"Data: {val[1]['data']}\n")

    return buscar_palavra(lista, buscarValor, indice+1)





buscar_palavra(mensagens, "vanessa")