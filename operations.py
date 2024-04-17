import json
import requests

local_host = "http://127.0.0.1:8080"

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

    # Converter o dicionário para formato JSON
    cliente_json = json.dumps(cliente_data)

    # Enviar a requisição POST para cadastrar o cliente
    response = requests.post(local_host + "/cadastrar_cliente", json=cliente_json)
    
    # Verificar o status da resposta
    if response.status_code == 200:
        return "Cliente cadastrado com sucesso!"
    else:
        return "Erro ao cadastrar o cliente."
