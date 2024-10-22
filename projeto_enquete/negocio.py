import banco

'''{
    "nome": "Pesquisa eleitoral",
    "perguntas": [
        {"numero": 1, "texto": "Qual o seu nome?", "tipo": "aberta"},
        {"numero": 2, "texto": "Qual a sua idade?", "tipo": "aberta"},
        {"numero": 3, "texto": "Gênero?", "tipo": "escolha única", 
            "itens": [{"numero": 1, "descricao": "masculino"},
                      {"numero": 2, "descricao": "feminino"}
                    ]
        },
        {"numero": 4, "texto": "Há quantos anos você vota?", "tipo": "aberta"},
        {"numero": 5, "texto": "Em quem você vai votar?", "tipo": "escolha única",
            "itens": [
                {"numero": 1, "descricao": "Guilherme Boulos"},
                {"numero": 2, "descricao": "Ricardo Nunes"}
            ]
        }
    ]
}'''
def cadastra_enquete(objeto: dict):
    enq = {"nome": objeto['nome']}
    banco.insere_enquete(enq)
    banco.insere_perguntas(objeto['perguntas'], enq['id'])


if __name__ == "__main__":
    e = {
    "nome": "Pesquisa eleitoral",
    "perguntas": [
        {"numero": 1, "texto": "Qual o seu nome?", "tipo": "aberta"},
        {"numero": 2, "texto": "Qual a sua idade?", "tipo": "aberta"},
        {"numero": 3, "texto": "Gênero?", "tipo": "escolha única", 
            "itens": [{"numero": 1, "descricao": "masculino"},
                      {"numero": 2, "descricao": "feminino"}
                    ]
        },
        {"numero": 4, "texto": "Há quantos anos você vota?", "tipo": "aberta"},
        {"numero": 5, "texto": "Em quem você vai votar?", "tipo": "escolha única",
            "itens": [
                {"numero": 1, "descricao": "Guilherme Boulos"},
                {"numero": 2, "descricao": "Ricardo Nunes"}
            ]
        }
    ]
    }
    cadastra_enquete(e)