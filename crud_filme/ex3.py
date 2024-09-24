import banco

clas = input("Classif: ")
filmes = banco.consulta_filme(clas)

for f in filmes:
    print(f)