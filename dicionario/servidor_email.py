def cadastra(correio: dict):
    login = input("Informe o login: ")
    if not login in correio:
        msg = {"assunto": "Bem vindo ao 1tdspv", "from": "admin", "msg": ""}
        correio[login] = [msg]
    else:
        print("Ja existe este login!")

def envia(correio: dict):
    login = input("Informe o login: ")
    if login in correio:
        sub = input("Assunto: ")
        de = input("Remetente: ")
        msg = input("Mensagem: ")
        registro = {"assunto": sub, "from": de, "msg": msg}
        lista_msgs = correio[login]
        lista_msgs.append(registro)
    else:
        print(f"{login} não encontrado!")


def le(correio: dict):
    login = input("Login:")
    if login in correio:
        lista_msgs = correio[login]
        for msg in lista_msgs:
            print(msg)
    else:
        print(f"{login} não encontrado")


escaninho = {}

opcao = 0
while opcao != 4:
    print("1 - cadastra")
    print("2 - envia email")
    print("3 - lê mensagens")
    print("4 - sair")
    opcao = int(input("Digite: "))
    if opcao == 1:
        cadastra(escaninho)
    elif opcao == 2:
        envia(escaninho)
    elif opcao == 3:
        le(escaninho)
    