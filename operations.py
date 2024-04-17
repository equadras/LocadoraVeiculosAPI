import json
import requests

local_host = "http://127.0.0.1:8080"

def tirar_veiculo_frota():
    placa = input("Qual a placa do veiculo: ")
    response = requests.delete(local_host + f"/tirar_veiculo_frota/{placa}")

    if response.status_code == 200:
        return "Veiculo retirado com sucesso!"
    else:
        return "Erro ao retirar o veiculo"

def adicionar_veiculo():
    placa = input("Placa do veículo: ")
    tipo_comb = input("Tipo combustivel: ")
    cor = input("Cor: ")
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    kms = int(input("Quilometragem: "))
    vlr_car = int(input("Valor carro: "))
    ar_cond = bool(int(input("Possui ar condicionado ? [1/0]: ")))  # Convertendo para booleano
    ativo = bool(int(input("Participa da frota ativa ? [1/0]: ")))  # Convertendo para booleano

    novo_veiculo = {
        "placa": placa,
        "tipo_comb": tipo_comb,
        "cor": cor,
        "marca": marca,
        "modelo": modelo,
        "kms": kms,
        "vlr_car": vlr_car,
        "ar_cond": ar_cond,
        "ativo": ativo
    }

    response = requests.post(local_host + "/adicionar_veiculo", json=novo_veiculo)
    
    if response.status_code == 200:
        return "Veículo cadastrado com sucesso!"
    else:
        return "Erro ao cadastrar o veículo."


def mudar_endereco_cliente():
    # mostrar todos os clientes
    novo_endereco = input("Novo endereço: ")
    id_cliente = int(input("Seu ID: "))

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



def demitir_funcionario():
    cpf = input("CPF do funcionario: ")

    response = requests.delete(local_host + "/demitir_funcionario/" + cpf);

    if response.status_code == 200:
        return "Funcionario demitidio com sucesso"
    else:
        return "Erro ao demitir funcionario."

