from menu import *
from operations import *

a = Menu("Cadstrar Usuário", "asdfsdf")
sair = True


while (sair):
    menu_inicial = Menu("Cadastrar cliente", "listar clientes", 
            "Mudar endereco de cliente",  "Cadastrar funcionario",
            "Promover funcionario", "alterar endereco de funcionario",
            "Demitir funcionario", "adicionar veiculo", 
            "Listar veiculos", "tirar veiculo da frota")

    menu_inicial.interface()
    escolha = menu_inicial.input()
    

    match escolha:

        case 0:
            print(cadastrar_cliente())
        case 1:
            listar_clientes()
        case 2:
            print(mudar_endereco_cliente())
        case 3:
            print(cadastrar_funcionario())
        case 4:
            print(promover_funcionario())
        case 5:
            print(alterar_endereco_funcionario())
        case 6:
            print(demitir_funcionario())
        case 7:
            print(adicionar_veiculo())
        case 8:
            print(listar_veiculos())
        case 9:
            print(tirar_veiculo_frota())

