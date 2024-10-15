import banco

def encontra_time(nome: str) -> dict:
    #recuperar o time pelo nome no banco de dados
    #se o time nao existe entao gravo o time no banco e retorno ele 
    #se o time ja existe entao simplesmente, retorno o time.
    time = banco.recupera_time_nome(nome)
    if time == None:
        time = {'nome': nome, 'vitorias': 0, 'empates': 0, 'derrotas': 0, 'gols_contra': 0, 'gols_pro': 0}
        banco.insere_time(time)
    
    return time


#{'nome': 'Palmeiras', 'vitorias': 2, 'empates': 1, 'derrotas': 0, 'gols_contra': 5, 'gols_pro': 9, 'id': 23}

#{'visi': 'Palmeiras', 'casa': 'Santos', 'gv': 1, 'gc': 3, 'rodada': 1}
def cadastra_partida(jogo: dict):
    time_casa = encontra_time(jogo['casa'])
    time_visi = encontra_time(jogo['visi'])

    if jogo['gc'] > jogo['gv']:
        time_casa['vitorias'] = time_casa['vitorias'] + 1
        time_visi['derrotas'] = time_visi['derrotas'] + 1
    elif jogo['gc'] < jogo['gv']:
        time_casa['derrotas'] = time_casa['derrotas'] + 1
        time_visi['vitorias'] = time_visi['vitorias'] + 1
    else:
        time_casa['empates'] = time_casa['empates'] + 1
        time_visi['empates'] = time_visi['empates'] + 1

    time_casa['gols_contra'] += jogo['gv']
    time_casa['gols_pro'] += jogo['gc']

    time_visi['gols_contra'] += jogo['gc']
    time_visi['gols_pro'] += jogo['gv']

    #atualiza os dois times no banco de dados
    banco.altera_time(time_casa)
    banco.altera_time(time_visi)

    #colocar os ids dos times em casa e visi respectivamente
    jogo['casa'] = time_casa['id']
    jogo['visi'] = time_visi['id']
    
    #cadastrar a partida no banco de dados
    banco.insere_partida(jogo)

def recupera_times():
    dados = banco.recupera_times()
    for time in dados:
        jogos = time['vitorias'] + time['derrotas'] + time['empates']
        pontos = 3 * time['vitorias'] + time['empates']
        aprov = pontos / (jogos * 3.0)
        time['jogos'] = jogos
        time['pontos'] = pontos
        time['aproveitamento'] = aprov
        time['saldo'] = time['gols_pro'] - time['gols_contra']
    
    return dados