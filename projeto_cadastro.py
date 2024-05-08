def adiciona(lista, nome, cpf, tel, nasc):
    lista.append(nome)
    lista.append(cpf)
    lista.append(tel)
    lista.append(nasc)

banco_dados = []
resp = "s"
while resp != 'n':
    nome = input("Nome: ")
    cpf = input("CPF: ")
    telefone = input("Tel: ")
    nascimento = input("Nascimento: ")
    resp = input("Deseja inserir mais alguém (s/n): ")
    adiciona(banco_dados, nome, cpf, telefone, nascimento)
    print(banco_dados)

banco_dados = ['Sueli', '23423', '(11) 32423', '02/09/2000', 'Manoel', '2344543', '(11) 934320', '16/10/1989', 'Maria', '324923', '335443', '14/1/2001']
i = 0
while i < len(banco_dados):
    print(f"{i} - {banco_dados[i]}: {banco_dados[i + 3]}")
    i = i + 4

resp = int(input("Qual pessoa deseja alterar: "))

nome = input(f"Nome ({banco_dados[resp]}): ")
if len(nome) > 0:
    banco_dados[resp] = nome

cpf = input(f"CPF ({banco_dados[resp + 1]}): ")
if len(cpf) > 0:
    banco_dados[resp + 1] = cpf

tel = input(f"Tel ({banco_dados[resp + 2]}): ")
if len(tel) > 0:
    banco_dados[resp + 2] = tel

nasc = input(f"Nascimento ({banco_dados[resp + 3]}): ")
if len(nasc) > 0:
    banco_dados[resp + 3] = nasc

print(banco_dados)