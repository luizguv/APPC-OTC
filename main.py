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
                cadastro_pedidos(opcao)
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
    print(f"Você escolheu a opção: 1. Cadastrar Pedidos")
    id_pedido = input("Digite o ID do pedido: ")
    nome_cliente = input("Digite seu nome: ")
    endereco = input("Digite o endereço: ")
    prioridade = int(input("Digite qual a prioridade (1 - Alta, 2 - Normal): "))
    descricao_pedido = input("Digite a descrição do pedido: ")
    status_pedido = int(input("Digite o status do pedido (1 - Pendente, 2 - Em Rota, 3 - Entregue e 4 - Cancelado): "))
    id_entregador = input("Digite o ID do entregador: ")

    return id_pedido, nome_cliente, endereco, prioridade, descricao_pedido, status_pedido, id_entregador

def cadastro_entregadores():
    print(f"Você escolheu a opção: 2. Cadastro de Entregadores")
    # ID ENTREGADOR
    nome_entregador = input("Digite o nome do entregador: ")
    veiculo = int(input("Digite qual é o veículo (1 - Carro, 2 -  Van, 3 - Moto): "))
    # ID PEDIDO PENDENTE
    disponibilidade = input("Digite qual a disponibilidade do entregador: ")

    return nome_entregador, veiculo, disponibilidade

def atualizacao_pedidos():
    print(f"Você escolheu a opção: 3. Atualização dos Pedidos")
    alterar_status = int(input("Digite qual o status atual do pedido (1 - Pendente, 2 - Em Rota, 3 - Entregue e 4 - Cancelado): "))


def consuta_informacoes():
    print(f"Você escolheu a opção: 4. Consulta de informações")
    print("1. Pedidos entregues")
    print("2. Pedidos pendentes")
    print("3. Buscar pedido por ID")
    print("4. Entregadores disponíveis")
    print("5. Entregas realizadas")
    print("6. Voltar ao menu")

    opcao_consulta_informacoes = int(input("Escolha uma opção: "))
    try:
        match opcao_consulta_informacoes:
            case 1:
                cadastro_pedidos(opcao_consulta_informacoes)
                return opcao_consulta_informacoes
            case 2:
                pass
                return opcao_consulta_informacoes
            case 3:
                pass
                return opcao_consulta_informacoes
            case 4:
                pass
                return opcao_consulta_informacoes
            case 5:
                pass
                return opcao_consulta_informacoes
            case 6:
                pass
                return opcao_consulta_informacoes
            case _:
                print("Opção Inválida!")
    except:
        print("Opção Inválida!")

def relatorios_operacionais():
    print(f"Você escolheu a opção: 5. Relatórios operacionais")
    print("1. Total de pedidos")
    print("2. Quantidade de pedidos")
    print("3. Entregador com maior número de entregas")
    print("4. Voltar ao menu")

    opcao_relatorios_operacionais = int(input("Escolha uma opção: "))
    try:
        match opcao_relatorios_operacionais:
            case 1:
                cadastro_pedidos(opcao_relatorios_operacionais)
                return opcao_relatorios_operacionais
            case 2:
                pass
                return opcao_relatorios_operacionais
            case 3:
                pass
                return opcao_relatorios_operacionais
            case 4:
                pass
                return opcao_relatorios_operacionais
            case _:
                print("Opção Inválida!")
    except:
        print("Opção Inválida!")

exibir_opcoes()
