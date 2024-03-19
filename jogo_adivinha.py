#O jogo sorteia um número aleatório entre 1 e 1000 e o usuário
#tem 10 chances para encontrar o número sorteado. 
#A cada tentativa fracassada de acerto, o jogo fala se o número sorteado
#é maior ou menor do que o número "chutado". Faça a implementação desse jogo
#usando Python.

import random

num = random.randint(1, 1000)
#print(num)

chute = int(input("Tentativa: "))
if chute < num:
    print("Tente um número maior!")
elif chute > num:
    print("Tente um número menor!")
else:
    print("Acertou na 1 tentativa")
    exit()


chute = int(input("Tentativa: "))
if chute < num:
    print("Tente um número maior!")
elif chute > num:
    print("Tente um número menor!")
else:
    print("Acertou na 2 tentativa")
    exit()

chute = int(input("Tentativa: "))
if chute < num:
    print("Tente um número maior!")
elif chute > num:
    print("Tente um número menor!")
else:
    print("Acertou na 3 tentativa")
    exit()

chute = int(input("Tentativa: "))
if chute < num:
    print("Tente um número maior!")
elif chute > num:
    print("Tente um número menor!")
else:
    print("Acertou na 4 tentativa")
    exit()

chute = int(input("Tentativa: "))
if chute < num:
    print("Tente um número maior!")
elif chute > num:
    print("Tente um número menor!")
else:
    print("Acertou na 5 tentativa")
    exit()

chute = int(input("Tentativa: "))
if chute < num:
    print("Tente um número maior!")
elif chute > num:
    print("Tente um número menor!")
else:
    print("Acertou na 6 tentativa")
    exit()

chute = int(input("Tentativa: "))
if chute < num:
    print("Tente um número maior!")
elif chute > num:
    print("Tente um número menor!")
else:
    print("Acertou na 7 tentativa")
    exit()

chute = int(input("Tentativa: "))
if chute < num:
    print("Tente um número maior!")
elif chute > num:
    print("Tente um número menor!")
else:
    print("Acertou na 8 tentativa")
    exit()

chute = int(input("Tentativa: "))
if chute < num:
    print("Tente um número maior!")
elif chute > num:
    print("Tente um número menor!")
else:
    print("Acertou na 9 tentativa")
    exit()

chute = int(input("Tentativa: "))
if chute < num:
    print("Tente um número maior!")
elif chute > num:
    print("Tente um número menor!")
else:
    print("Acertou na 10 tentativa")
    exit()

print("O numero sorteado era", num)


