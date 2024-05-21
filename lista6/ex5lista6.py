def maior(dados: tuple):
    aux_maior = dados[0]
    for i in range(1, len(dados)):
        if len(aux_maior) < len(dados[i]):
            aux_maior = dados[i]
    return aux_maior


conj = ("Computational Thinking", "Building Relational Database", 
        "Domain Driven Design", "Front End Interfaces", 
        "Software Engineering")

disciplina = maior(conj)
print(disciplina)

