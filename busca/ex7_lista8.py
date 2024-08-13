def busca_todos(conj: list, valor: object) -> list:
    resp = []
    i = 0
    while i < len(conj):
        if conj[i] == valor:
            resp.append(i)
        i = i + 1
    return resp

if __name__ == '__main__':
    lst = [2, 4, 6, 0, 4, 0, 7, 2, 1, 5]
    resp = busca_todos(lst, 6)
    print(resp)