## Este codico vai contar de 0 até 9, se fou = a 0 ele sera 0. Se ele for divisivel por 2 é par, caso contrario é impar.

## Indentifica se o numero é impar ou par.
numero = 0

while numero < 10:
    if numero == 0:
        print('O numero é 0')
    elif numero % 2 == 0:
        print('O numero é par')
    else: 
        print('O numero é impar')
    
    numero += 1
    
## Melhoria de código.

numero = 0

while numero < 100:
    if numero == 0:
        print('O numero', numero,  'é 0')
    elif numero % 2 == 0:
        print('O numero', numero, 'é par')
    else: 
        print('O numero', numero, 'é impar')
    
    numero += 1
