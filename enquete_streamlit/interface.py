'''
pip install streamlit ou pip3 install streamlit
'''

import streamlit as st
import requests

st.write("Olá mundo!")

col1, col2 = st.columns(2)
with col1:
    botao = st.button("clique")

with col2:
    if botao:
        st.write("Vc clicou no botao")
