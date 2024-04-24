palavra = "cadeira"
erros = 0
segredo = ""

for c in palavra:
    #segredo = f"{segredo}_ "
    segredo = segredo + "_ "

print(f"{segredo}\nerros: {erros}")
letra = input("Letra: ")
          
segredo = ""
for c in palavra:
    if c in letra:
        segredo = segredo + c + " "
    else:
        segredo = segredo + "_ "

print(f"{segredo}\nerros: {erros}")
letra = input("Letra: ")