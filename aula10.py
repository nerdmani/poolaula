## Comando para ir retirando Letras ou palavras.
palavra_chave = '' ## Para colocar o printo na mesma linha.

usuario_palavra = input("Entre com uma palavra: ")
usuario_palavra = usuario_palavra.upper() ## Upper: Somente Letras maiusculas.

for letra in usuario_palavra:
    if letra ==  "A":
        continue 
    if letra ==  "O":
        continue 
    if letra ==  "E":
        continue 
    if letra ==  "I":
        continue 
  
    else: 
        palavra_chave += letra
    
print(palavra_chave)
        
        