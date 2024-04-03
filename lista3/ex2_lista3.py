n = int(input("Informe a qtd de alunos: "))

while n <= 0:
    n = int(input("Valor inválido, digite novamente: "))

soma = 0
contador = 0

while contador < n:
    nota = float(input("Digite a nota: "))
    soma = soma + nota
    contador = contador + 1

media = soma / n
print(f"A média da turma vale {media}")    