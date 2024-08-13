import busca_simples

#para cada valor da lista A:
#    faço uma busca do valor em resp
#    se valor nao esta em resp
#        adiciono valor em resp
#retorno resp

def elimina_repetidos(a):
    resp = []
    for valor in a:
        ret = busca_simples.busca(resp, valor)
        if ret == -1:
            resp.append(valor)
    return resp


lst = [2, 4, 9, 3, 4, 2, 1, 0, 6, 8]
ret = elimina_repetidos(lst)
print("Resposta: ", ret)