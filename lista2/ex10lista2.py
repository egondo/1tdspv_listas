import math

a = float(input("A: "))
b = float(input("B: "))
c = float(input("C: "))

delta = b * b - 4 * a * c

if delta < 0:
    print(f"Equação {a}x^2 + {b}x + {c} não possui raízes reais")
else:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print(f"As raízes da equação são {x1} e {x2}")
    