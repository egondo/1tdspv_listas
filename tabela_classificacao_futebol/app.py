import negocio

if __name__ == '__main__':
    partida = {'casa': 'Penarol', 'visi': 'Atlético Mineiro', 'gc': 1, 'gv': 3, 'rodada': 1}
    
    negocio.cadastra_partida(partida)

    partida = {'visi': 'Penarol', 'casa': 'Atlético Mineiro', 'gc': 2, 'gv': 0, 'rodada': 2}
    negocio.cadastra_partida(partida)
    