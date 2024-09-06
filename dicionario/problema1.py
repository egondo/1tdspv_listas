contagem = {}

texto = input("Informe uma msg: ")
texto = texto.upper()
for letra in texto:
    if letra != ' ':
        if letra in contagem:
            v = contagem.get(letra)
            contagem[letra] = v + 1
        else:
            contagem[letra] = 1

for letra in sorted(contagem.keys()):
    print(letra, "=>", contagem[letra])
