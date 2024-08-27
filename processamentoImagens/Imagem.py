from PIL import Image

def getMatrizImagemColorida(nome_imagem):
    im = Image.open(nome_imagem)
    (largura, altura) = im.size
    matrizR = []
    matrizG = []
    matrizB = []
    pixels = im.getdata()
    k = 0
    for j in range(altura):
        linhaR = []
        linhaG = []
        linhaB = []
        for i in range(largura):
            linhaR.append(pixels[k][0])
            linhaG.append(pixels[k][1])
            linhaB.append(pixels[k][2])
            k = k + 1
        matrizR.append(linhaR)
        matrizG.append(linhaG)
        matrizB.append(linhaB)
    return matrizR, matrizG, matrizB

def getMatrizImagemCinza(nome_imagem):
    im = Image.open(nome_imagem)
    (largura, altura) = im.size
    matrizC = []
    pixels = im.getdata()
    k = 0
    for i in range(altura):
        linha = []
        for j in range(largura):
            if type(pixels[k]) is tuple:
                linha.append(pixels[k][0])
            else:
                linha.append(pixels[k])
            k = k + 1
        matrizC.append(linha)
    return matrizC

def salvaImagemColorida(nome_imagem, matrizR, matrizG, matrizB):
    dimensao = (len(matrizR[0]), len(matrizR))
    im = Image.new("RGB", dimensao)
    dados = []
    for i in range(dimensao[1]):
        for j in range(dimensao[0]):
            dados.append((matrizR[i][j], matrizG[i][j], matrizB[i][j]))
    im.putdata(dados)
    im.save(nome_imagem)


def salvaImagemCinza(nome_imagem, matrizC):
    dimensao = (len(matrizC[0]), len(matrizC))
    im = Image.new("L", dimensao)
    dados = []
    for i in range(dimensao[1]):
        for j in range(dimensao[0]):
            dados.append(matrizC[i][j])
            
    im.putdata(dados)
    im.save(nome_imagem)

