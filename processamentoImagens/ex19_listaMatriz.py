import Imagem

def desenha_coluna(img: list, pos: int, valor: int):
    linFim = 550
    col = pos
    lin = linFim - valor * 5
    colFim = pos + 45

    while lin <= linFim:
        col = pos
        while col <= colFim:
            img[lin][col] = 100
            col = col + 1
        lin = lin + 1


matriz = []
for i in range(600):
    matriz.append([255] * 800)

desenha_coluna(matriz, 50, 60)
desenha_coluna(matriz, 100, 75)
desenha_coluna(matriz, 150, 65)
desenha_coluna(matriz, 200, 40)


Imagem.salvaImagemCinza("histograma.png", matriz)
print("Imagem criada!")
