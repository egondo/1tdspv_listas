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

def recupera_enquete(id: int) -> dict:
    lista = banco.recupera_enquete_perguntas(id)
    retorno = {'perguntas': []}

    aux_id_pergunta = -1

    for reg in lista:
        retorno['id'] = reg[0] #id da enquete
        retorno['nome'] = reg[1] #nome da enquete
        if aux_id_pergunta != reg[2]:
            perg = {"id": reg[2], "numero": reg[3], "texto": reg[4], "tipo": reg[5], "opcoes": []}
            retorno['perguntas'].append(perg)
            aux_id_pergunta = reg[2]

        if reg[5] != "aberta":
            opcao = {"id": reg[6], "numero": reg[7], "descricao": reg[8]}
            perg['opcoes'].append(opcao)

    return retorno


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
    #cadastra_enquete(e)
    enq = recupera_enquete(3)
    print(enq)