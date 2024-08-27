import Imagem

if __name__ == "__main__":
    tupla = Imagem.getMatrizImagemColorida("lago_canada.jpg")
    matriz_r = tupla[0]
    matriz_g = tupla[1]
    matriz_b = tupla[2]

    linhas = len(matriz_r)
    colunas = len(matriz_r[0])
    print("Dimensao", linhas, "X", colunas)

    Imagem.salvaImagemColorida("lago_desfigurado.png", matriz_b, matriz_r, matriz_g)
    print("Programa finalizado!")

    #criando uma matriz 750X1000
    matriz_cinza = []
    for i in range(linhas):
        matriz_cinza.append([0] * colunas)

    for i in range(linhas):
        for j in range(colunas):
            matriz_cinza[i][j] = (matriz_r[i][j] + matriz_g[i][j] + matriz_b[i][j]) // 3

    Imagem.salvaImagemCinza("lago_cinza.png", matriz_cinza)