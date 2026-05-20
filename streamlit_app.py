import streamlit as st

# =========================================
# CONFIGURAÇÃO DA PÁGINA
# =========================================
st.set_page_config(
    page_title="Empresas Parceiras",
    page_icon="🌐",
    layout="wide"
)

# =========================================
# TÍTULO
# =========================================
st.title("🌎 Empresas Parceiras")
st.write("Confira algumas empresas incríveis abaixo.")

# =========================================
# COLUNAS
# =========================================
col1, col2, col3 = st.columns(3)

# =========================================
# EMPRESA 1
# =========================================
with col1:
    st.image("images.png", use_container_width=True)
    st.subheader("Amazon")
    st.write("Empresa de tecnologia e compras online líder.")
    st.link_button(
        "Acessar Site",
        "https://www.amazon.com"
    )

# =========================================
# EMPRESA 2
# =========================================
with col2:
    st.image("images (1).png", use_container_width=True)
    st.subheader("Microsoft")
    st.write("Empresa mundialmente conhecida pelo Windows.")
    st.link_button(
        "Acessar Site",
        "https://www.microsoft.com"
    )

# =========================================
# EMPRESA 3
# =========================================
with col3:
    st.image("images (2).png", use_container_width=True)
    st.subheader("Youtube")
    st.write("Plataforma líder de vídeos online.")
    st.link_button(
        "Acessar Site",
        "https://www.youtube.com"
    )

# =========================================
# RODAPÉ
# =========================================
st.write("---")
st.write("Desenvolvido por ALAN MIGUEL")
