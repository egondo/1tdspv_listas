def mmc(a, b):
    x = a
    while x % b != 0:
        x = x + a
    return x

a = int(input("Informe a: "))
b = int(input("Informe b: "))
res = mmc(a, b)
print(f"{res} é múltiplo de {a} e {b}")
