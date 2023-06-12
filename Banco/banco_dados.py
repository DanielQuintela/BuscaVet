import pandas as pd
import streamlit as st
import sqlite3
import threading
from datetime import datetime
conn_local = threading.local()


con = sqlite3.connect('banco_programa.db')
cursor = con.cursor()
    


# cadastro de pesquisador, inicialmente chamado no código de user

def create_usertable():
    con = sqlite3.connect('banco_programa.db')
    cursor = con.cursor()
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS usuario(email TEXT UNIQUE, nome TEXT,senha TEXT, cpf NUMERIC UNIQUE, telefone NUMERIC UNIQUE)')
    cursor.close()
    con.close()

def add_user(email, nome, senha, cpf, telefone):
    con = sqlite3.connect('banco_programa.db')
    cursor = con.cursor()
    cursor.execute('INSERT INTO usuario(email, nome,senha, cpf, telefone) VALUES (?,?,?,?,?)',
                   (email,nome, senha, cpf, telefone))
    con.commit()
    cursor.close()
    con.close()



def login_user(email, senha):
    con = sqlite3.connect('banco_programa.db')
    cursor = con.cursor()
    cursor.execute('SELECT * FROM usuario WHERE email = ? AND senha = ?', (email, senha))
    data = cursor.fetchall()
    cursor.close()
    con.close()
    return data
# Aqui vai buscar o nome do usuário logado
def get_name(email):
    con = sqlite3.connect('banco_programa.db')
    cursor = con.cursor()
    cursor.execute('SELECT nome FROM usuario WHERE email = ?', (email,))
    data = cursor.fetchall()
    cursor.close()
    con.close()
    # Acima pegou o nome completo, abaixo eu separei e peguei os 2 primeiros
    if data:
        nome_completo = str(data[0][0])
        lista_nomes = nome_completo.split()
        nome_abreviado = ' '.join(lista_nomes[:2])
        return nome_abreviado
    else:
        return None

# Ainda nas funções de usuario
# criando a função de adicionar pet ao banco
def create_pet():
    con = sqlite3.connect('banco_programa.db')
    cursor = con.cursor()
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS pet(email TEXT, dono TEXT, nome TEXT, raca TEXT,cor TEXT, data_nascimento DATE)')
    cursor.close()
    con.close()

def add_pet(email, dono, nome, raca, cor, data_nascimento):
    con = sqlite3.connect('banco_programa.db')
    cursor = con.cursor()
    cursor.execute(
        'INSERT INTO pet(email, dono, nome, raca, cor, data_nascimento) VALUES (?,?,?,?,?,?)', (email, dono, nome, raca, cor, data_nascimento))
    con.commit()
    cursor.close()
    con.close()


def consulta_pet(email):
    con = sqlite3.connect('banco_programa.db')
    cursor = con.cursor()
    cursor.execute('SELECT dono, nome , raca, cor, data_nascimento FROM pet WHERE email = ?', (email,))
    data = cursor.fetchall()
    cursor.close()
    con.close()
    return data

def calculate_age(date_of_birth):
    # Calcula a idade com base na data de nascimento
    today = datetime.today().date()
    age = today.year - date_of_birth.year
    if today.month < date_of_birth.month or (today.month == date_of_birth.month and today.day < date_of_birth.day):
        age -= 1
    return age

#criar no banco o veterinário

def create_veterinario():
    con = sqlite3.connect('banco_programa.db')
    cursor = con.cursor()
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS veterinario(email TEXT, nome TEXT,senha TEXT, crmv NUMERIC UNIQUE, telefone NUMERIC UNIQUE, situacao TEXT, especialidade TEXT, localidade TEXT)')
    cursor.close()
    con.close()
    
def add_veterinario(email, nome, senha, crmv, telefone,situacao = 'Espera'):
    con = sqlite3.connect('banco_programa.db')
    cursor = con.cursor()
    cursor.execute('INSERT INTO veterinario(email, nome,senha, crmv, telefone,situacao) VALUES (?,?,?,?,?,?)',
                   (email,nome, senha, crmv, telefone,situacao))
    con.commit()
    cursor.close()
    con.close()
    # Adicionar a especialidade do médico e a localidade
def especialidade(email, especialidade, localidade):
    con = sqlite3.connect('banco_programa.db')
    cursor = con.cursor()
    cursor.execute('UPDATE veterinario SET especialidade = ?, localidade = ? WHERE email = ?', (especialidade, localidade, email))
    con.commit()
    cursor.close()
    con.close()

def busca_especialidade_nome(email):
    con = sqlite3.connect('banco_programa.db')
    cursor = con.cursor()
    cursor.execute('SELECT especialidade, localidade FROM veterinario WHERE email = ?', (email,))
    data = cursor.fetchone()
    cursor.close()
    con.close()
    if data:
        data = data[0:]
    return data

