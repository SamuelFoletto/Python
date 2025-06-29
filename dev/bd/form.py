import streamlit as st
import dados

st.title("Filmes")

nome = st.text_input('Nome do filme:')

ano = st.number_input('Ano do filme:', min_value=2000, max_value=2025)

nota = st.slider('Nota do filme:', min_value=0.0, max_value=10.0 )


if st.button('Adicionar'):
    dados.insere_dados(nome, ano, nota)
    st.success("Filme cadastrado")


filmes = dados.listar_dados()
st.header("Lista de filmes")
st.table(filmes)