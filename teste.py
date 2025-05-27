import streamlit as st

st.title("Meu Primeiro Site com Streamlit")
st.write("esse é um site simples feito com Python e Streamlit!")

nome = st.text_input("Digite seu nome:")

if st.button("Enviar"):
    st.success(f"Olá, {nome}! Seja bem-vindo ao meu site 😊")
