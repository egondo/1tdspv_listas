num = int(input("Informe número: "))

soma = 0
mult = 2
while num != 0:
    dig = num % 10
    prod = dig * mult
    soma = soma + prod // 10 + prod % 10
    if mult == 2:
        mult = 1
    else:
        mult = 2
    num = num // 10

resto = soma % 10
if resto == 0:
    print(f"DC = 0")
else:
    print(f"DC = {10 - resto}")    