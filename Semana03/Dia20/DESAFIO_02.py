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