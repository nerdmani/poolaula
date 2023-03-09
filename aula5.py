## Armazena um numero pequeno

mn = -9999999

## Entra com o primeiro numero

number = int(input('Entre com um numero ou digite 0 para parar: '))

## Se o numero não for igual a -1 contnua

while number != 0:
    
    ## O numero maior é maior que o MN
    if number > mn:
    
    ## Sim atualiza o MN.
        mn = number
    
    ## Entre com o próximo numero.
    number = int(input("Entre com um numero ou digite 0 para parar: "))
    
## Imprimir o maior numero.
print('O maior numero é: ', mn)