import pandas as pd
import streamlit as st
import sqlite3
import Banco.banco_dados as Banco
con = sqlite3.connect('banco_programa.db')
cursor = con.cursor()

def Veterinario(nome):
    nome2 = Banco.get_name_vet(nome)
    st.sidebar.title(f'Veterinário {nome2} logado')
    st.title(f"Bem vindo {nome2}, a Área do Veterinário ")

    area = st.selectbox('Selecione um caminho', ['Inicio', 'Visualizar Tabela'])
    if area == 'Inicio':
        st.text('inicio')
    if area == 'Visualizar Tabela':
        st.text('tabela')
