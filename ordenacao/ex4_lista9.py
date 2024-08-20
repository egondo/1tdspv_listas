def bubble_sort(lista: list):
    for i in range(len(lista)):
        subir(lista)

def subir(lista):
    pos = len(lista) - 1
    while pos > 0:
        if lista[pos] < lista[pos-1]:
            aux = lista[pos]
            lista[pos] = lista[pos-1]
            lista[pos-1] = aux
        pos = pos - 1        

if __name__ == "__main__":
    nomes = ["Bruno", "Betao", "Bernardo", "Barbara", "Bira", "Boccardi", "Barnabe", "Bianca", "Buba"]
    bubble_sort(nomes)
    print(nomes)
    