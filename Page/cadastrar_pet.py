import pandas as pd
import streamlit as st
import sqlite3
import Banco.banco_dados as Banco

def Cadastrar_pet(email, nome1):
    nome_input = st.text_input('Qual é o nome do Seu lindo Pet ?')
    raca = st.text_input('Qual a Raça ?')
    cor = st.text_input("Qual a cor ?")
    data_nascimento = st.date_input("Qual a data de nascimento ?")

    salvar = st.button('Salvar novo Pet')

    if salvar:
        Banco.add_pet(email, nome1, nome_input, raca, cor,data_nascimento,)
        st.success("Novo Pet Cadastrado !!")

