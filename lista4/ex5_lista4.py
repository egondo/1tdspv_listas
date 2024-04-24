frase = input("Digite uma frase: ").lower()

palavra = input("Digite uma palavra: ").lower()
i = 0
contador = 0
pos = frase.find(palavra, i)
while  pos != -1:
    contador = contador + 1
    i = pos + 1
    pos = frase.find(palavra, i)

print(contador)