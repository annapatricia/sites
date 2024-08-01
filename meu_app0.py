import streamlit as st
import pandas as pd
st.set_page_config(page_title="Meu Site Streamlit")
with st.container():
    st.write("meu primeiro site com streamlit")
    st.subheader("olha garoto esta começando a sair")
    st.title("Dashboard de contratos")
    st.write('Iformaçoes sobre os contratos fechados no mes de maio') 
    st.write("quer aprender python?[clique aqui](https://www.hashtagtreinamentos.com/)")

@st.cache_data
def carregar_dados():
    tabela=pd.read_csv("resultados.csv")
    return tabela

with st.container():

    st.write("---")  
    
    qtde_dias=st.selectbox("Selecione o periodo",["7D","15D","21D","30D"])
    num_dias=int(qtde_dias.replace("D",""))
    dados=carregar_dados()
    dados=dados[-num_dias:]
    st.area_chart(dados, x="Data",y="Contratos")

