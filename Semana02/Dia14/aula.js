// Antes do Desafio, vamos falar de JSON.
// JSON é uma forma de notação, em formato de texto, de transmissão de dados e informações entre sistemas

// JSON é formado por chave-valor, onde cada elemento é representado por uma chave e um valor.

// Formato
const variavel = { chave: "valor", cahve2: "valor2" };

// Exemplo Real
const cliente = {nome: 'João', idade: 30, prioridade: true};

// Exemplo co arrays
const cidade = { bairro1: ["Rua A", "Rua B"], bairro2: ["Rua C", "Rua D"]};

// Iterando pelos bairros
for (let bairro in cidade) {
    console.log(`${bairro}: ${cidade[bairro].join(", ")}`);
}