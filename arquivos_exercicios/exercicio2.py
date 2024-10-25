import oracledb

'''
select mes, loja, sum(faturamento) from 
        (select to_char(data, 'MM') as mes, loja, quantidade*valor as faturamento from tbv_faturamento)
    group by mes, loja order by mes
'''

def grava_faturamento_oracle(lista: list):
    con = oracledb.connect(user="pf0313", password="professor#23",
                            dsn="oracle.fiap.com.br/orcl")
    cur = con.cursor()
    sql = "insert into tbv_faturamento(produto, marca, loja, data, quantidade, valor) values    (:produto, :marca, :loja, to_date(:data, 'DD/MM/YYYY'), :qtd, :valor)"

    #for info in lista:
    #    cur.execute(sql, info)

    cur.executemany(sql, lista)

    cur.close()
    con.commit()
    con.close()


if __name__ == "__main__":

    with open("faturamento_anual.txt", mode="r") as arq:
        lista = arq.readlines()

    #print(lista)
    registros = []
    for linha in lista:
        reg = linha.split(";")
        #print(reg)
        dado = {"produto": reg[0], "marca": reg[1], "loja": reg[2],
                "data": reg[3], "qtd": int(reg[4]), "valor": float(reg[5])}
        registros.append(dado)
    
    grava_faturamento_oracle(registros)