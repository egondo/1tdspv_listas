import math

numero = float(input("Informe um número: "))

if numero < 0:
    print("Impossível extrair a raiz quadrada!")
else:
    raiz = math.sqrt(numero)
    print(f"A raiz quadrada de {numero} vale {raiz}")

    