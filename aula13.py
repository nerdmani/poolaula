tipo = input('Digite o tipo de palavra que deseja imprimir (par ou impar): ')
for i in range (1, 11):
    if tipo == "par" and i % 2 == 0:
        print (i)
    elif tipo == 'impar' and i % 2 !=0:
        print(i)