import oracledb

def get_conexao():
    return oracledb.connect(user='pf0313', password='professor#23',
                            dsn='oracle.fiap.com.br/orcl')

#{'visi': 'Palmeiras', 'casa': 'Santos', 'gv': 1, 'gc': 3, 'rodada': 1}
def insere_partida(partida: dict):
    sql = "insert into tb_partida(id_casa, id_visi, gols_casa, gols_visitante, rodada) values(:casa, :visi, :gc, :gv, :rodada)"
    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(sql, partida)
        con.commit()

#{'nome': 'Palmeiras', 'vitorias': 2, 'empates': 1, 'derrotas': 0, 'gols_contra': 5, 'gols_pro': 9, 'id': 23}
def altera_time(time: dict):
    sql = "update tb_time set nome=:nome, vitorias=:vitorias, empates=:empates, derrotas=:derrotas, gols_contra=:gols_contra, gols_pro=:gols_pro where id=:id"
    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(sql, time)
        con.commit()

def recupera_time_nome(nome: str) -> dict:
    pass

def insere_time(time: dict):
    #insere o time pegando o id que foi gerado pelo banco de dados
    pass