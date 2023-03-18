import pandas as pd
import streamlit as st
import sqlite3

con = sqlite3.connect('banco_programa.db')
cursor = con.cursor()

# cadastro de pesquisador, inicialmente chamado no código de user

def create_usertable():
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS usuario(email TEXT, nome TEXT,senha TEXT, cpf NUMERIC UNIQUE, telefone NUMERIC UNIQUE)')

def add_user(email, nome, senha, cpf, telefone):
    cursor.execute('INSERT INTO usuario(email, nome,senha, cpf, telefone) VALUES (?,?,?,?,?)',
                   (email,nome, senha, cpf, telefone))
    con.commit()

def login_user(email, senha):
    cursor.execute('SELECT * FROM usuario WHERE email = ? AND senha = ?', (email, senha))
    data = cursor.fetchall()
    return data
# Aqui vai buscar o nome do usuário logado
def get_name(email):
    cursor.execute('SELECT nome FROM usuario WHERE email = ?', (email,))
    data = cursor.fetchall()
    # Acima pegou o nome completo, abaixo eu separei e peguei os 2 primeiros
    if data:
        nome_completo = str(data[0][0])
        lista_nomes = nome_completo.split()
        nome_abreviado = ' '.join(lista_nomes[:2])
        return nome_abreviado
    else:
        return None


#criar no banco o veterinário

def create_veterinario():
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS veterinario(email TEXT, nome TEXT,senha TEXT, crmv NUMERIC UNIQUE, telefone NUMERIC UNIQUE)')
    
def add_veterinario(email, nome, senha, crmv, telefone):
    cursor.execute('INSERT INTO veterinario(email, nome,senha, crmv, numero) VALUES (?,?,?,?,?)',
                   (email,nome, senha, crmv, telefone))
    con.commit()

def login_veterinario(email, senha):
    cursor.execute('SELECT * FROM veterinario WHERE email = ? AND senha = ?', (email, senha))
    data = cursor.fetchall()
    return data

def get_name_vet(email):
    cursor.execute('SELECT nome FROM veterinario WHERE email = ?', (email,))
    data = cursor.fetchall()
    return str(data[0][0]) if data else None

def ver_todos_nomes():
    cursor.execute('SELECT DISTINCT nome FROM veterinario')
    data = cursor.fetchall()
    return data

def delete_vet(resultado):
    cursor.execute(f'DELETE FROM veterinario WHERE nome="{resultado}"')
    con.commit()



paginaSelecionada = st.sidebar.selectbox('Selecione o caminho',
                                         ['Tela de inicio', 'Login e/ou Cadastro'])

if paginaSelecionada == 'Tela de inicio':
    st.title('Tela principal')
    st.text('Em construção 🏗')



elif paginaSelecionada == 'Login e/ou Cadastro':
    st.sidebar.title("Seja Bem vindo !")
    funcionarios = st.sidebar.selectbox('Selecione a Opção', ['Login', 'Cadastro'])

    if funcionarios == 'Cadastro':
        st.title('Seja Bem vindo a tela Cadastro')
        input_email = st.text_input(label='Insira seu e-mail')
        input_name = st.text_input(label='Insira o seu nome completo')
        input_senha = st.text_input(label='Defina uma senha', type="password")
        input_cpf = st.text_input(label='Insira o seu CPF')
        input_telefone = st.text_input(label='Insira o seu telefone')

        if st.button("Enviar Dados"):
            create_usertable()
            add_user(input_email,input_name, input_senha, input_cpf, input_telefone)
            st.success('Adicionado com sucesso !!')
            st.info("Vá para o menu de login!!")


    if funcionarios == 'Login':
        nome = st.sidebar.text_input('Insira seu E-mail')
        senha = st.sidebar.text_input('Insira a senha', type='password')
        if st.sidebar.checkbox('Login'):
            # if input_senha_func == '1234':
            create_usertable()
            create_veterinario()
            result = login_user(nome, senha)
            result2 = login_veterinario(nome, senha)
            if result:
                nome2 = get_name(nome)
                st.sidebar.title(f"Logado como: {nome2}")
                area_pesq =st.selectbox('Selecione o que deseja',['Inicio'])
                if area_pesq == 'Inicio':
                    st.title(f'Página inicial, Olá {nome2}')
                    st.text('Selecione uma opção acima para começar os trabalhos !!')
                
            elif result2:
                nome2 = get_name_vet(nome)
                st.sidebar.title(f'Veterinário {nome2} logado')
                st.title(f"Bem vindo {nome2}, Área do Veterinário ")

            elif senha == '0809':
                area_mestre = st.selectbox('Selecione oque deseja',['Inicio','Adicionar Veterinário',
                                                                    'Remover Veterinário'])
                if area_mestre == 'Inicio':
                    st.title('Bem vindo mestre, o sistema do site é seu')

                if area_mestre == 'Adicionar Veterinário':
                    st.title('Vamos adicionar o mais novo Veterinário ao Sistema')
                    input_email = st.text_input(label='Coloque o email')
                    input_name = st.text_input(label='Insira o nome')
                    input_senha = st.text_input(label='Digite a senha', type='password')
                    input_crmv = st.text_input(label='Insira o crmv')
                    input_telefone = st.text_input(label='Insira o seu telefone')

                    if st.button('Cadastrar Veterinário'):
                        create_veterinario()
                        add_veterinario(input_email,input_name,input_senha,input_crmv, input_telefone)
                        st.success('Adicionado com sucesso !!')
                        st.info("Você é o Cara, Diretor !!")

                
                if area_mestre == 'Remover Veterinário':
                    st.title('Qual Veterinário vamos remover do Sistema')
                    st.text('Nesta seleção podemos ver os Veterinários atuantes na empresa')
                    st.subheader('Lista de Veterinários')
                    dados_vet = cursor.execute('SELECT nome, crmv from veterinario')
                    pesquisa = pd.DataFrame(dados_vet, columns=['Veterinários ativos','CRMV'])
                    st.dataframe(pesquisa)
                    with st.form(key='include_cliente'):
                        st.subheader('Selecione o que deseja realizar')
                        remover = st.form_submit_button("Remover")
                    
                        nomes_unicos = [i[0] for i in ver_todos_nomes()]
                        selecao = st.selectbox("Pesquisadores", nomes_unicos)
                        if remover:
                            delete_vet(selecao)
                            st.warning(f"Removido(a): '{selecao}' do Sistema")
                            st.warning('Atualize a Página')
                            
                
            else:
                st.warning("Usuário incorreto ou Inexistente")
    
    
