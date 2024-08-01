import streamlit as st
from PIL import Image, ImageDraw

# Configurando o layout com três colunas
col1, col2, col3 = st.columns(3)

# Coluna da esquerda - Adicionando uma figura
with col1:
    st.header("Figura")
    img = Image.new('RGB', (200, 200), color='blue')
    st.image(img, caption='Figura Azul', use_column_width=True)

# Coluna do meio - Adicionando o formulário de ouvidoria
with col2:
    st.title('Canal de Ouvidoria e Denúncias')
    nome = st.text_input('Seu Nome')
    email = st.text_input('Seu Email')
    mensagem = st.text_area('Sua Mensagem')

    if st.button('Enviar'):
        st.write(f'Mensagem enviada por {nome} ({email}): {mensagem}')

# Coluna da direita - Adicionando um quadrado e um círculo amarelo
with col3:
    st.header("Formas")
    
    # Desenhando o quadrado amarelo
    img_square = Image.new('RGB', (200, 200), color='white')
    draw = ImageDraw.Draw(img_square)
    draw.rectangle([50, 50, 150, 150], fill='yellow')
    st.image(img_square, caption='Quadrado Amarelo', use_column_width=True)

    # Desenhando o círculo amarelo
    img_circle = Image.new('RGB', (200, 200), color='white')
    draw = ImageDraw.Draw(img_circle)
    draw.ellipse([50, 50, 150, 150], fill='yellow')
    st.image(img_circle, caption='Círculo Amarelo', use_column_width=True)