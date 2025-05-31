# DESAFIO 01: Super desafio final!

Vamos criar um código para simular transações Pix
em uma conta bancária, mas teremos algumas
regras bem específicas. Então preste bastante
atenção!

1. Vamos fornecer uma estrutura inicial em JSON
com o saldo, o limite diário para transferências (que
será de R$ 10.000), teremos um controle para saber
o quanto já foi transferido no dia, um histórico de
transações por Pix e também um total já transferido
por chave Pix.

Exatamente como está neste código.
``` javascript
const conta = {
    saldo: 50000,
    limiteDiario: 10000,
    totalTransferidoHoje: 0,
    historicoTransacoes: [],
    totalPorChave: {} // Armazena total transferido por chave Pix

};
```

2. Você deverá implementar 2 operações Pix, uma
para enviar o Pix e outra para cancelar (ou seja, fazer
o reembolso). Para isso você deve utilizar a
**chavePix**, o **valor** a ser transferido e uma
**mensagem** de referência. Para cancelar, basta utilizar
o **indice** da transação para facilitar.


3. A regra será a seguinte: A conta terá um limite
máximo diário de R$ 10.000 para realizar Pix;

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

    Espero que tenha ficado claro. Agora partiu arrasar
no código e resolver esse último desafio! Não
esqueça que você pode baixar toda essa
especificação e o código inicial da conta.

"*Aquele que pergunta é um tolo por cinco minutos, mas aquele que não pergunta permanece um tolo para sempre.*" - Provérbio Chinês