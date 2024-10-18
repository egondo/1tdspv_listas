from flask import Flask, request, jsonify
import negocio
import traceback

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
def cadastra_enquete():
    enquete = request.json
    try:
        negocio.cadastra_enquete(enquete)
        return enquete, 201
    except:
        traceback.print_exc()
        return {'title': "deu erro", 'status': 404}, 404



