let objeto = {
    chavel: "valor1",
    chave2: "valor2",
    // ...
    
    };
    
    // Objeto representando uma pessoa
    let pessoa = {
    nome: "João",
    idade: 30,
    hobbies: ["ler", "correr"],
    falar: function( ) {
    console. log("Olá, meu nome é " + this.nome);
    
    }
    
    };
    
    // Acessando propriedades
    console. log(pessoa.nome); // Saída: João
    
    // Acessando métodos
    pessoa.falar( ); // Saída: Olá meu nome é João




// Criando o nó da lista encadeada
function criarNo(elemento) {
    return {
    data: elemento,
    next: null
    
    };
}
    
// Criando a estrutura básica da lista encadeada
let listaEncadeada = {
    head: null,
    
    insertFirst: function(elemento) {
        const novoNo = criarNo(elemento);
        
        if (!this.head) {
            this.head = novoNo;
        } else {
            novoNo. next = this.head;
            this.head = novoNo;   
        }
        return elemento;
    }
};

console.log(listaEncadeada.insertFirst('Locomotiva'))