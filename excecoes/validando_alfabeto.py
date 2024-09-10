import re

def valida_letras(info: str) -> bool:
    alfabeto = 'abcdefghijklmnopqrstuvxywz'
    for letra in info:
        if not letra in alfabeto:
            return False
    return True

def valida_letras2(info: str) -> bool:
    for letra in info:
        obj = re.search("[a-zA-Z ]", letra)
        if obj == None:
            return False
    return True

texto = input("Texto: ")
if valida_letras2(texto):
    print("Só tem letras")
else:
    print("Existem outros simbolos que nao sao letras")