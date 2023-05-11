import streamlit as st

def login():
    st.title("Bem vindo de Volta !")
    nome = st.text_input('Insira seu E-mail')
    senha = st.text_input('Insira a senha', type='password')
    situacao = 'Aprovado'
    retorne = [nome, senha, situacao]
    return retorne
    
 
