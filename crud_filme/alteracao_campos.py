import banco

tupla = banco.consulta_filme_por_id(2)
cols = ['id', 'titulo', 'diretor', 'sinopse', 'classificacao', 'data_lancamento', 'nota', 'genero']
filme = {}
for i in range(len(cols)):
    filme[cols[i]] = tupla[i]

chave = input("Informe a coluna que deseja alterar: ")
valor = input(f"Informe o novo valor do {chave}: ")
filme[chave] = valor
banco.altera_filme(filme)

