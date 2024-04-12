opcao = 0

while opcao != 6:
    print("Locadora FIAP")
    print("1 - Alugar carro\n2 - Cadastra cliente")
    print("3 - Consulta carro\n4 - Análise de crédito")
    print("5 - Fale conosco\n6 - Sair")
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        cpf = int(input("Informe o CPF: "))
        categoria = input("Informe a categoria (básico, premium e luxo): ")
        print("cod: 239 BMW 2020 R$ 500,00")
        print("cod: 267 M Benz 2022 R$ 580,00")
        print("cod: 284 Audi Q3 R$ 420,00")
        codigo = int(input("Escolha o carro: "))
        dias = int(input("Informe a qtd de dias: "))
        print(f"Você alugou uma q3 e vai pagar {dias * 420}")
    elif opcao == 2:
        pass
    elif opcao == 3:
        pass
    elif opcao == 4:
        pass
    elif opcao == 5:
        email = input("Informe o email: ")
        pergunta = input("Pergunta/dúvida: ")
        print("Mais tarde entraremos em contato ou responderemos sua pergunta!")
    elif opcao == 6:
        print("Obrigado por usar nosso sistema!")
    else:
        print("Opção inválida!")
    
