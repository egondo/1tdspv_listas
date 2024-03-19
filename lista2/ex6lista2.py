a = int(input("Informe o número A: "))
b = int(input("Informe o número B: "))

if b != 0:
	if a % b == 0:
		print(f"{a} é divisível por {b}")
	else:
		print(f"{a} não é divisível por {b}")	
else:
	print("Impossível efetuar a divisão!")

	