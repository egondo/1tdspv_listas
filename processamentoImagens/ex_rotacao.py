import Imagem

def rotaciona(matriz):
    lin = len(matriz)
    col = len(matriz[0])
    rot_mat = []
    for i in range(lin):
        rot_mat.append([0] * col)

    for i in range(lin):
        for j in range(col):
            l = lin - i - 1
            c = col - j - 1
            rot_mat[l][c] = matriz[i][j]    
    return rot_mat        

if __name__ == "__main__":
    yao = Imagem.getMatrizImagemCinza("yao-ming.png")
    yao_rot = rotaciona(yao)
    Imagem.salvaImagemCinza("yao_rot.png", yao_rot)