import random

def gera_data():
    mes = random.randint(1, 12)
    if mes == 4 or mes == 6 or mes == 9 or mes == 11:
        dia = random.randint(1, 30)
    elif mes == 2:
        dia = random.randint(1, 28)
    else:
        dia = random.randint(1, 31)
    print(f"{dia}/{mes}")
    return f"{dia}/{mes}/2023"



if __name__ == "__main__":
    lojas = ["Ibirapuera", "Analia Franco", "Eldorado"]
    produtos = [
        {"produto": "smartphone", "marcas": ["Samsung", "Xiaomi"], "valor": [1879.99, 1650.48]},
        {"produto": "smart TV", "marcas": ["LG", "Samsung"], "valor": [2500.00, 2879.99]},
        {"produto": "notebook", "marcas": ["Acer", "Asus"], "valor": [3440.78, 3250.87]},
        {"produto": "geladeira", "marcas": ["Brastemp", "Electrolux"], "valor":[4500, 5000]},
        {"produto": "lavadora", "marcas": ["LG", "Brastemp"], "valor": [3800, 2306]},
        {"produto": "console", "marcas": ["Sony", "Nintendo"], "valor": [3500, 2000]}
    ]

    dic_datas = {}
    with open("faturamento_anual.txt", mode="w") as arq:
        i = 0
        while i < 5000:
            data = gera_data()
            while data in dic_datas:
                data = gera_data()
            dic_datas[data] = data

            for p in produtos:
                for loja in lojas:
                    qtd = random.randint(1, 30)
                    linha = f"{p['produto']};{p['marcas'][0]};{loja};{data};{qtd};{p['valor'][0]}"
                    arq.write(linha + "\n")
                    
                    qtd = random.randint(1, 30)
                    linha = f"{p['produto']};{p['marcas'][1]};{loja};{data};{qtd};{p['valor'][1]}"
                    arq.write(linha + "\n")
            i = i + 30        
