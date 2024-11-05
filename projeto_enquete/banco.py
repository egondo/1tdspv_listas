import oracledb
import datetime

def get_conexao():
    return oracledb.connect(user="pf0313", password="professor#23",
                        dsn="oracle.fiap.com.br/orcl")

def recupera_enquete_perguntas(id_enquete: int):
    sql = '''select enq.id, enq.nome, per.id, per.numero, per.texto, per.tipo, it.id, it.numero, it.descricao from tbv_enquete enq inner join tbv_pergunta per on enq.id=per.id_enquete left join tbv_item it on per.id = it.id_pergunta where enq.id = :id_enquete order by per.numero, it.numero'''

    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(sql, {"id_enquete": id_enquete})
            return cur.fetchall()
        

def recupera_enquetes():
    sql = "select id, nome from tbv_enquete order by nome"
    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(sql)
            return cur.fetchall()


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


def insere_pessoa(pes: dict):
    sql = "insert into tbv_pessoa(nome, idade, genero, aplicacao) values(:nome, :idade, :genero, :aplicacao) returning id into :id"
    with get_conexao() as con:
        with con.cursor() as cur:
            novo_id = cur.var(oracledb.NUMBER)
            pes['id'] = novo_id
            pes['aplicacao'] = datetime.date.today()
            cur.execute(sql, pes)
            pes['id'] = novo_id.getvalue()[0]
        print(pes)
        con.commit()

def insere_respostas(respostas: list, id_pessoa: int):
    sql = "insert into tbv_resposta(texto, id_pessoa, id_pergunta) values(:valor, :id_pessoa, :id_pergunta)"
    with get_conexao() as con:
        with con.cursor() as cur:
            for resp in respostas:
                resp['id_pessoa'] = id_pessoa
                cur.execute(sql, resp)
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














