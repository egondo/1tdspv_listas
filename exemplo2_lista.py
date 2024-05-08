def maior_menor(conjunto):
    max = conjunto[0]
    min = conjunto[0]

    i = 1
    while i < len(conjunto):
        if conjunto[i] > max:
            max = conjunto[i]
        if conjunto[i] < min:
            min = conjunto[i]
        i = i + 1
    return (min, max)

lst = [7, 10, -1, 4, 6, 18, 0, 9, 8]
resp = maior_menor(lst)
print(resp)
print(lst)
