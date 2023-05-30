import pandas as pd
import streamlit as st
import sqlite3
import Banco.banco_dados as Banco, main 
con = sqlite3.connect('banco_programa.db')
cursor = con.cursor()
checkbox_placeholder = st.empty()

def Veterinario(email):
    nome2 = Banco.get_name_vet(email)
    st.sidebar.title(f'Veterinário {nome2}')
    area = st.sidebar.selectbox('Selecione um caminho', ['Inicio', 'Alterar dados', 'Cadastrar Clínica'])
    sair = st.sidebar.button('Sair')
    st.title(f"Bem vindo {nome2}, a Área do Veterinário ")
    
    if area == 'Inicio':
        st.text('inicio')
        meus_pets, em_andamento, Histórico_servico = st.tabs(["Meus Pets", "Histórico de Serviços", "Em Andamento"])

        with meus_pets:
            st.title('Pets')
            
        with em_andamento:
            st.title('Teste 2')

        with Histórico_servico:
            st.title('Teste 3')
            
    if area == 'Alterar dados':
        st.title('Cadastre seus dados específicos')
        input_localidade = st.text_input(label='Insira sua Localidade de atuação')
        input_especialidade = st.text_input(label='Qual sua especialidade')

        if st.button('Salvar'):
            Banco.especialidade(email, input_especialidade, input_localidade)
            especialidade = Banco.busca_especialidade(email)
            st.text(f'Sua especilidade é {especialidade}')
    if area == 'Cadastrar Clínica':
        st.title("Seja bem vindo a tela de cadastro de Clínicas")
        
    if sair:
        main.fechar()
            
       

   
