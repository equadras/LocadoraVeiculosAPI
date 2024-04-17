from menu import *
from operations import *

a = Menu("Cadstrar Usuário", "asdfsdf")
sair = True


while (sair):
    menu_inicial = Menu("Cadastrar Usuario", "Cadastrar Funcionario")
    menu_inicial.interface()
    escolha = menu_inicial.input()
    

    match escolha:
        case 0:
            print(cadastrar_cliente())
        case 1:
            print(cadastrar_funcionario())


