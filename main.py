import streamlit as st
st.set_page_config(page_title='BuscaVet', page_icon=':mag:')
import pandas as pd
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


if 'login' not in st.session_state:
    st.session_state.login = False

def aprovar():
    st.session_state.login = True
    return st.session_state.login

def fechar():
    st.session_state.login = False


start = st.sidebar.empty()

paginaSelecionada = start.selectbox('Selecione o caminho',
                                         ['Tela de inicio', 'Login e/ou Cadastro'], key='selectbox3')

if paginaSelecionada == 'Tela de inicio':
    st.title('Tela principal')
    st.text('Em construção 🏗')
   
    
    
    
elif paginaSelecionada == 'Login e/ou Cadastro':
    title = st.empty()
    titulo = title.title("Seja Bem vindo a Tela de Cadastro !")
    selectbox_placeholder = st.sidebar.empty()
    nome_place = st.empty()
    senha_place = st.empty()
    checkbox_placeholder = st.empty()
    escolha = selectbox_placeholder.selectbox('Selecione a Opção', ['Login', 'Cadastro'])

    if escolha == 'Cadastro':
        PageCadastro.Cadastro()
   
                        

    if escolha == 'Login':
        titulo = title.title("Bem vindo de Volta !")
        nome = nome_place.text_input('Insira seu E-mail')
        senha = senha_place.text_input('Insira a senha', type='password')
        situacao = 'Aprovado'
        marcado = checkbox_placeholder.button('Login')

        if marcado:
            aprovar()

        if st.session_state.login:    
            # if input_senha_func == '1234':
            Banco.create_usertable()
            Banco.create_veterinario()
            Banco.criar_clinica()
            user = Banco.login_user(nome, senha)
            vet = Banco.login_veterinario(nome, senha, situacao)
            #clinica = Banco.login_clinica(nome, senha, situacao)
            

            if user:
                start.empty()
                title.empty()
                selectbox_placeholder.empty()
                nome_place.empty()
                senha_place.empty()
                checkbox_placeholder.empty()

                Page = PageUsuario.Usuario(nome)

               
            elif vet:
                start.empty()
                title.empty()
                selectbox_placeholder.empty()
                nome_place.empty()
                senha_place.empty()
                checkbox_placeholder.empty()

                PageVeterinario.Veterinario(nome)


            elif senha == '0809':
                start.empty()
                title.empty()
                
                nome_place.empty()
                senha_place.empty()
                checkbox_placeholder.empty()
                PageAdm.Adm()
                            
                
            else:
                st.warning("Usuário incorreto ou Inexistente")
    
   
