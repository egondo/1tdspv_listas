frase = input("Informe uma frase: ")
letras = input("Informe um conjunto de letras: ")

letras = letras.lower()
letrasM = letras.upper()

resp = ""
for c in frase:
    if c in letras or c in letrasM:
        resp = resp + "*"
    else:
        resp = resp + c

print(resp)