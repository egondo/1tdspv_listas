import time

def busca(conjunto: list, valor: object) -> int:
    i = 0
    while i < len(conjunto) and conjunto[i] != valor:
        i = i + 1

    if i < len(conjunto):
        return i
    else:
        return -1
    

lista = [2, -6, 9, 5, 2, 0, 4, 3, 12]
resp = busca(lista, 0)
print(resp)

lista = [0] * 1_000_000_000

ini = time.time()
resp = busca(lista, 1)
fim = time.time()
print(fim - ini)

print(resp)





