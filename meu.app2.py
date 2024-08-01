import streamlit as st
import pandas as pd
st.set_page_config(page_title="ideias minhas")


with st.container():
    st.title('Canal de Ouvidoria e Denúncias')

nome = st.text_input('Seu Nome')
email = st.text_input('Seu Email')
mensagem = st.text_area('Sua Mensagem')

if st.button('Enviar'):
    st.write(f'Mensagem enviada por {nome} ({email}): {mensagem}')
    
        
    
