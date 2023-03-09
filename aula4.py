## Ultilização de While como senha.

tentativa = 0

while tentativa < 3:
    senha = input('Digite sua senha: ')
    if senha == "senha123":
        print('Acesso concedido!!! Finalmente Gio!!')
        break
    else:
        print("Senha Incorreta. Tenta novamente Gio .")
        tentativa += 1
else:
    print("Você excedeu seu numero maximos de tentativas Gio. Por favor olhe seu E-mail")