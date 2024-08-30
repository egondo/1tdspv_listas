def cadastra(lista: list):
    marca = input("Informe a marca: ")
    modelo = input("Informe o modelo: ")
    ano = int(input("Ano do carro: "))
    placa = input("Informe a placa: ")
    cor = input("Cor: ")
    registro = [marca, modelo, ano, placa, cor]
    lista.append(registro)

def altera(lista: list):
    placa = input("Informe a placa: ")
    pos = busca(lista, placa)
    if pos == -1:
        print(f"Nenhum veiculo encontrado com a placa: {placa}")
    else:
        print(lista[pos])
        marca = input("Digite a marca")
        if len(marca) > 0:
            lista[pos][0] = marca
        modelo = input("Digite o modelo: ")
        if len(modelo) > 0:
            lista[pos][1] = modelo
        ano = input("Ano: ")
        if len(ano) > 0:
            lista[pos][2] = int(ano)
        

def busca(matriz, placa):
    for i in range(len(matriz)):
        if matriz[i][3] == placa:
            return i
    return -1

def consulta(lista: list):
    for lin in lista:
        print(lin)

    for i in range(len(lista)):
        print(lista[i])

def remove(lista: list):
    placa = input("Placa: ")
    pos = busca(lista, placa)
    if pos == -1:
        print(f"Não há veiculos com a placa {placa}")
    else:
        lista.pop(pos)
        #del lista[pos]


def grava_arquivo(matriz: list):
    arq = open("d:/carros.dat", mode="w")
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            arq.write(f"{matriz[i][j]};")
        arq.write("\n")
    arq.close()





banco = []
opcao = -1
while opcao != 5:
    print("1 - cadastra carro")
    print("2 - altera")
    print("3 - consulta")
    print("4 - remove")
    print("5 - sair")
    opcao = int(input("Opção: "))

    if opcao == 1:
        cadastra(banco)
    elif opcao == 2:
        altera(banco)
    elif opcao == 3:
        consulta(banco)
    elif opcao == 4:
        remove(banco)
    elif opcao == 5:
        grava_arquivo(banco)