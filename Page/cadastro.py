import pandas as pd
import streamlit as st
import sqlite3
import Banco.banco_dados as Banco

def Cadastro():
    st.title('Atenção:')
    st.subheader(""" Caso queira se inscrever como veterinário, selecionar abaixo:
              """)
    usuario, veterinario = st.tabs(["Usuário", "Veterinário"])
    with usuario:
        input_email = st.text_input(label='Insira seu e-mail')
        input_name = st.text_input(label='Insira o seu nome completo')
        input_senha = st.text_input(label='Defina uma senha', type="password")
        input_cpf = st.text_input(label='Insira o seu CPF')
        input_telefone = st.text_input(label='Insira o seu telefone')

        if st.button("Cadastrar"):
            Banco.create_usertable()
            Banco.add_user(input_email,input_name, input_senha, input_cpf, input_telefone)
            st.success('Adicionado com sucesso !!')
            st.info("Vá para o menu de login!!")

    with veterinario:
        st.title('Observações:')
        st.subheader(""" A nossa plataforma ultilizará os dados Fornecidos no cadastro de Veterinário para Análise e Aprovação dos Veterinários no Sistema.
              """)

        input_emailv = st.text_input(label='Coloque o email')
        input_namev = st.text_input(label='Insira o nome')
        input_senhav = st.text_input(label='Digite a senha', type='password')
        input_crmv = st.text_input(label='Insira o crmv')
        input_telefonev = st.text_input(label='Insira seu telefone')

        if st.button("Solicitar Análise de Aprovação"):
            Banco.create_veterinario()
            Banco.add_veterinario(input_emailv,input_namev, input_senhav, input_crmv, input_telefonev)

            st.success('Seus Dados foram enviado com Sucesso !! ')
            st.warning('O login será liiberado quando for Validado.')
