import pandas as pd
import streamlit as st
import sqlite3
import Banco.banco_dados as Banco, main

def Adm():
    area_mestre = st.selectbox('Selecione oque deseja',['Inicio','Adicionar Veterinário',
                                                                    'Gerenciar Veterinários'])
    sair = st.sidebar.button('Sair')
    if area_mestre == 'Inicio':
        st.title('Bem vindo mestre, o sistema do site é seu')

    if area_mestre == 'Adicionar Veterinário':
        st.title('Vamos adicionar o mais novo Veterinário ao Sistema')
        input_email = st.text_input(label='Coloque o email', key='22')
        input_name = st.text_input(label='Insira o nome', key='23')
        input_senha = st.text_input(label='Digite a senha', type='password', key='24')
        input_crmv = st.text_input(label='Insira o crmv', key='25')
        input_telefone = st.text_input(label='Insira o seu telefone', key='26')
        situacao= 'Aprovado'

        if st.button('Cadastrar Veterinário'):
            Banco.create_veterinario()
            Banco.add_veterinario(input_email,input_name,input_senha,input_crmv, input_telefone,situacao)
            st.success('Adicionado com sucesso !!')
            st.info("Você é o Cara, Diretor !!")

    
    if area_mestre == 'Gerenciar Veterinários':
        st.title('Nesta seleção podemos ver os Veterinários atuantes na empresa')
        st.subheader('Lista de Veterinários')
    
        dados_vet = Banco.situacao()
 
        pesquisa = pd.DataFrame(dados_vet, columns=['Veterinários ativos','CRMV', 'Situação'])
        st.dataframe(pesquisa)
        with st.form(key='include_cliente'):
            st.subheader('Selecione o que deseja realizar')
            aprovar = st.form_submit_button('Aprovar')
            remover = st.form_submit_button("Remover")
        
            nomes_unicos = [i[0] for i in Banco.ver_todos_nomes()]
            selecao = st.selectbox("Veterinários", nomes_unicos)
            if aprovar:
                Banco.aprovar_vet(selecao)
                st.success(f'{selecao} foi Aprovado com Sucesso')

            if remover:
                Banco.delete_vet(selecao)
                st.warning(f"Removido(a): '{selecao}' do Sistema")
                st.warning('Atualize a Página')

    if sair:
        main.fechar()
