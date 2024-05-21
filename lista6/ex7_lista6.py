def monta_duplas(nome, tuplas, pos):
    while pos < len(tuplas):
        print(nome, tuplas[pos])
        pos = pos + 1

pessoas = ("Ana", "Bia", "Celi", "Dora", "Elsa", "Fabi", "Gabi", "Helo")

for j in range(0, len(pessoas)):
    monta_duplas(pessoas[j], pessoas, j+1)


