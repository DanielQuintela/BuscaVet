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
        minha_agenda, em_andamento, Histórico_servico = st.tabs(["Minha Agenda" , "Em Andamento", "Histórico de Serviços"])

        with minha_agenda:
            st.title('Minha Agenda')

            minha_especialidade = Banco.busca_especialidade_nome(email)

            st.write(f'Minha Especialidade Atual {minha_especialidade[0]}')
            st.write(f'Minha Area de Atuação Atual {minha_especialidade[1]}')
            
        with em_andamento:
            st.title('Em Andamento')

            st.write('Nenhum Agendamento Marcado')

        with Histórico_servico:
            st.title('Histórico Vazio, Por enquanto 😉')
            
    if area == 'Alterar dados':
        st.title('Cadastre seus dados específicos')
        input_localidade = st.text_input(label='Insira sua Localidade de atuação')
        input_especialidade = st.text_input(label='Qual sua especialidade')

        if st.button('Salvar'):
            Banco.especialidade(email, input_especialidade, input_localidade)

            st.success('Dados Atualizados ! 🍷 🗿')
           

    if area == 'Cadastrar Clínica':
        st.title("Seja bem vindo a tela de cadastro de Clínicas")
        
        
    if sair:
        main.fechar()
            
       

   
