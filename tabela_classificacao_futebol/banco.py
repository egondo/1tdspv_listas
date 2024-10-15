import oracledb

def get_conexao():
    return oracledb.connect(user='pf0313', password='professor#23',
                            dsn='oracle.fiap.com.br/orcl')

#{'visi': 'Palmeiras', 'casa': 'Santos', 'gv': 1, 'gc': 3, 'rodada': 1}
def insere_partida(partida: dict):
    sql = "insert into tb_partida(id_casa, id_visitante, gols_casa, gols_visitante, rodada) values(:casa, :visi, :gc, :gv, :rodada)"
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
    sql = "select id, nome, vitorias, empates, derrotas, gols_contra, gols_pro from tb_time where nome = :nome"
    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(sql, {'nome': nome})
            reg = cur.fetchone()
            if not reg:
                return None
            else:
                return {'id':reg[0], 'nome': reg[1], 'vitorias': reg[2], 'empates': reg[3], 'derrotas': reg[4], 'gols_contra': reg[5], 'gols_pro': reg[6]}


def recupera_times() -> list:
    sql = "select id, nome, vitorias, empates, derrotas, gols_contra, gols_pro from tb_time"
    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(sql)
            registros = cur.fetchall()
            lista = []
            for reg in registros:
                time = {'id':reg[0], 'nome': reg[1], 'vitorias': reg[2], 'empates': reg[3], 'derrotas': reg[4], 'gols_contra': reg[5], 'gols_pro': reg[6]}
                lista.append(time)
    return lista


def insere_time(time: dict):
    #insere o time pegando o id que foi gerado pelo banco de dados
    sql = "insert into tb_time(nome, vitorias, empates, derrotas, gols_contra, gols_pro) values(:nome, :vitorias, :empates, :derrotas, :gols_contra, :gols_pro) returning id into :id"
    
    with get_conexao() as con:
        with con.cursor() as cur:
            novo_id = cur.var(oracledb.NUMBER)
            time['id'] = novo_id
            cur.execute(sql, time)
        con.commit()
        time['id'] = novo_id.getvalue()[0]


#select nome, vitorias+empates+derrotas as jogos, vitorias * 3 + empates as pts, vitorias, empates, derrotas, gols_contra, gols_pro, gols_pro - gols_contra as saldo, (300*vitorias+empates)/((vitorias+empates+derrotas) * 3) as aproveitamento from tb_time order by pts desc        