import oracledb

def get_conexao():
    return oracledb.connect(user="pf0313", password="professor#23",
                        dsn="oracle.fiap.com.br/orcl")

def insere_enquete(enquete: dict):
    sql = "insert into tbv_enquete(nome) values(:nome) returning id into :id"
    with get_conexao() as con:
        with con.cursor() as cur:
            novo_id = cur.var(oracledb.NUMBER)
            enquete['id'] = novo_id
            cur.execute(sql, enquete)
            enquete['id'] = novo_id.getvalue()[0]
        print(enquete)
        con.commit()


def insere_perguntas(perguntas: list, id_enquete: int):
    sql = "insert into tbv_pergunta(numero, texto, tipo, id_enquete) values(:numero, :texto, :tipo, :id_enquete) returning id into :id"
    sql_item = "insert into tbv_item(numero, descricao, id_pergunta) values(:numero, :descricao, :id_pergunta)"

    with get_conexao() as con:
        with con.cursor() as cur:
            for questao in perguntas:

                questao['id_enquete'] = id_enquete

                if questao['tipo'] != 'aberta':
                    itens = questao.pop('itens')
                else:
                    itens = None

                novo_id = cur.var(oracledb.NUMBER)
                questao['id'] = novo_id
                cur.execute(sql, questao)
                questao['id'] = novo_id.getvalue()[0]
                
                if itens != None:
                    for item in itens:
                        item['id_pergunta'] = questao['id']
                        cur.execute(sql_item, item)
        con.commit()














