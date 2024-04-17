from menu import *
from operations import *

a = Menu("Cadstrar Usuário", "asdfsdf")
sair = True


while (sair):
    menu_inicial = Menu("Cadastrar Usuario", "Mudar Cargo Funcionario")
    menu_inicial.interface()
    escolha = menu_inicial.input()
    

    match escolha:
        case 0:
            print(alterar_endereco_cliente())
        case 1:
            print(mudar_cargo_funcionario())




