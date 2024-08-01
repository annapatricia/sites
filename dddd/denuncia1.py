import streamlit as st
from PIL import Image, ImageDraw

# Coluna do meio - Adicionando o formulário de ouvidoria
with st.container():
    st.markdown('<h1 style="color: blue;">Canal de Ouvidoria e Denúncias</h1>', unsafe_allow_html=True)
    nome = st.text_input('Seu Nome')
    email = st.text_input('Seu Email')
    mensagem = st.text_area('Sua Mensagem')

    if st.button('Enviar'):
        st.write(f'Mensagem enviada por {nome} ({email}): {mensagem}')

    # Gerando link para enviar pelo WhatsApp
    if st.button('Enviar pelo WhatsApp'):
        whatsapp_url = f"https://wa.me/?text=Nome: {nome}%0AEmail: {email}%0AMensagem: {mensagem}"
        st.markdown(f'[Clique aqui para enviar pelo WhatsApp]({whatsapp_url})')

