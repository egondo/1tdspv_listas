const consulta = () => {
    fetch("http://127.0.0.1:5000/times").
        then(response => response.json()).
        then(data => {
            var tab = "<table><tr><td>Nome<td>Jogos<td>PG<td>Aprov"
            data.forEach(element => {
                tab = tab + "<tr><td>" + element.nome 
                tab = tab + "<td>" + element.jogos
                tab = tab + "<td>" + element.pontos
                tab = tab + "<td>" + element.aproveitamento
            });
            tab = tab + "</table>"
            document.querySelector("#tabela").innerHTML = tab
        })
}

botao_times = document.querySelector('[name="times"]')
botao_times.addEventListener("click", consulta)

botao_cadastra = document.querySelector('[name="cadastra"]')

