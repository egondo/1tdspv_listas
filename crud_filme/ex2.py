import banco
import datetime

filmes = [
    ['Estrelas Além do Tempo', 'Theodore Melfi', '''No auge da 
     corrida espacial travada entre Estados Unidos e Rússia 
     durante a Guerra Fria, uma equipe de cientistas da NASA, 
     formada exclusivamente por mulheres afro-americanas, provou 
     ser o elemento crucial que faltava na equação para a vitória 
     dos Estados Unidos''', 8.8, datetime.datetime(2017, 1, 6),
     'livre', 'drama'],

     ['Uma mente brilhante', 'Tom Hanks', '''Narra a história de Jonh Nash, 
      vencedor do Prêmio Nobel de Economia''', 9, 
      datetime.datetime(2011, 10, 10), '14 anos', 'romance'],

      ['ET o Extraterrestre', 'Steven Spielberg', 'A passagem dos et na TERRA',
       9.2, datetime.datetime(1989, 12, 25), 'livre', 'infantil']
]

for linha in filmes:
    filme = {'titulo': linha[0], 'diretor': linha[1],
             'sinopse': linha[2], 'nota': linha[3],
             'data_lancamento': linha[4], 
             'classificacao': linha[5], 'genero': linha[6]}
    banco.insere_filme(filme)