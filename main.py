from menu import *
from operations import *

a = Menu("Cadstrar Usuário", "asdfsdf")
sair = True


while (sair):
    menu_inicial = Menu("Cadastrar Usuario", "Cadastrar Funcionario", "Promover Funcionario", "Alterar Endereco de Funcionario", "Demitir Funcionario", "Adicionar Veículo")
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
            print(demitir_funcionario())
        case 5:
            print(adicionar_veiculo())
        case 7:
            print(tirar_veiculo_frota())
