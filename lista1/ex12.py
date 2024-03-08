#Soma dos digitos de um RM

soma = 0

rm = int(input("Informe o RM: "))

dig = rm % 10
soma = soma + dig   #soma += dig
rm = rm // 10

dig = rm % 10
soma = soma + dig
rm = rm // 10

dig = rm % 10
soma = soma + dig
rm = rm // 10

dig = rm % 10
soma = soma + dig
rm = rm // 10

dig = rm % 10
soma = soma + dig
rm = rm // 10

print(f"A soma dos digitos vale {soma}")


