from flask import Flask, request, jsonify
from py2neo import Graph, Node, Relationship
from datetime import datetime, timedelta, date
from py2neo.data import Node, Relationship

app = Flask(__name__)

# Conectar ao banco de dados Neo4j
graph = Graph('bolt://localhost:7687', auth=("neo4j", "brutebrute"))

# =================== ROTAS FUNCIONARIOS =================== 
@app.route("/get_all_funcionarios", methods=["GET"])
def get_all_funcionarios():
    query = """
    MATCH (f:Funcionario)
    RETURN f.nome AS nome, f.cpf AS cpf, f.cargo AS cargo, f.salario AS salario, 
           f.endereco AS endereco, f.dt_nasc AS dt_nasc, f.ativo AS ativo
    """
    result = graph.run(query)
    funcionarios = [dict(record) for record in result]
    for funcionario in funcionarios:
        if 'dt_nasc' in funcionario and funcionario['dt_nasc']:
            if isinstance(funcionario['dt_nasc'], str):
                try:
                    parsed_date = datetime.strptime(funcionario['dt_nasc'], '%Y-%m-%d').date()
                    funcionario['dt_nasc'] = parsed_date.strftime('%Y-%m-%d')
                except ValueError:
                    pass
            elif hasattr(funcionario['dt_nasc'], 'year'):
                python_date = date(funcionario['dt_nasc'].year, funcionario['dt_nasc'].month, funcionario['dt_nasc'].day)
                funcionario['dt_nasc'] = python_date.strftime('%Y-%m-%d')
    return jsonify(funcionarios)

@app.route("/cadastrar_funcionario", methods=["POST"])
def cadastrar_funcionario():
    data = request.json
    funcionario = Node("Funcionario", nome=data['nome'], cpf=data['cpf'], cargo=data['cargo'],
                       endereco=data['endereco'], salario=data['salario'], dt_nasc=data['dt_nasc'], ativo=True)
    graph.create(funcionario)
    return jsonify({"message": "Funcionário cadastrado com sucesso!"})

@app.route("/promover_funcionario/<string:cpf>", methods=["PUT"])
def promover_funcionario(cpf):
    data = request.json
    novo_cargo = data.get('cargo')
    novo_salario = data.get('salario')

    query = """
    MATCH (f:Funcionario {cpf: $cpf})
    SET f.cargo = $novo_cargo, f.salario = $novo_salario
    RETURN f
    """
    graph.run(query, cpf=cpf, novo_cargo=novo_cargo, novo_salario=novo_salario)
    return f"Dados do funcionário com CPF {cpf} atualizados com sucesso!"

@app.route("/alterar_endereco_funcionario/<string:cpf>", methods=["PUT"])
def alterar_endereco_funcionario(cpf):
    data = request.json
    novo_endereco = data.get('endereco')
    
    query = """
    MATCH (f:Funcionario {cpf: $cpf})
    SET f.endereco = $novo_endereco
    RETURN f
    """
    graph.run(query, cpf=cpf, novo_endereco=novo_endereco)
    return f"Endereço do funcionário com CPF {cpf} alterado com sucesso!"

@app.route("/demitir_funcionario/<string:cpf>", methods=["DELETE"])
def demitir_funcionario(cpf):
    query = """
    MATCH (f:Funcionario {cpf: $cpf})
    SET f.ativo = false
    RETURN f
    """
    graph.run(query, cpf=cpf)
    return f"Funcionário com CPF {cpf} foi demitido com sucesso!"

# =================== ROTAS VEICULOS =================== 
@app.route("/get_all_veiculos", methods=["GET"])
def get_all_veiculos():
    query = """
    MATCH (v:Veiculo)
    RETURN v.placa AS placa, v.tipo_comb AS tipo_comb, v.cor AS cor, v.marca AS marca,
           v.modelo AS modelo, v.kms AS kms, v.vlr_car AS vlr_car, v.ar_cond AS ar_cond, v.ativo AS ativo
    """
    result = graph.run(query)
    veiculos = [dict(record) for record in result]
    return jsonify(veiculos)

@app.route("/tirar_veiculo_frota/<string:placa>", methods=["DELETE"])
def tirar_veiculo_frota(placa):
    query = """
    MATCH (v:Veiculo {placa: $placa})
    SET v.ativo = false
    RETURN v
    """
    graph.run(query, placa=placa)
    return f"Veículo com placa {placa} foi retirado da frota com sucesso!"

