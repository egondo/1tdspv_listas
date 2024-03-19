num_a = float(input("Digite a: "))
op = input("Operador: ")
num_b = float(input("Digite b: "))

if op == '+':
    result = num_a + num_b
elif op == '-':
    result = num_a - num_b
elif op == '*':
    result = num_a * num_b
elif op == '/':
    if num_b != 0:
        result = num_a / num_b
    else:
        print("Não é possível dividir por 0")
        #poderia encerrar o programa
        exit()
else:
    print("operador invalido")
    #poderia encerrar o programa
    quit()
    
print(f"O resultado vale {result}")