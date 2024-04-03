acumul = 0

num = int(input("Informe número da sequência: "))

while num != 0:
    if num % 2 == 0:
        acumul = acumul + num
    num = int(input("Informe número da sequência: "))

print(f"A soma dos pares vale {acumul}")