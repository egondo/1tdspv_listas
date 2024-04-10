dec = int(input("Informe o numero: "))

resp = ""

while dec > 0:
    res = dec % 2
    resp = str(res) + resp
    dec = dec // 2

print(f"Binário: {resp}")


