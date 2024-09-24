import banco
import datetime

print("Cadastro de filme: ")
tit = input("Título: ")
dir = input("Diretor: ")
sin = input("Sinopse: ")
dia = int(input("Dia: "))
mes = int(input("Mes: "))
ano = int(input("Ano: "))
data = datetime.datetime(ano, mes, dia)
gen = input("Gênero: ")
nota = float(input("Nota: "))
cla = input("Classificação: ")

filme = {'titulo': tit, 'diretor': dir, 
         'sinopse': sin, 'data_lancamento': data}
filme['genero'] = gen
filme['nota'] = nota
filme['classificacao'] = cla
banco.insere_filme(filme)