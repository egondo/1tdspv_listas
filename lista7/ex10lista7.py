def intercala(lista_a, lista_b):
    resposta = []
    i = 0
    j = 0
    while i < len(lista_a) and j < len(lista_b):
        if lista_a[i] < lista_b[j]:
            resposta.append(lista_a[i])
            i = i + 1
        else:
            resposta.append(lista_b[j])
            j = j + 1
    
    while i < len(lista_a):
        resposta.append(lista_a[i])
        i = i + 1
    while j < len(lista_b):
        resposta.append(lista_b[j])
        j = j + 1
    return resposta


a = [3.4, 8.9, 15.1, 18.0, 45.3, 48.8, 55.5]
b = [-0.8, 1.2, 7.5, 12.0, 13.1, 23.4, 35.8, 38.9, 41.9]
resultado = intercala(a, b)
print(resultado)



