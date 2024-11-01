import streamlit as st

with st.form("form"):
    nome = st.text_input("Nome:")
    sobrenome = st.text_input("Sobrenome: ")

    botao = st.form_submit_button("Cadastra")

    if botao:
        st.markdown(nome + " " + sobrenome)