from menu import *
from operations import *

a = Menu("Cadstrar Usuário", "asdfsdf")
sair = True


while (sair):
    menu_inicial = Menu("Cadastrar Usuario", "Cadastrar Funcionario", "Promover Funcionario", "Alterar Endereco de Funcionario", "todo", "Adicionar Veículo", "Tirar Veículo Frota")
    menu_inicial.interface()
    escolha = menu_inicial.input()
    

    match escolha:
        case 0:
            print(mudar_endereco_cliente())
        case 1:
            print(cadastrar_funcionario())
        case 2:
            print(promover_funcionario())
        case 3:
            print(alterar_endereco_funcionario())
        case 4:
            print("todo")
        case 5:
            print(adicionar_veiculo())
        case 6:
            print(tirar_veiculo_frota())
