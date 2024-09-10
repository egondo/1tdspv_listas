def divisao(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Divisao por 0")
    return a / b

if __name__ == "__main__":
    try:
        x = float(input("X: "))
        y = float(input("Y: "))

        result = divisao(x, y)
    except ZeroDivisionError as e:
        print(e)
    else:
        print("Resultado: ", result)