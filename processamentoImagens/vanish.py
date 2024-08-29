import Imagem

def tem_vizinho_branco(matriz: list, i: int, j:int) -> bool:
    lin = len(matriz)
    col = len(matriz[0])

    if i >= 1 and j >= 1 and matriz[i-1][j-1] == 255:
        return True
    
    if i >= 1 and matriz[i-1][j] == 255:
        return True
    
    if i >= 1 and j < col -1 and matriz[i-1][j+1] == 255:
        return True
    
    if j >= 1 and matriz[i][j-1] == 255:
        return True
    
    if matriz[i][j] == 255:
        return True
    
    if j < col - 1 and matriz[i][j+1] == 255:
        return True
    
    if i < lin - 1 and j >= 1 and matriz[i+1][j-1] == 255:
        return True
    
    if i < lin - 1 and matriz[i+1][j] == 255:
        return True
    
    if i < lin - 1 and j < col - 1 and matriz[i+1][j+1] == 255:
        return True
    
    return False


if __name__ == "__main__":
    mat = Imagem.getMatrizImagemCinza("yao2.png")
    lin = len(mat)
    col = len(mat[0])
    
    aux = []
    for i in range(lin):
        aux.append([0] * col)

    for i in range(lin):
        for j in range(col):
            if tem_vizinho_branco(mat, i, j): 
                aux[i][j] = 255

    Imagem.salvaImagemCinza("yao3.png", aux)