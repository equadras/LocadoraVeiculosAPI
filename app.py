import sys
import json
from flask import Flask, request, jsonify
from psutil import process_iter
from signal import SIGTERM
from sqlalchemy import create_engine
from sqlalchemy import text

app = Flask(__name__)
engine = create_engine("postgresql://trab_banco_owner:5kYVI6gRfHlK@ep-nameless-tooth-a5fq2x2q-pooler.us-east-2.aws.neon.tech/trab_banco?sslmode=require")

# =================== ROTAS FUNCIONARIOS  =================== 
@app.route("/cadastrar_funcionario", methods=["POST"])
def cadastrar_funcionario():
    # Obter os dados do funcionário a partir do corpo da requisição
    data = request.json
    nome = data.get('nome')
    cpf = data.get('cpf')
    cargo = data.get('cargo')
    endereco = data.get('endereco')
    salario = data.get('salario')
    dt_nasc = data.get('dt_nasc')

    # Utilize parâmetros na consulta SQL para evitar injeção de SQL
    query = text("INSERT INTO funcionarios (nome, cpf, cargo, endereco, salario, dt_nasc, ativo) "
                 "VALUES (:nome, :cpf, :cargo, :endereco, :salario, :dt_nasc, true)")

    # Inserir os dados do funcionário na tabela 'funcionario'
    with engine.connect() as connection:
        connection.execute(query, {
            'nome': nome,
            'cpf': cpf,
            'cargo': cargo,
            'endereco': endereco,
            'salario': salario,
            'dt_nasc': dt_nasc
        })

    return "Funcionário cadastrado com sucesso!"


@app.route("/promover_funcionario/<int:id_func>", methods=["PUT"])
def promover_funcionario(id_func):
    # Obter os novos dados do funcionário a partir do corpo da requisição
    data = request.json
    novo_cargo = data.get('cargo')
    novo_salario = data.get('salario')

    query = text("""UPDATE funcionarios
                    SET cargo = :novo_cargo, salario = :novo_salario
                    WHERE id_funcionario = :id_func""")

    # Atualizar o cargo e o salário do funcionário na tabela 'funcionario'
    with engine.connect() as connection:
        connection.execute(query, {
            'novo_cargo': novo_cargo,
            'novo_salario': novo_salario,
            'id_func': id_func
        })

    return f"Dados do funcionário com ID {id_func} atualizados com sucesso!"


@app.route("/alterar_endereco_funcionario/<int:id_func>", methods=["PUT"])
def alterar_endereco_funcionario(id_func):
    # Obter o novo endereço do funcionário a partir do corpo da requisição
    data = request.json
    novo_endereco = data.get('endereco')
    
    # Atualizar o endereço do funcionário na tabela 'funcionarios'
    with engine.connect() as connection:
        connection.execute(
            f"UPDATE funcionarios SET endereco = '{novo_endereco}' WHERE id_funcionario = {id_func}"
        )

    return f"Endereço do funcionário com ID {id_func} alterado com sucesso!"

@app.route("/demitir_funcionario/<int:id_func>", methods=["DELETE"])
def demitir_funcionario(id_func):
    with engine.connect() as connection:
        connection.execute(
            f"UPDATE funcionarios SET ativo = False WHERE id_funcionario = {id_func}"
        )

    return f"Funcionário com ID {id_func} foi demitido com sucesso!"
# =========================================================== 

# =================== ROTAS VEICULOS =================== 
@app.route("/get_all_veiculos", methods=["GET"])
def get_all_veiculos():
    with engine.connect() as connection:
        result = connection.execute("SELECT placa, marca, modelo, ar_cond, vlr_car FROM veiculos WHERE ativo = true")
        veiculos = result.fetchall()
    
    return jsonify(veiculos)


@app.route("/tirar_veiculo_frota/<string:placa>", methods=["DELETE"])
def tirar_veiculo_frota(placa):
    with engine.connect() as connection:
        connection.execute(f"UPDATE veiculos SET ativo = False WHERE placa = {placa}")

    return f"Veículo com placa {placa} foi retirado da frota com sucesso!"

@app.route("/adicionar_veiculo", methods=["POST"])
def adicionar_veiculo():
    data = request.json
    placa = data.get('placa')
    tipo_comb = data.get('tipo_comb')
    cor = data.get('cor')
    marca = data.get('marca')
    modelo = data.get('modelo')
    kms = data.get('kms')
    vlr_car = data.get('vlr_car')
    ar_cond = data.get('ar_cond')
    ativo = data.get('ativo', True) 
    query = f"""INSERT INTO veiculos (placa, tipo_comb, cor, marca, modelo, kms, vlr_car, ar_cond, ativo) VALUES
            ('{placa}', '{tipo_comb}', '{cor}', '{marca}', '{modelo}', {kms},
            {vlr_car}, {ar_cond}, {ativo})"""
    
    with engine.connect() as connection:
        connection.execute(query)

    return "Veículo adicionado com sucesso!"
# =========================================================== 


# =================== ROTAS VEICULOS =================== 
@app.route("/alterar_endereco_cliente/<int:id_cliente>", methods=["PUT"])
def alterar_endereco_cliente(id_cliente):
    data = request.json
    novo_endereco = data.get('endereco')
    
    with engine.connect() as connection:
        connection.execute(
            f"UPDATE funcionarios SET endereco = '{novo_endereco}' WHERE id_cliente = {id_cliente}"
        )

    return f"Endereço do cliente com ID {id_func} alterado com sucesso!"

# =================== ROTAS CLIENTES =================== 
@app.route("/cadastrar_cliente", methods=["POST"])
def cadastrar_cliente():
    data = request.json
    dt_nasc = data.get('dt_nasc')
    cnh = data.get('cnh')
    nome = data.get('nome')
    cpf = data.get('cpf')
    endereco = data.get('endereco')

    query = text("INSERT INTO clientes (dt_nasc, cnh, nome, cpf, endereco) "
                 "VALUES (:dt_nasc, :cnh, :nome, :cpf, :endereco)")

    with engine.connect() as connection:
        connection.execute(query,{
            'dt_nasc': dt_nasc,
            'cnh': cnh,
            'nome': nome,
            'cpf': cpf,
            'endereco': endereco
        })

    return jsonify({"message": "Cliente cadastrado com sucesso!"})
# =========================================== 


@app.route("/")
def hello_world():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True, port=8080)
