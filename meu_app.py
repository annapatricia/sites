import streamlit as st
import pandas as pd
st.set_page_config(page_title="Meu Site Streamlit")
with st.container():
    st.write("meu primeiro site com streamlit")
    st.subheader("olha garoto esta começando a sair")
    #st.title("Dashboard de contratos")
    # Centralizando o título
    st.markdown("<h1 style='text-align: center;'>Dashboard de contratos</h1>", unsafe_allow_html=True)
    st.write('Iformaçoes sobre os contratos fechados no mes de maio') 
    st.write("quer aprender python?[clique aqui](https://www.hashtagtreinamentos.com/)")
with st.container():
    st.write("---")  
    dados=pd.read_csv("resultados.csv")
    st.area_chart(dados, x="Data",y="Contratos")



              

