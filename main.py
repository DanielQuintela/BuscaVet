import pandas as pd
import streamlit as st
import sqlite3
import Banco.banco_dados as Banco
import Page.cadastro as PageCadastro , Page.usuario as PageUsuario, Page.veterinario as PageVeterinario, Page.adm as PageAdm
from sqlite3 import Error

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect('./Banco/banco_programa.db')
        print(f"Conexão com o banco de dados estabelecida: {sqlite3.version}")
        return conn
    except Error as e:
        print(e)



with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

paginaSelecionada = st.sidebar.selectbox('Selecione o caminho',
                                         ['Tela de inicio', 'Login e/ou Cadastro'])

if paginaSelecionada == 'Tela de inicio':
    st.title('Tela principal')
    st.text('Em construção 🏗')
    st.text('Abaixo uma demonstração de edição com css')
    
    
elif paginaSelecionada == 'Login e/ou Cadastro':
    st.sidebar.title("Seja Bem vindo !")
    funcionarios = st.sidebar.selectbox('Selecione a Opção', ['Login', 'Cadastro'])

    if funcionarios == 'Cadastro':
        PageCadastro.Cadastro()
                        

    if funcionarios == 'Login':
        nome = st.sidebar.text_input('Insira seu E-mail')
        senha = st.sidebar.text_input('Insira a senha', type='password')
        situacao = 'Aprovado'
        if st.sidebar.checkbox('Login'):
            # if input_senha_func == '1234':

            Banco.create_usertable()
            Banco.create_veterinario()
            Banco.criar_clinica()
            user = Banco.login_user(nome, senha)
            vet = Banco.login_veterinario(nome, senha, situacao)

            clinica = ('nome','senha')
            if user:
                PageUsuario.Usuario(nome)
               
            elif vet:
                PageVeterinario.Veterinario(nome)
        
                

            elif senha == '0809':
                PageAdm.Adm()
                            
                
            else:
                st.warning("Usuário incorreto ou Inexistente")
    
    