def busca_especialidade_geral():
    con = sqlite3.connect('banco_programa.db')
    cursor = con.cursor()
    cursor.execute('SELECT nome, especialidade FROM veterinario')
    data = cursor.fetchall()
    cursor.close()
    con.close()

    especialidades = set()
    for row in data:
        especialidades.add(row[1])

    return list(especialidades)

 

def busca_medicos_por_especialidade(especialidade):
    con = sqlite3.connect('banco_programa.db')
    cursor = con.cursor()
    cursor.execute('SELECT nome, especialidade, localidade, telefone FROM veterinario WHERE especialidade = ?', (especialidade,))
    data = cursor.fetchall()
    cursor.close()
    con.close()

    # medicos = [row[0] for row in data]
    return data

def busca_especidalidade_por_local(localidade):
    con = sqlite3.connect('banco_programa.db')
    cursor = con.cursor()
    cursor.execute('SELECT nome, especialidade, localidade FROM veterinario WHERE localidade = ?', (localidade,))
    data = cursor.fetchall()
    cursor.close()
    con.close()

def localidade_geral():
    con = sqlite3.connect('banco_programa.db')
    cursor = con.cursor()
    cursor.execute('SELECT localidade FROM veterinario')
    data = cursor.fetchall()
    cursor.close()
    con.close()

    localidade = set()
    for row in data:
        localidade.add(row[0])

    return list(localidade)



def busca_localidade_nome(nome):
    con = sqlite3.connect('banco_programa.db')
    cursor = con.cursor()
    cursor.execute('SELECT localidade FROM veterinario WHERE nome = ?', (nome,))
    data = cursor.fetchone()
    cursor.close()
    con.close()
    if data:
        data = data[0]
    return data


def login_veterinario(email, senha, situacao):
    con = sqlite3.connect('banco_programa.db')
    cursor = con.cursor()
    cursor.execute('SELECT * FROM veterinario WHERE email = ? AND senha = ? AND situacao = ?', (email, senha, situacao))
    data = cursor.fetchall()
    cursor.close()
    con.close()
    return data

def get_name_vet(email):
    con = sqlite3.connect('banco_programa.db')
    cursor = con.cursor()
    cursor.execute('SELECT nome FROM veterinario WHERE email = ?', (email,))
    data = cursor.fetchall()
    cursor.close()
    con.close()
    if data:
        nome_completo = str(data[0][0])
        lista_nomes = nome_completo.split()
        nome_abreviado = ' '.join(lista_nomes[:2])
        return nome_abreviado
    else:
        return None
    
def situacao():
    con = sqlite3.connect('banco_programa.db')
    cursor = con.cursor()
    resultado = cursor.execute('SELECT nome, crmv, situacao from veterinario').fetchall()
    cursor.close()
    con.close()
    return resultado

def ver_todos_nomes():
    con = sqlite3.connect('banco_programa.db')
    cursor = con.cursor()
    cursor.execute('SELECT DISTINCT nome FROM veterinario')
    data = cursor.fetchall()
    cursor.close()
    con.close()
    return data

def aprovar_vet(resultado):
    con = sqlite3.connect('banco_programa.db')
    cursor = con.cursor()
    cursor.execute(f'UPDATE veterinario SET situacao = "Aprovado" WHERE nome = "{resultado}" ')
    con.commit()
    cursor.close()
    con.close()

def delete_vet(resultado):
    con = sqlite3.connect('banco_programa.db')
    cursor = con.cursor()
    cursor.execute(f'DELETE FROM veterinario WHERE nome="{resultado}"')
    con.commit()
    cursor.close()
    con.close()

#Criando banco de Clinica:

def criar_clinica():
    con = sqlite3.connect('banco_programa.db')
    cursor = con.cursor()
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS clinica(email TEXT, nome TEXT,senha TEXT, cnpj NUMERIC UNIQUE, telefone NUMERIC UNIQUE, situacao TEXT)')
    cursor.close()
    con.close()

def add_clinica(email, nome, senha, cnpj, telefone, situacao):
    con = sqlite3.connect('banco_programa.db')
    cursor = con.cursor()
    cursor.execute('INSERT INTO clinica(email, nome,senha, cnpj, telefone,situacao) VALUES (?,?,?,?,?,?)',
                   (email,nome, senha, cnpj, telefone,situacao))
    con.commit()
    cursor.close()
    con.close()

def login_clinica(email, senha, situacao):
    con = sqlite3.connect('banco_programa.db')
    cursor = con.cursor()
    cursor.execute('SELECT * FROM clinica WHERE email = ? AND senha = ? AND situacao = ?', (email, senha, situacao))
    data = cursor.fetchall()
    cursor.close()
    con.close()
    return data

def get_name_cli(email):
    con = sqlite3.connect('banco_programa.db')
    cursor = con.cursor()
    cursor.execute('SELECT nome FROM clinica WHERE email = ?', (email,))
    data = cursor.fetchall()
    cursor.close()
    con.close()
    return str(data[0][0]) if data else None
