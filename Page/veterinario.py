import pandas as pd
import streamlit as st
import sqlite3
import Banco.banco_dados as Banco, main 
con = sqlite3.connect('banco_programa.db')
cursor = con.cursor()
checkbox_placeholder = st.empty()

def Veterinario(nome):
    nome2 = Banco.get_name_vet(nome)
    st.sidebar.title(f'Veterinário {nome2}')
    area = st.sidebar.selectbox('Selecione um caminho', ['Inicio', 'Visualizar Tabela', 'Cadastrar Clínica'])
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
            
    if area == 'Visualizar Tabela':
        st.text('tabela')
    if area == 'Cadastrar Clínica':
        st.title("Seja bem vindo a tela de cadastro de Clínicas")
        
    if sair:
        main.fechar()
            
       

    
        

