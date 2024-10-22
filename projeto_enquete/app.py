import negocio

enq = negocio.recupera_enquete(3)

print(f"Enquete: {enq['nome']}")

for quest in enq['perguntas']:

    print(f"{quest['numero']}) {quest['texto']}")
    if quest['tipo'] != "aberta":

        for it in quest['opcoes']:
            print(f"{it['numero']} - {it['descricao']}")

    resp = input("Resp: ")