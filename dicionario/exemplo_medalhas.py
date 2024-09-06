if __name__ == "__main__":
    quadro = {
                "China": [45, 32, 16],
                "Grã Bretanha": [29, 16, 12],
                "Estados Unidos": [15, 19, 11],
                "Brasil": [13, 9, 20],
                "França": [11, 10, 13]
              }
    
    medalhas = {}
    medalhas["China"] = [45, 32, 16]
    medalhas["Grã Bretanha"] = [29, 16, 12]
    medalhas['Estados Unidos'] = [15, 19, 11]
    medalhas["Brasil"] = [13, 9, 20]
    medalhas["França"] = [11, 10, 13]


    print(medalhas['Brasil'])
    print(medalhas.get('China'))
    #print(quadro['Egito'])

    pais = input("Informe um país: ")
    ouro = int(input("Ouro: "))
    prata = int(input("Prata: "))
    bronze = int(input("Bronze: "))

    if not pais in medalhas:
        medalhas[pais] = [ouro, prata, bronze]
    else:
        print("Não foi possível inserir o país")

    for chave in medalhas.keys():
        print(chave, '=>', medalhas[chave])

