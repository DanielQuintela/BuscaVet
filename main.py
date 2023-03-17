import pandas as pd
import streamlit as st
import sqlite3

con = sqlite3.connect('banco_programa.db')
cursor = con.cursor()


# cadastro de pesquisador, inicialmente chamado no código de user

def create_usertable():
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS usuario(email TEXT, nome TEXT,senha TEXT, cpf NUMERIC UNIQUE)')


def add_user(nome, email,senha,cpf, telefone):
    situacao = "Aprovado"
    cursor.execute('INSERT INTO usuario(nome,email,senha,cpf,telefone) VALUES (?,?,?,?,?)',
                   (nome, email,senha,cpf, telefone))
    con.commit()

def add_uservet(nome, email,senha,cpf,identificacao,telefone):
    situacao = "Aprovado"
    cursor.execute('INSERT INTO veterinario(nome,email,senha,cpf,identificacao,telefone) VALUES (?,?,?,?,?,?)',
                   (nome, email,senha,cpf,identificacao, telefone))
    con.commit()


def login_user(email, senha):
    cursor.execute('SELECT * FROM usuario WHERE email = ? AND senha = ?', (email, senha))
    data = cursor.fetchall()
    return data


def get_name(email):
    cursor.execute('SELECT nome FROM usuario WHERE email = ?', (email,))
    data = cursor.fetchall()
    return str(data[0][0]) if data else None


paginaSelecionada = st.sidebar.selectbox('Selecione o caminho',
                                         ['Tela de inicio', 'Login e/ou Cadastro'])

if paginaSelecionada == 'Tela de inicio':
    st.title('Tela principal')
    st.text('Em construção 🏗')



elif paginaSelecionada == 'Login e/ou Cadastro':
    usuario = st.sidebar.selectbox('', ['Login', 'Cadastro'])

    if usuario == 'Cadastro':
        st.title('Cadastro de usuário')
        escolha = st.selectbox('', ['Cliente', 'Veterinário'])
        if escolha == "Cliente":
            input_name = st.text_input(label='Insira o seu nome completo')
            input_email = st.text_input(label='Insira o seu email')
            input_senha = st.text_input(label='Insira a senha', type="password")
            input_cpf = st.text_input(label='Insira o seu CPF')
            input_telefone = st.text_input(label='Insira o seu telefone')

            if st.button("Enviar Dados"):
                add_user(input_name, input_email, input_senha, input_cpf, input_telefone)
                st.success('Adicionado com sucesso !!')
                st.info("Vá para o menu de login!!")

        if escolha == "Veterinário":
            input_name = st.text_input(label='Insira o seu nome completo')
            input_email = st.text_input(label='Insira o seu email')
            input_senha = st.text_input(label='Insira a senha', type="password")
            input_cpf = st.text_input(label='Insira o seu CPF')
            input_vet = st.text_input(label='Insira a sua identificacao')
            input_telefone = st.text_input(label='Insira o seu telefone')

            if st.button("Enviar Dados"):
                add_uservet(input_name,input_email,input_senha,input_cpf, input_vet,input_telefone)
                st.success('Adicionado com sucesso !!')
                st.info("Vá para o menu de login!!")

    if usuario == 'Login':
        nome = st.sidebar.text_input('Insira seu E-mail')
        senha = st.sidebar.text_input('Insira a senha', type='password')
        if st.sidebar.checkbox('Login'):
            # if input_senha_func == '1234':
            create_usertable()
            result = login_user(nome, senha)
            result2 = login_secretaria(nome, senha)
            if result:
                nome2 = get_name(nome)
                st.sidebar.title(f"Logado como: {nome2}")
                st.title(f'Bem vindo de Volta {nome2}')
                area_pesq = st.selectbox('Selecione o que deseja', ['Inicio'])
                if area_pesq == 'Inicio':
                    st.title('Página inicial do pesquisador')
                    st.text('Selecione uma opção acima para começar os trabalhos !!')

            elif result2:
                st.sidebar.title('Secretária logada')
                st.title("Área da Secretária")


            else:
                st.warning("Usuário incorreto ou Inexistente")
