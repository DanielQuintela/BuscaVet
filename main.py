import pandas as pd
import streamlit as st
import sqlite3

con = sqlite3.connect('banco_programa.db')
cursor = con.cursor()

# cadastro de pesquisador, inicialmente chamado no código de user

def create_usertable():
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS usuario(email TEXT, nome TEXT,senha TEXT, cpf NUMERIC UNIQUE)')

def add_userdata(email, nome, senha, cpf):
    cursor.execute('INSERT INTO usuario(email, nome,senha, cpf) VALUES (?,?,?,?)',
                   (email,nome, senha, cpf))
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
                                         ['Tela de inicio', 'Login',
                                          'Login Presidente', 'Área do Gerente de TI'])

if paginaSelecionada == 'Tela de inicio':
    st.title('Tela principal')
    st.text('Em construção 🏗')



elif paginaSelecionada == 'Login':
    st.sidebar.title("Seja Bem vindo !")
    funcionarios = st.sidebar.selectbox('Selecione a Opção', ['Login', 'Cadastro'])

    if funcionarios == 'Cadastro':
        st.title('Seja Bem vindo a tela Cadastro')
        input_email = st.text_input(label='Insira seu e-mail')
        input_name = st.text_input(label='Insira o seu nome')
        input_senha = st.text_input(label='Defina uma senha', type="password")
        input_cpf = st.text_input(label='Insira o seu CPF')

        if st.button("Enviar Dados"):
            create_usertable()
            add_userdata(input_email,input_name, input_senha, input_cpf)
            st.success('Adicionado com sucesso !!')
            st.info("Vá para o menu de login!!")


    if funcionarios == 'Login':
        nome = st.sidebar.text_input('Insira seu E-mail')
        senha = st.sidebar.text_input('Insira a senha', type='password')
        if st.sidebar.checkbox('Login'):
            # if input_senha_func == '1234':
            create_usertable()
            create_secretaria()
            result = login_user(nome, senha)
            result2 = login_secretaria(nome, senha)
            if result:
                nome2 = get_name(nome)
                st.sidebar.title(f"Logado como: {nome2}")
                st.title(f'Bem vindo de Volta {nome2}')
                area_pesq =st.selectbox('Selecione o que deseja',['Inicio'])
                if area_pesq == 'Inicio':
                    st.title('Página inicial do pesquisador')
                    st.text('Selecione uma opção acima para começar os trabalhos !!')
                
            elif result2:
                st.sidebar.title('Secretária logada')
                st.title("Área da Secretária")
               
            
            else:
                st.warning("Usuário incorreto ou Inexistente")    


