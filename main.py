pedidos = []
entregadores = []


def exibir_opcoes():
    print("========================")
    print("1. Cadastro de Pedidos")
    print("2. Cadastro de Entregadores")
    print("3. Atualização dos Pedidos")
    print("4. Consulta")
    print("5. Relatórios Operacionais")
    print("6. Finalizar sistema")
    print("========================")

def finalizar_sistema():
    print("========================")
    print("Finalizando o sistema...")
    print("========================")

def cadastro_pedidos():
    print(f"\nVocê escolheu a opção: 1. Cadastrar Pedidos\n")
    id_pedido = input("Digite o ID do pedido: ")
    nome_cliente = input("Digite seu nome: ")
    endereco = input("Digite o endereço: ")
    prioridade = int(input("Digite qual a prioridade (1 - Alta, 2 - Normal): "))
    descricao_pedido = input("Digite a descrição do pedido: ")
    status_pedido = int(input("Digite o status do pedido (1 - Pendente, 2 - Em Rota, 3 - Entregue e 4 - Cancelado): "))
    id_entregador = input("Digite o ID do entregador: ")

    pedidos.append({
        "id_pedido": id_pedido,
        "nome_cliente": nome_cliente,
        "endereco": endereco,
        "prioridade": prioridade,
        "descricao_pedido": descricao_pedido,
        "status_pedido": status_pedido,
        "id_entregador": id_entregador})
    
    print(pedidos)

def cadastro_entregadores():
    print(f"Você escolheu a opção: 2. Cadastro de Entregadores")
    id_entregador = input("Digite o ID do entregador: ")
    nome_entregador = input("Digite o nome do entregador: ")
    veiculo = int(input("Digite qual é o veículo (1 - Carro, 2 -  Van, 3 - Moto): "))
    disponibilidade = input("Digite qual a disponibilidade do entregador: ")

    entregadores.append({
        "id_entregador": id_entregador,
        "nome_entregador": nome_entregador,
        "veiculo": veiculo,
        "id_pedido_nao_entregue": [],
        "disponibilidade": disponibilidade
    })

def atualizacao_pedidos():
    print(f"\nVocê escolheu a opção: 3. Atualização dos Pedidos\n")
    print("====================================")
    print("1. Alterar status do pedido")
    print("2. Cancelar Pedido")
    print("3. Associar entregadores a pedidos")
    print("4. Remover associação de entregador")
    print("5. Voltar ao menu")
    print("====================================")

    try:
        opcao_atualizacao_pedidos = int(input("Escolha uma opção: "))
        while opcao_atualizacao_pedidos != 5:
            match opcao_atualizacao_pedidos:
                case 1:
                    pass
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    pass
                case 5:
                    print("Voltando ao menu...")
                    main()
                case _:
                    print("Opção Inválida!")

            opcao_atualizacao_pedidos = int(input("Escolha uma opção: "))
    except:
        print("Opção Inválida!")


def consuta_informacoes():
    print(f"\nVocê escolheu a opção: 4. Consulta de informações\n")
    print("============================")
    print("1. Pedidos entregues")
    print("2. Pedidos pendentes")
    print("3. Buscar pedido por ID")
    print("4. Entregadores disponíveis")
    print("5. Entregas realizadas")
    print("6. Voltar ao menu")
    print("============================")

    try:
        opcao_consulta_informacoes = int(input("Escolha uma opção: "))
        match opcao_consulta_informacoes:
            case 1:
                cadastro_pedidos()
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                print("Voltando ao menu...")
                main()
            case _:
                print("Opção Inválida!")
    except:
        print("Opção Inválida!")

def relatorios_operacionais():
    print(f"\nVocê escolheu a opção: 5. Relatórios operacionais\n")
    print("===========================================")
    print("1. Total de pedidos")
    print("2. Quantidade de pedidos")
    print("3. Entregador com maior número de entregas")
    print("4. Pedidos com alta prioridade")
    print("5. Voltar ao menu")
    print("===========================================")

    try:
        opcao_relatorios_operacionais = int(input("Escolha uma opção: "))
        match opcao_relatorios_operacionais:
            case 1:
                cadastro_pedidos(opcao_relatorios_operacionais)
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                print("Voltando ao menu...")
                main()
            case _:
                print("Opção Inválida!")
    except:
        print("Opção Inválida!")


def escolher_opcao():
    try:
        opcao = int(input("Escolha uma opção: "))
        while opcao != 6:
            match opcao:
                case 1:
                    cadastro_pedidos()
                case 2:
                    cadastro_entregadores()
                case 3:
                    atualizacao_pedidos()
                case 4:
                    consuta_informacoes()
                case 5:
                    relatorios_operacionais()
                case 6:
                    finalizar_sistema()
                case _:
                    print("Opção Inválida!")
            
            opcao = int(input("Escolha uma opção: "))
    except:
        print("Opção Inválida!")

def main():
    exibir_opcoes()
    escolher_opcao()

main()
