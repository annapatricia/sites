import streamlit as st

# Configurando a navegação na parte superior
st.markdown("""
<nav style="display: flex; justify-content: center; background-color: #f2f2f2; padding: 10px;">
    <ul style="list-style-type: none; display: flex; justify-content: center; margin: 0; padding: 0;">
        <li style="margin-right: 20px;"><a href="#home" style="text-decoration: none; color: black; font-size: 20px;">Home</a></li>
        <li style="margin-right: 20px;"><a href="#sobre-nos" style="text-decoration: none; color: black; font-size: 20px;">Sobre Nós</a></li>
        <li><a href="#denuncia" style="text-decoration: none; color: black; font-size: 20px;">Denúncia</a></li>
    </ul>
</nav>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# Seção Home
st.markdown('<h2 id="home" style="text-align: center;">Home</h2>', unsafe_allow_html=True)
st.write("<p style='text-align: center;'>Bem-vindo ao nosso canal de ouvidoria e denúncias. Este é o local onde você pode expressar suas preocupações e enviar denúncias de forma segura e confidencial.</p>", unsafe_allow_html=True)

# Seção Sobre Nós
st.markdown('<h2 id="sobre-nos" style="text-align: center;">Sobre Nós</h2>', unsafe_allow_html=True)
st.write("<p style='text-align: center;'>Nós somos uma instituição dedicada a garantir a segurança e bem-estar de nossa comunidade. Nossa missão é ouvir e agir conforme as necessidades de nossos membros.</p>", unsafe_allow_html=True)

# Seção Denúncia
st.markdown('<h2 id="denuncia" style="text-align: center;">Denúncia</h2>', unsafe_allow_html=True)

# Adicionando o formulário de ouvidoria
st.markdown('<h3 style="color: blue; text-align: center;">Canal de Ouvidoria e Denúncias</h3>', unsafe_allow_html=True)
nome = st.text_input('Seu Nome')
email = st.text_input('Seu Email')
mensagem = st.text_area('Sua Mensagem')

if st.button('Enviarrrr'):
    st.write(f'Mensagem enviada por {nome} ({email}): {mensagem}')

# Gerando link para enviar pelo WhatsApp
if st.button('Enviar pelo WhatsApp'):
    whatsapp_url = f"https://wa.me/?text=Nome: {nome}%0AEmail: {email}%0AMensagem: {mensagem}"
    st.markdown(f'[Clique aqui para enviar pelo WhatsApp]({whatsapp_url})')
    