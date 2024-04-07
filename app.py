import sys
from flask import Flask
from psutil import process_iter
from signal import SIGTERM
from sqlalchemy import create_engine

app = Flask(__name__)

@app.route("/get_funcionario/<int:id_func>", methods=["GET"])
def get_func(id_func):
    with engine.connect() as connection:
        result = connection.execute(f"SELECT * FROM funcionario WHERE id = {id_func}")
        funcionario = result.fetchone()
    if funcionario:
        return f"Funcionário ID: {funcionario[0]}, Nome: {funcionario[1]}, Sobrenome: {funcionario[2]}"
    else:
        return "Funcionário não encontrado"

@app.route("/")
def hello_world():
    return "Hello, World!"

if __name__ == "__main__":
    engine = create_engine("postgresql://trab_banco_owner:5kYVI6gRfHlK@ep-nameless-tooth-a5fq2x2q-pooler.us-east-2.aws.neon.tech/trab_banco?sslmode=require")
    app.run(debug=True, port=8080)