@app.route("/adicionar_veiculo", methods=["POST"])
def adicionar_veiculo():
    data = request.json
    veiculo = Node("Veiculo", placa=data['placa'], tipo_comb=data['tipo_comb'], cor=data['cor'],
                   marca=data['marca'], modelo=data['modelo'], kms=data['kms'], vlr_car=data['vlr_car'],
                   ar_cond=data['ar_cond'], ativo=data.get('ativo', True))
    graph.create(veiculo)
    return jsonify({"message": "Veículo adicionado com sucesso!"})

# =================== ROTAS CLIENTES =================== 
@app.route("/get_all_clientes", methods=["GET"])
def get_all_clientes():
    query = """
    MATCH (r:Cliente) 
    return r.nome as nome, r.cnh as cnh, r.cpf as cpf, r.endereco as endereco
    """
    result = graph.run(query).data()
    
    # Check if reservas list is not empty before returning
    if result:
        return jsonify(result)
    else:
        return jsonify({"message": "No reservations found"})


@app.route("/alterar_endereco_cliente/<string:cpf>", methods=["PUT"])
def alterar_endereco_cliente(cpf):
    data = request.json
    novo_endereco = data.get('endereco')

    query = """
    MATCH (c:Cliente {cpf: $cpf})
    SET c.endereco = $novo_endereco
    RETURN c
    """
    result = graph.run(query, cpf=cpf, novo_endereco=novo_endereco).data();
    if result:
        return jsonify({"message": f"Endereço do cliente com CPF {cpf} alterado com sucesso!"}), 200 
    else:
        return jsonify({"message": f"Erro na alteração do endereço"}), 404

@app.route("/cadastrar_cliente", methods=["POST"])
def cadastrar_cliente():
    data = request.json
    nome = data.get('nome')
    cpf = data.get('cpf')
    cargo = data.get('cargo')
    endereco = data.get('endereco')
    salario = data.get('salario')
    dt_nasc = data.get('dt_nasc')

    cliente = Node("Cliente", dt_nasc=data['dt_nasc'], cnh=data['cnh'], nome=data['nome'],
                   cpf  =data['cpf'], endereco=data['endereco'])
    graph.create(cliente)
    return jsonify({"message": "Cliente cadastrado com sucesso!"})

# =================== ROTAS RESERVAS =================== 
@app.route("/fazer_reserva", methods=["POST"])
def fazer_reserva():
    data = request.json
    cpf = data.get("cpf")
    cpf_funcionario = data.get("cpf_funcionario")
    dias = int(data.get("dias"))
    dt_reserva = data.get("dt_reserva")
    dt_devolucao = data.get("dt_devolucao")
    placa = data.get("placa")

    cliente = graph.evaluate("MATCH (c:Cliente {cpf: $cpf}) RETURN c", cpf=cpf)
    if not cliente:
        return jsonify({"error": "Cliente não encontrado"}), 404

    funcionario = graph.evaluate("MATCH (f:Funcionario {cpf: $cpf}) RETURN f", cpf=cpf_funcionario)
    if not funcionario:
        return jsonify({"error": "Funcionário não encontrado"}), 404

    veiculo = graph.evaluate("MATCH (v:Veiculo {placa: $placa}) RETURN v", placa=placa)
    if not veiculo:
        return jsonify({"error": "Carro não encontrado"}), 404

    valor = calcular_valor_reserva(veiculo['vlr_car'], dias)  # Supõe-se que você tenha essa função definida em algum lugar.
    if valor is None:
        return jsonify({"error": "Erro ao calcular o valor da reserva"}), 400

    reserva = Node("Reserva", valor=valor, dt_reserva=dt_reserva, dt_devolucao=dt_devolucao)
    graph.create(reserva)

    graph.create(Relationship(cliente, "FEZ", reserva))
    graph.create(Relationship(funcionario, "PROCESSOU", reserva))
    graph.create(Relationship(reserva, "INCLUI", veiculo))

    return jsonify({"message": "Reserva realizada com sucesso!", "valor": valor}), 200

@app.route("/get_all_reservas", methods=["GET"])
def get_all_reservas():
    query = """
    MATCH (c:Cliente)-->(r:Reserva), (f:Funcionario)-->(r), (r)-->(v:Veiculo)
    RETURN DISTINCT c.nome AS cliente, f.nome AS funcionario, r.valor AS valor,
               r.dt_reserva AS dt_reserva, r.dt_devolucao AS dt_devolucao, v.placa AS placa_veiculo
    """
    result = graph.run(query)
    response = []
    for record in result:
        data = record.data()
        for key in data:
            if data[key] is not None:
                data[key] = str(data[key])
        response.append(data)
    return jsonify(response)

def calcular_valor_reserva(vlr_carro, dias):
    try:
        valor_por_dia = (0.001 * float(vlr_carro)) + 10
        return valor_por_dia * int(dias)
    except ValueError:
        return None  

@app.route("/")
def hello_world():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True, port=8080)
