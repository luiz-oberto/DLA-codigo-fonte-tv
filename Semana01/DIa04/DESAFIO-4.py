"""
DESAFIO 04: Condição ternária com expressão mais complexa

Um cliente possui uma conta em uma loja com um certo saldo para compras e uma condição que indica
se a conta está ativa ou não. Sua tarefa é escrever um código que determine se o cliente pode fazer
compras com sua conta.

As condições para poder comprar são: 
- a conta precisa estar ativa (ou seja, o cliente não deve estar inativo) e;
- o saldo deve ser maior que 500.

Use a condição ternária para isso.
"""
saldo = 5033
conta_is_ativa = False

situacao = "Compras liberadas" if conta_is_ativa and saldo > 500 else "Não foi possível efetuar a compra, consulte seu ADM."
print(situacao)