palavra = "cadeira de praia"
erros = 0
segredo = ""
letras_chutadas = ""

for c in palavra:
    #segredo = f"{segredo}_ "
    if c == " ":
        segredo = segredo + "  " 
    else:
        segredo = segredo + "_ "

while erros < 6 and '_' in segredo:
    print(f"{segredo}\nerros: {erros}")
    letra = input("Letra: ")
    letras_chutadas = letras_chutadas + letra
    
    if not letra in palavra:
        erros = erros + 1

    segredo = ""
    for c in palavra:
        if c in letras_chutadas:
            segredo = segredo + c + " "
        else:
            segredo = segredo + "_ "

if erros >= 6:
    print(f"Você perdeu, a palavra era {palavra}")
else:
    print(f"Você acertou, a palavra e {palavra}")
