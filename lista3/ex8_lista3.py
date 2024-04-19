num = int(input("Numero: "))

divisores = 0
for div in range(1, num + 1):
    if num % div == 0:
        divisores = divisores + 1

if divisores == 2:
    print(f"{num} é primo!")
else:
    print(f"{num} não é primo")    