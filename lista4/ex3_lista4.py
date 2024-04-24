frase = input("Informe uma frase: ")
letra = input("Informe um caracter: ")

while len(letra) != 1:
    letra = input("Erro, informe um caracter: ")

resp = ""
letra = letra.lower()
letraM = letra.upper()

for c in frase:
    if c == letra or c == letraM:
        resp = resp + "*"
    else:
        resp = resp + c

print(resp)
