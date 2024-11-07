#pip install pandas
#pip install matplotlib
#pip install streamlit

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt 

st.set_page_config(layout="wide")
st.header("Dashboard Faturamento")

arquivo = st.file_uploader("Faturamento")

if arquivo:
    df = pd.read_csv(arquivo, sep=";")

    df['total'] = df['quantidade'] * df['valor']
    df['mes'] = df['data'].apply(lambda y: int(y.split("/")[1]))

    df_agrupado = pd.pivot_table(df, index="mes", columns="loja", aggfunc="sum", values="total")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.dataframe(df_agrupado)

    with col2:
        st.bar_chart(df_agrupado)

    with col3:
        st.bar_chart(df_agrupado, stack=False)
        
    lista_produtos = df['produto'].unique()

    prod_select = st.selectbox("Produto", options=lista_produtos)

    if prod_select:
        df_produto = df.query(f"produto == '{prod_select}'")
        df_produto_agregado = pd.pivot_table(df_produto, index="marca", columns="mes", aggfunc="sum", values="total")

        df_produto_graf = pd.pivot_table(df_produto, index="mes", columns="marca", aggfunc="sum", values="total")

        st.bar_chart(df_produto_graf, stack=False)
        st.dataframe(df_produto_agregado)
        
        
        #fig = plt.figure() 
        #plt.plot(df_produto_graf)
        #st.pyplot(fig) 
        