#pedir para o usuario digitar o raio

aux = input("Informe o raio do círculo: ")
raio = float(aux)

area = raio * raio * 3.1415
perimetro = 2 * raio * 3.1415

print("A área vale", area)
print("O perimetro vale", perimetro)

print(f"A área vale {area:.3f}")
print(f"O perímetro vale {perimetro:.3f}")

