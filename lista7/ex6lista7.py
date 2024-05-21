def insere_ordenado(valor, lista):
    i = 0
    while i < len(lista) and lista[i] < valor:
        i = i + 1

    lista.insert(i, valor)

vet = [1, 6, 10, 24, 25, 30, 45]
insere_ordenado(20, vet)
print(vet)

insere_ordenado(100, vet)
print(vet)    