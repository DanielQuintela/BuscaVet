import pandas as pd
import streamlit as st
import sqlite3
import Banco.banco_dados as Banco
con = sqlite3.connect('banco_programa.db')
cursor = con.cursor()

def Usuario(nome):     
    nome2 = Banco.get_name(nome)
    st.sidebar.title(f"Logado como: {nome2}")
    area_pesq =st.selectbox('Selecione o que deseja',['Inicio'])
    if area_pesq == 'Inicio':
        st.title(f'Página inicial, Olá {nome2}')
        st.text('Selecione uma opção acima para começar os trabalhos !!')
        algo1, algo2, algo3 = st.tabs(["Algo1", "Algo2", "Algo3"])
        with algo1:
            st.title('Teste 1')
            
        with algo2:
            st.title('Teste 2')
        with algo3:
            st.title('Teste 3')