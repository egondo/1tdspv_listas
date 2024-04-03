candidatos = 20

conta20 = 0
conta21a50 = 0
conta50 = 0

nota = int(input("Digite a pontuação do candidato: "))
contador = 1
maior_nota = nota
menor_nota = nota
if nota <= 20:
    conta20 = conta20 + 1
elif nota <= 50:
    conta21a50 = conta21a50 + 1
else:
    conta50 = conta50 + 1

while contador < candidatos:
    nota = int(input("Digite a pontuação do candidato: "))
    if nota > maior_nota:
        maior_nota = nota
    if nota < menor_nota:
        menor_nota = nota
    
    if nota <= 20:
        conta20 = conta20 + 1
    elif nota <= 50:
        conta21a50 = conta21a50 + 1
    else:
        conta50 = conta50 + 1
    
    contador = contador + 1

print(f"A maior nota foi {maior_nota} e a menor foi {menor_nota}")
print(f"Até 20 acertos {conta20 * 100 / candidatos}%")
print(f"De 21 a 50 acertos {conta21a50 * 100 / candidatos}%")
print(f"Acima de 50 acertos {conta50 * 100 / candidatos}%")