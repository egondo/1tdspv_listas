def aumento(valor, percentual):
    novo_valor = (1 + percentual/100) * valor
    #print(novo_valor) não recomendo usar o print como resultado da funcao
    return novo_valor

aux = aumento(1000, 15)
#posso escolher o que fazer com o aux: gravar em arquivo, gravar no banco de dados, mandar para um outro servidor, exibir na tela do meu celular ou do navegador web
print(aux)
