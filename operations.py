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

def get_all_veiculos():
    response = requests.get(local_host + "/get_all_veiculos")

    if response.status_code == 200:
        veiculos = response.json()  # Assumindo que a resposta é uma lista de veículos
        for veiculo in veiculos:
            print("Placa:", veiculo["placa"])
            print("Marca:", veiculo["marca"])
            print("Modelo:", veiculo["modelo"])
            print("Cor:", veiculo["cor"])
            print("Tipo de Combustível:", veiculo["tipo_comb"])
            print("Quilometragem:", veiculo["kms"])
            print("Valor do Carro:", veiculo["vlr_car"])
            print("Ar Condicionado:", 'Sim' if veiculo["ar_cond"] else 'Não')
            print("Ativo:", 'Sim' if veiculo["ativo"] else 'Não')
            print("#####################################")
    else:
        print("Erro ao listar veículos:", response.status_code, response.text)

def get_all_clientes():
    response = requests.get(local_host + "/get_all_clientes")

    print(response)
    if response.status_code == 200:
        clientes = response.json()
        for cliente in clientes:
            print("Nome:", cliente["nome"])
            print("CPF:", cliente["cpf"])
            print("Endereço:", cliente["endereco"])
            print("Data de nascimento:", cliente["dt_nasc"])
            print("CNH:", cliente["cnh"])
            print("#####################################")
    else:
        print("Erro ao listar clientes:", response.status_code, response.text)




def get_all_funcionarios():
    response = requests.get(local_host + "/get_all_funcionarios")

    if response.status_code == 200:
        funcionarios = response.json()
        for funcionario in funcionarios:

            if (funcionario["ativo"] == False):
                continue
            else:
                print("########################")
                print("Nome: ", funcionario["nome"])
                print("CPF: ", funcionario["cpf"])
                print("Cargo: ", funcionario["cargo"])
    else:
        print ("Erro ao listar funcionarios")


def get_all_clientes():
    response = requests.get(local_host + "/get_all_clientes");

    if response.status_code == 200:
        clientes = response.json()
        for cliente in clientes:
            print("Nome:", cliente["nome"])
            print("CPF:", cliente["cpf"])
            print("#####################################") 
    else:
        return "Erro ao listar clientes"

def get_all_clientes():
    response = requests.get(local_host + "/get_all_clientes")
    print(response)
    if response.status_code == 200:
        clientes = response.json()
        for cliente in clientes:
            print("Nome:", cliente.get("nome", "Unavailable"))
            print("CPF:", cliente.get("cpf", "Unavailable"))
            print("Endereço:", cliente.get("endereco", "Unavailable"))
            print("Data de nascimento:", cliente.get("dt_nasc", "Unavailable"))
            print("CNH:", cliente.get("cnh", "Unavailable"))
            print("#####################################")
    else:
        print("Erro ao listar clientes:", response.status_code, response.text)



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

    response = requests.post(local_host + "/cadastrar_funcionario", json=cliente_data)
    
    # Verificar o status da resposta
    if response.status_code == 200:
        return "Funcionário cadastrado com sucesso!"
    else:
        return "Erro ao cadastrar o funcionario."

def promover_funcionario():
    cpf = input("CPF do funcionario: ")
    novo_cargo = input("Novo cargo: ")
    novo_salario = input("Novo salario: ")

    # Criar o dicionário com os dados do cliente
    func_data = {
        "cargo": novo_cargo,
        "salario": novo_salario
    }

    response = requests.put(local_host + f"/promover_funcionario/{cpf}", json=func_data)
    
    # Verificar o status da resposta
    if response.status_code == 200:
        return "funcionario promovido com sucesso!"
    else:
        return "Erro ao promover o funcionario."

def alterar_endereco_funcionario():
    cpf = input("CPF do funcionario: ")
    novo_endereco = input("Novo endereco: ")

    # Criar o dicionário com os dados do cliente
    cliente_data = { "endereco": novo_endereco }

    response = requests.put(local_host + "/alterar_endereco_funcionario/" + cpf, json=cliente_data)
    if response.status_code == 200:
        return "endereco do funcionario alterado com sucesso!"
    else:
        return "Erro ao alterar o endereco do funcionario."

def demitir_funcionario():
    cpf = input("CPF do funcionario: ")

    response = requests.delete(local_host + "/demitir_funcionario/" + cpf);

    if response.status_code == 200:
        return "Funcionario demitido com sucesso"
    else:
        return "Erro ao demitir funcionario."

def get_all_reservas():
    response = requests.get(local_host + "/get_all_reservas")
    
    if response.status_code == 200:
        reservas = response.json()
        for reserva in reservas:
            print("Código da reserva:", reserva.get("cod_reserva", "N/A"))  # Safe access with default value
            print("Código do cliente:", reserva.get("cod_cliente", "N/A"))
            print("ID do funcionário:", reserva.get("id_funcionario", "N/A"))
            print("Valor:", reserva.get("valor", "N/A"))  # Prevent KeyError by using .get()
            print("Data da reserva:", reserva.get("dt_reserva", "N/A"))
            print("Data de devolução:", reserva.get("dt_devolucao", "N/A"))
            print("Placa do veículo:", reserva.get("placa_veiculo", "N/A"))
            print("#####################################")
    else:
        print("Erro ao listar reservas:", response.status_code)


def fazer_reserva():
    get_all_veiculos()
    placa = input("Placa do carro:")

    get_all_clientes()
    cpf = input("CPF do cliente:")

    get_all_funcionarios()
    id_funcionario = input("CPF do funcionario:")

    dt_reserva = input("Data inicio da reserva (no formato YYYY-MM-DD): ")
    dias = input("Quantidade de dias:")

    cliente_data = { 
            "cpf": cpf,
            "cpf_funcionario": id_funcionario,
            "dias": dias,
            "dt_reserva": dt_reserva,
            "placa": placa
            }

    response = requests.post(local_host + "/fazer_reserva", json=cliente_data)

    if response.status_code == 200:
        valor = response.json()  # Extracting the value from the JSON response
        print("Valor da reserva:", valor)
        return "Reserva realizada com sucesso!"
    else:
        return "Erro ao realizar a reserva."

