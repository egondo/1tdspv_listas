import banco

filme = {}
filme['titulo'] = 'O Jogo da Imitação'
filme['diretor'] = 'Morten Tyldum'
filme['nota'] = 9.5
filme['sinopse'] = '''Governo do Reino Unido arregimenta, durante a Segunda Guerra Mundial, uma turma de cientistas para decifrar o código Enigma, usado pelos oficiais alemães para enviar mensagens aos submarinos.'''
filme['genero'] = 'suspense'
filme['classificacao'] = '14 anos'
filme['id'] = 1
filme['data_lancamento'] = '14-11-2014'

banco.altera_filme(filme)
