n = int(input("Informe n: "))

if n == 1 or n == 2:
    print(f"F{n} = 1")
else:
    ant = 1
    atual = 1
    conta = 2
    while conta < n:
        prox = ant + atual
        ant = atual
        atual = prox
        conta = conta + 1
        
    print(f"F{n} = {atual}")    



