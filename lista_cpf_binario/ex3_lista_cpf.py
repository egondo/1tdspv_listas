cpf = int(input("Informe o cpf com 9 dígitos: "))
soma = 0

mult = 2

while cpf != 0:
    dig = cpf % 10
    cpf = cpf // 10
    soma = soma + dig * mult
    mult = mult + 1

resto = soma % 11
if resto < 2:
    print(0)
else:
    print(11 - resto)




