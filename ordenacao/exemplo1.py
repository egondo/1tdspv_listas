def esta_ordenada(lst):
    i = 0
    while i < len(lst) - 1:
        if lst[i] > lst[i+1]:
            return False
        i = i + 1
    return True

if __name__ == '__main__':
    conj = [2, 5, 7, 7, 10, 12, 15]
    resp = esta_ordenada(conj)
    print(resp)