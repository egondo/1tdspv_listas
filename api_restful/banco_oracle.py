import oracledb

def get_conexao():
    return oracledb.connect(user="pf0313", password="professor#23",
                            dsn="oracle.fiap.com.br/orcl")

def recupera_todos():
    sql = "select id, modelo, montadora, placa, ano from tb_carro"
    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(sql)
            return cur.fetchall()
        
def recupera_id(id):
    sql = "select id, modelo, montadora, placa, ano from tb_carro where id = :id"
    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(sql, {"id": id})
            return cur.fetchone()

def insere(carro: dict):
    sql = "insert into tb_carro(modelo, montadora, ano, placa) values(:modelo, :montadora, :ano, :placa) returning id into :id"
    with get_conexao() as con:
        with con.cursor() as cur:
            novo_id = cur.var(oracledb.NUMBER)
            carro['id'] = novo_id
            cur.execute(sql, carro)
            carro['id'] = novo_id.getvalue()[0]
        con.commit()

def altera(carro: dict):
    sql = "update tb_carro set modelo=:modelo, montadora=:montadora, placa=:placa, ano=:ano where id=:id"

    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(sql, carro)
        con.commit()        