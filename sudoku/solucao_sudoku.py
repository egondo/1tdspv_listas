def cria_matriz():
    mat = [
        [0, 7, 0, 0, 2, 0, 0, 4, 6],
        [0, 6, 0, 0, 0, 0, 8, 9, 0],
        [2, 0, 0, 8, 0, 0, 7, 1, 5],
        [0, 8, 4, 0, 9, 7, 0, 0, 0],
        [7, 1, 0, 0, 0, 0, 0, 5, 9],
        [0, 0, 0, 1, 3, 0, 4, 8, 0],
        [6, 9, 7, 0, 0, 2, 0, 0, 8],
        [0, 5, 8, 0, 0, 0, 0, 6, 0],
        [4, 3, 0, 0, 8, 0, 0, 7, 0]
    ]
    return mat

def pode_linha(mat, l, v):
    for c in range(9):
        if mat[l][c] == v:
            return False
    return True

def pode_coluna(mat, c, v):
    for l in range(9):
        if mat[l][c] == v:
            return False
    return True

def pode_regiao(mat, l, c, v):
    lin_ini = (l // 3) * 3
    col_ini = (c // 3) * 3
    for i in range(3):
        for j in range(3):
            if mat[lin_ini + i][col_ini + j] == v:
                return False            
    return True

def coloca(matriz, lin, col, valor) -> bool:
    if pode_linha(matriz, lin, valor) and pode_coluna(matriz, col, valor) and pode_regiao(matriz, lin, col, valor):
        matriz[lin][col] = valor
        return True
    else:
        return False

def proxima_posicao(atual: tuple) -> tuple:
    lin = atual[0]
    col = atual[1]
    if col == 8:
        return (lin + 1, 0)
    else:
        return (lin, col + 1)
    
def monta_dicionario_posicoes_originais(matriz):
    dic = {}
    for i in range(9):
        for j in range(9):
            if matriz[i][j] != 0:
                dic[(i, j)] = (i, j)
    return dic

pos = (0, 0)
sudoku = cria_matriz()
posicao_original = monta_dicionario_posicoes_originais(sudoku)
pilha = []
while pos != (9, 0):
    lin = pos[0]
    col = pos[1]
    if pos in posicao_original: #se a posicao/valor ja faz parte da matriz original
        pos = proxima_posicao(pos)
    else:
        valor = sudoku[lin][col] + 1
        while not coloca(sudoku, lin, col, valor) and valor < 10:
            valor = valor + 1
        
        if valor < 10:
            pilha.append( pos )
            pos = proxima_posicao(pos)
        else:
            sudoku[lin][col] = 0
            pos = pilha.pop()

for lin in sudoku:
    print(lin)
