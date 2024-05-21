def interseccao(listaA, listaB):
    res = []
    for elem in listaA:
        if elem in listaB:
            res.append(elem)
    return res


a = [2, 5, 8, 9, -1, 3, 0, 5]
b = [-1, 10, 4, 3, 2, 6, 11, 16, 0]

resp = interseccao(a, b)
print(resp)


