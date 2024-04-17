import json
import requests

local_host = "http://127.0.0.1:8080"

def cadastrar_cliente():
    nome = input("Nome: ")
    cpf = input("CPF: ")
    dt_nasc = input("Data de nascimento (no formato YYYY-MM-DD): ")
    endereco = input("Endereço: ")
    cnh = input("CNH: ")

    # Criar o dicionário com os dados do cliente
    cliente_data = {
        "nome": nome,
        "cpf": cpf,
        "dt_nasc": dt_nasc,
        "endereco": endereco,
        "cnh": cnh
    }

    response = requests.post(local_host + "/cadastrar_cliente", json=cliente_data)
    
    # Verificar o status da resposta
    if response.status_code == 200:
        return "Cliente cadastrado com sucesso!"
    else:
        return "Erro ao cadastrar o cliente."

def cadastrar_funcionario():
    nome = input("Nome: ")
    cpf = input("CPF: ")
    dt_nasc = input("Data de nascimento (no formato YYYY-MM-DD): ")
    endereco = input("Endereço: ")
    cargo = input("Cargo: ")
    salario = input("Salario: ")

    cliente_data = {
        "nome": nome,
        "cpf": cpf,
        "dt_nasc": dt_nasc,
        "endereco": endereco,
        "cargo": cargo,
        "salario": salario
    }

    response = requests.post(local_host + "/cadastrar_cliente", json=cliente_data)
    
    # Verificar o status da resposta
    if response.status_code == 200:
        return "Cliente cadastrado com sucesso!"
    else:
        return "Erro ao cadastrar o cliente."

def promover_funcionario():
    cpf = input("CPF do funcionario: ")
    novo_cargo = input("Novo cargo: ")
    novo_salario = input("Novo salario: ")

    # Criar o dicionário com os dados do cliente
    cliente_data = {
        "cargo": novo_cargo,
        "salario": novo_salario
    }

    response = requests.put(local_host + "/promover_funcionario/" + cpf, json=cliente_data)
    
    # Verificar o status da resposta
    if response.status_code == 200:
        return "funcionario promovido com sucesso!"
    else:
        return "Erro ao promover o funcionario."

def alterar_endereco_funcionario():
    cpf = input("CPF do funcionario: ")
    novo_endereco = input("Novo endereco: ")

    # Criar o dicionário com os dados do cliente
    cliente_data = {
        "endereco": novo_endereco
    }

    response = requests.put(local_host + "/alterar_endereco_funcionario/" + cpf, json=cliente_data)
    
    # Verificar o status da resposta
    if response.status_code == 200:
        return "endereco do funcionario alterado com sucesso!"
    else:
        return "Erro ao alterar o endereco do funcionario."
