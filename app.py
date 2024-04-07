impot psycopg2
import sys
import ppri
from flask import Flask

app = Flask(_name_)
conn_string = "postgresql://trab_banco_owner:5kYVI6gRfHlK@ep-nameless-tooth-a5fq2x2q.us-east-2.aws.neon.tech/trab_banco?sslmode=require"
conn = psycopg2.connect(conn_string)
cursor = conn.cursor()

@app.route("/get_funcionario/<int: id_func>", methods["GET"])
def get_func(id_func):
    return "<p>Hello, World!</p>"

@app.route("/")
def hello_world():

def main():

