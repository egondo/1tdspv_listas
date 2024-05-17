import random

def cria(tipo):
    cartas = []
    for valor in range(1, 14):
        cartas.append( (valor, '♥') )
        cartas.append( (valor, '♠') )
        cartas.append( (valor, '♦') )
        cartas.append( (valor, '♣') )
    
    return cartas

def to_str(carta):
    if carta[0] == 1:
        return f"A{carta[1]}"
    elif carta[0] == 11:
        return f"J{carta[1]}"
    elif carta[0] == 12:
        return f"Q{carta[1]}"
    elif carta[0] == 13:
        return f"K{carta[1]}"
    else:
        return f"{carta[0]}{carta[1]}"

def compra(deck: list):
    if len(deck) > 0:
        return deck.pop()
    else:
        return None

def distribui(deck: list, qtd: int):
    mao = []
    if len(deck) >= qtd:
        while qtd > 0:
            mao.append(deck.pop())
            qtd = qtd - 1
    return mao

def embaralha(deck: list):
    tam = len(deck)
    for x in range(200):
        i = random.randint(0, tam - 1)
        j = random.randint(0, tam - 1)
        aux = deck[i]
        deck[i] = deck[j]
        deck[j] = aux    

def to_str_mao(hand: list):
    resp = ""
    for carta in hand:
        resp = resp + to_str(carta) + " "
    return resp


if __name__ == '__main__':
    monte = cria('normal')
    #for carta in monte:
    #    print(to_str(carta))
    embaralha(monte)
    mao_jogador = distribui(monte, 10)
    print(mao_jogador)
    carta = compra(monte)
    while carta != None:
        print(to_str(carta))
        carta = compra(monte)

