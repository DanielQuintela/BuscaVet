import pandas as pd
import streamlit as st
import sqlite3
import Banco.banco_dados as Banco, main
con = sqlite3.connect('banco_programa.db')
cursor = con.cursor()

selectbox_placeholder = st.sidebar.empty()
def Usuario(nome):   
    
    nome2 = Banco.get_name(nome)
    st.sidebar.title(f"Entrou como: {nome2}")
    sair = st.sidebar.button('Sair')
    area_pesq =selectbox_placeholder.selectbox('Selecione o que deseja',['Inicio'])
    if area_pesq == 'Inicio':
        st.title(f'Página inicial, Olá {nome2}')
        meus_pets, em_andamento, Histórico_servico = st.tabs(["Meus Pets", "Histórico de Serviços", "Em Andamento"])
        with meus_pets:
            st.title('Pets')


            
        with em_andamento:
            st.title('Teste 2')

        with Histórico_servico:
            st.title('Teste 3')
    if sair:
        main.fechar()
