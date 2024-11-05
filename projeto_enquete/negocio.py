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

def cadastra_respostas(respostas: list):
    pessoa = {}
    lista_respostas = []
    for resp in respostas:
        if resp['numero'] == 1:
            pessoa['nome'] = resp['valor']
        elif resp['numero'] == 2:
            pessoa['idade'] = int(resp['valor'])
        elif resp['numero'] == 3:
            pessoa['genero'] = resp['valor']
        else:
            lista_respostas.append(resp)

    banco.insere_pessoa(pessoa)
    banco.insere_respostas(lista_respostas, pessoa['id'])
    '''[
        {"valor": "Maria", "id_pergunta": 10, "numero": 1},
        {"valor": "35", "id_pergunta": 11, "numero": 2},
        {"valor": "feminino", "id_pergunta": 12, "numero": 3},
        {"valor": "Boulos", "id_pergunta": 13, "numero": 4}
        ]
    '''

def recupera_todas_enquetes():
    lista = banco.recupera_enquetes()
    retorno = []
    for reg in lista:
        retorno.append({"id": reg[0], "nome": reg[1]})
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