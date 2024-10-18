import oracledb

def get_conexao():
    return oracledb.connect(user="pf0313", password="professor#23",
                        dsn="oracle.fiap.com.br/orcl")

def insere_enquete(enquete: dict):
    sql = "insert into tbv_enquete(nome, data) values(:nome, sysdate) returning id into :id"
    with get_conexao() as con:
        with con.cursor() as cur:
            novo_id = cur.var(oracledb.NUMBER)
            enquete['id'] = novo_id
            cur.execute(sql, enquete)
            enquete['id'] = novo_id.getvalue()[0]
        print(enquete)
        con.commit()


def insere_perguntas(perguntas: list):






