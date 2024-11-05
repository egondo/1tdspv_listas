import streamlit as st
import requests


st.set_page_config(layout="wide")

st.markdown("Projeto Enquete")

lista = requests.get("http://127.0.0.1:5000/enquetes")

if lista.status_code == 200:
    #st.write(lista.json())
    enquetes = lista.json()
    aux = []
    for e in enquetes:
        aux.append(e['nome'])

    nome_enquete = st.selectbox("Enquete", options=aux, index=None)

    resposta = requests.get("http://127.0.0.1:5000/enquetes/3")
    
    with st.form("form"):
        enq_select = resposta.json()

        resp = [''] * len(enq_select['perguntas'])
        i = 0
        for quest in enq_select['perguntas']:
            enunciado = f"{quest['numero']} - {quest['texto']}"
            
            if quest['tipo'] == "aberta":
                resp[i] = st.text_input(enunciado)
            elif quest['tipo'] == "escolha única":
                opcoes = []

                for op in quest['opcoes']:
                    opcoes.append(op['descricao'])
                resp[i] = st.radio(enunciado, options=opcoes, index=None)
            i = i + 1
        submit = st.form_submit_button("envia")
        
        if submit:
            respostas_dict = []
            i = 0
            while i < len(resp):
                quest = enq_select['perguntas'][i]
                respostas_dict.append({"valor": resp[i], "numero": quest['numero'], "id_pergunta": quest['id']})
                i = i + 1
            
            retorno = requests.post("http://127.0.0.1:5000/respostas", json=respostas_dict)

            if retorno.status_code == 200:
                st.write("Respostas gravadas com sucesso!")
            else:
                st.write(retorno.json())    
