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