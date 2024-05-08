n = int(input("Informe a qtd de alunos: "))
soma = 0
lista_notas = []

i = 0
while i < n:
    nota = float(input("Informe a nota do aluno: "))
    lista_notas.append(nota)
    soma = soma + nota
    i = i + 1

media = soma / n
print(f"A media da turma foi de {media}")
#print(lista_notas)
acima = 0
abaixo = 0

for nota in lista_notas:
    if nota < media:
        abaixo = abaixo + 1
    else:
        acima = acima + 1

print(f"A qtd de alunos abaixo da média é de {abaixo}")
print(f"A qtd de alunos acima da média é de {acima}")        
