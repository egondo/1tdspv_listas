def inverte_dicionario(dic: dict) -> dict:
    dic_inv = {}

    for chave in dic.keys():
        valor = dic.get(chave)
        dic_inv[valor] = chave
    
    return dic_inv

if __name__ == "__main__":
    ing_port = {'house': 'casa', 'street': 'rua',
                'gold': 'ouro', 'mall': 'shopping'}
    
    port_ing = inverte_dicionario(ing_port)
    print(port_ing)