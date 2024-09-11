def busca(matriz: list, valor: object) -> list:
    lin = len(matriz)
    col = len(matriz[0])
    for i in range(lin):
        for j in range(col):
            if matriz[i][j] == valor:
                return [i, j]
    return [-1, -1]

