from menu import *
from operations import *

a = Menu("Cadstrar Usuário", "asdfsdf")
sair = True

while (sair):
    menu_inicial = Menu(
            #sair
            "Sair",
            #clientes
            "Adicionar cliente",
            "Listar clientes",
            "Alterar endereço de cliente",

            #funcionarios 
            "Adicionar funcionario",
            "Listar funcionarios",
            "Alterar endereço de funcionario",
            "Demitir funcionario",
            "Promover funcionario", 

            #veículos 
            "Adicionar veículo",
            "Listar veículos",
            "Tirar Veículo frota"
            )
            # alugar veiculo
            # ver veiuclos disponiveis

    menu_inicial.interface()
    escolha = menu_inicial.input()
    
    match escolha:
        case 0:
            print("Saindo do aplicativo")
            sair = False;
        case 1:
            print(cadastrar_cliente())
        case 2:
            get_all_clientes()
        case 3:
            get_all_clientes()
            print(alterar_endereco_cliente())
        case 4:
            print(cadastrar_funcionario())
        case 5:
            print(get_all_funcionarios())
        case 6:
            print(alterar_endereco_funcionario())
        case 7:
            print(demitir_funcionario())
        case 8:
            print(promover_funcionario())
        case 9:
            print(adicionar_veiculo())
        case 10:
            print(get_all_veiculos())
        case 11:
            print(tirar_veiculo_frota())

