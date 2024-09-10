try:
    a = int(input("A: "))
    b = int(input("B: "))
    result = a / b
except ZeroDivisionError:
    print("Impossivel fazer divisao por 0")
else: 
    print(result)
