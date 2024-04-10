bin = int(input("Informe o número binário"))
soma = 0
pot = 1

while bin > 0:
    dig = bin % 10
    bin = bin // 10
    soma = soma + dig * pot
    pot = pot * 2

print(f"Resp {soma}")





