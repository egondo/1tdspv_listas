acertou_input = False
while not acertou_input:
    try:
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        salario = float(input("Salário: "))
    except ValueError:
        print("Entrada invalida!")
    else:
        acertou_input = True

