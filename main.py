def exibir_opcoes():
    print("========================")
    print("1. Cadastro de Pedidos")
    print("2. Cadastro de Entregadores")
    print("3. Atualização dos Pedidos")
    print("4. Consulta")
    print("5. Relatórios Operacionais")
    print("6. Finalizar sistema")
    print("========================")
    opcao = int(input("Escolha uma opção: "))
    try:
        match opcao:
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                finalizar_sistema()
            case _:
                print("Opção Inválida!")
    except:
        print("Opção Inválida!")

def finalizar_sistema():
    print("========================")
    print("Finalizando o sistema...")
    print("========================")

exibir_opcoes()
