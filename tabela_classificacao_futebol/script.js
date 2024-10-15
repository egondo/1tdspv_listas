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

const cadastra = () => {
    cmp_visi = document.querySelector('[name="visi"]')
    cmp_gv = document.querySelector('[name="gv"]')
    cmp_casa = document.querySelector('[name="casa"]')
    cmp_gc = document.querySelector('[name="gc"]')

    dado = {casa: cmp_casa.value, visi: cmp_visi.value,
        gc: parseInt(cmp_gc.value), gv: parseInt(cmp_gv.value),
        rodada: 3}
    fetch("http://127.0.0.1:5000/partidas", {
        method: "POST",
        body: JSON.stringify(dado),
        headers: {"Content-Type": "application/json"}
    })
        .then(resp => resp.json())
        .then(data => console.log(data))
}
botao_cadastra = document.querySelector('[name="cadastra"]')
botao_cadastra.addEventListener("click", cadastra)

botao_times = document.querySelector('[name="times"]')
botao_times.addEventListener("click", consulta)


