#pip install oracledb
import oracledb

def get_conexao():
    return oracledb.connect(user='pf0313', password='professor#23',
                            dsn='oracle.fiap.com.br/orcl')

def insere_filme(movie: dict):
    sql = '''INSERT into filme(titulo, diretor, data_lancamento,
            sinopse, genero, nota, classificacao) values(:titulo,
            :diretor, to_date(:data_lancamento, 'DD-MM-YYYY'),
             :sinopse, :genero, :nota, :classificacao)'''
    #con = get_conexao()
    with get_conexao() as con:
        #cur = con.cursor()
        with con.cursor() as cur:
            cur.execute(sql, movie)
        con.commit()
    #cur.close()
    #con.close()

def consulta_filme(genero: str) -> list:
    sql = '''select id, titulo, diretor, sinopse, classificacao,
     data_lancamento, nota, genero from filme 
     where genero like :genero'''

    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(sql, {"genero": genero})    
            return cur.fetchall()

def altera_filme(movie: dict):
    sql = '''update filme set titulo=:titulo, diretor=:diretor, 
        sinopse=:sinopse, genero=:genero, nota=:nota, 
        data_lancamento=to_date(:data_lancamento, 'DD-MM-YYYY'),
        classificacao=:classificacao where id=:id'''
    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(sql, movie)
        con.commit()

def apaga_filme(id: int):
    sql = "delete from filme where id=:id"
    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(sql, {"id": id})
        con.commit()
        








