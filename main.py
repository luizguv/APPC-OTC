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
                cadastro_pedidos()
                return opcao
            case 2:
                pass
                return opcao
            case 3:
                pass
                return opcao
            case 4:
                pass
                return opcao
            case 5:
                pass
            case 6:
                finalizar_sistema()
                return opcao
            case _:
                print("Opção Inválida!")
    except:
        print("Opção Inválida!")

def finalizar_sistema():
    print("========================")
    print("Finalizando o sistema...")
    print("========================")

def cadastro_pedidos(opcao):
    print(f"Você escolheu a opção: {opcao}")
    print(f"")

exibir_opcoes()
