import pandas as pd
import streamlit as st
import sqlite3
import Banco.banco_dados as Banco, main, Page.cadastrar_pet as Cadastrar
from datetime import datetime

con = sqlite3.connect('banco_programa.db')
cursor = con.cursor()

selectbox_placeholder = st.sidebar.empty()
def Usuario(email):
   
    nome2 = Banco.get_name(email)
    st.sidebar.title(f"Entrou como: {nome2}")
    sair = st.sidebar.button('Sair')
    area_pesq =selectbox_placeholder.selectbox('Selecione o que deseja',['Inicio'])

    if area_pesq == 'Inicio':
        st.title(f'Página inicial, Olá {nome2}')
        meus_pets, em_andamento, Histórico_servico, buscar_servico = st.tabs(["Meus Pets", "Em Andamento" , "Histórico de Serviços", 'Buscar Serviço',])
        with meus_pets:
            st.title('Pets')
            Banco.create_pet()
            nome1 = nome2[0:]
            
            pets = Banco.consulta_pet(email)
            
            if pets:
                for pet in pets:
                    dono, nome, raca, cor, data_nasc = pet
                    idade = Banco.calculate_age(datetime.strptime(data_nasc, '%Y-%m-%d').date())
                    pet_info = {'Dono': [dono], 'Nome': [nome], 'Raça': [raca], 'Cor': [cor], 'Idade': [idade], 'Data de Nascimento': [data_nasc]}
                    lista_pet = pd.DataFrame(pet_info)
                    st.dataframe(lista_pet)
            else:
                st.write("Não foi encontrado nenhum pet com o email fornecido.")
                        
            apertado = st.checkbox("Adicionar Pet")

            if apertado:
                Cadastrar.Cadastrar_pet(email, nome1)

            
        with em_andamento:
            st.title('Serviços em Andamento')
            st.write('Nenhum serviço em Andamento')

        with Histórico_servico:
            st.title('Histórico de Serviço')
            st.write('Histórico Vazio')
        
        with buscar_servico:
            st.title('Escolha as opções a baixo')
            especialidade = Banco.busca_especialidade_geral()
            locais = Banco.localidade_geral()
            especialidades = st.empty()
            
            especialidade_selecionada = especialidades.selectbox('Selecione a Especialidade: ',especialidade)

            if especialidade_selecionada:
                st.write("Médicos disponíveis para a especialidade:", especialidade_selecionada)
                medicos = Banco.busca_medicos_por_especialidade(especialidade_selecionada)
                 
                lista_medicos = pd.DataFrame(medicos, columns=['Médico', 'Especialidade', 'Localidade', 'Telefone',])
                st.dataframe(lista_medicos)

             # Criar DataFrame com coordenadas de Aracaju
            data = {'LAT': [-10.9472], 'LON': [-37.0731]}
            df = pd.DataFrame(data)

            texto_inicio2 = st.empty()
            mapa_st2 = st.empty()   
            # Exibir mapa no Streamlit
            texto_inicio2.title("Localização dos médicos disponíveis")
            mapa_st2.map(df)

            agendar = st.button('Agendar')

            if agendar:
                st.success('Doutor Disponível, Irei te encaminhar para o agendamento !!')

           

    if sair:
        main.fechar()
