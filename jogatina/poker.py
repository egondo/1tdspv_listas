#criar o baralho, misturar, distribuir duas cartas para
#dois jogadores e abriremos 5 cartas na mesa.

import baralho

monte = baralho.cria('normal')

baralho.embaralha(monte)

mao_jogador1 = baralho.distribui(monte, 2)
mao_jogador2 = baralho.distribui(monte, 2)

mesa = baralho.distribui(monte, 5)

print("Jogador 1")
print(baralho.to_str_mao(mao_jogador1))

print("Mesa: ")
print(baralho.to_str_mao(mesa))

print("Jogador 2")
print(baralho.to_str_mao(mao_jogador2))
