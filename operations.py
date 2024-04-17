import json
from requests import *


local_host = "http://127.0.0.1:8080"

def cadastrar_cliente():
    nome = input("Nome: ")
    cpf = input("CPF: ")
    dt_nasc = input("Data nascimento: ")
    endereco = input("Endereco: ")
    cnh = input("CNH: ")

    js = f'{ "dt_nasc": {dt_nasc}, "cnh": {cnh}, "nome": {nome}, "cpf": {cpf}, "endereco": {endereco} }'
    
    js = json.dumps()
    return put(local_host + "/cadastrar_cliente", data=js)


