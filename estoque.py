produtos = {}  
proximo_id = 1

def cadastrar_produto():
    global proximo_id

    print("\n--- Cadastro de Produto ---")
    nome = input("Nome do produto: ")
    categoria = input("Categoria: ")
    preco = float(input("Preço: R$ "))
    quantidade = int(input("Quantidade inicial: "))

    produtos[proximo_id] = {
        "nome": nome,
        "categoria": categoria,
        "preco": preco,
        "quantidade": quantidade
    }

    print(f"\nProduto cadastrado com sucesso! ID: {proximo_id}")
    proximo_id += 1


def excluir_produto():
    print("\n--- Excluir Produto ---")
    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    id_produto = int(input("Digite o ID do produto para excluir: "))

    if id_produto in produtos:
        del produtos[id_produto]
        print("Produto removido com sucesso!")
    else:
        print("ID não encontrado.")


def listar_produtos():
    print("\n--- Relatório de Produtos ---")

    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    for idp, info in produtos.items():
        print(f"\nID: {idp}")
        print(f"Nome: {info['nome']}")
        print(f"Categoria: {info['categoria']}")
        print(f"Preço: R$ {info['preco']:.2f}")
        print(f"Quantidade: {info['quantidade']}")

        if info['quantidade'] < 5:
            print("⚠ ESTOQUE BAIXO!")

    print("\nFim do relatório.\n")


def menu():
    while True:
        print("\n=== ESTOQUE ===")
        print("1 - Cadastrar Produto")
        print("2 - Excluir Produto")
        print("3 - Mostrar Relatório")
        print("4 - Sair")
        
        opc = input("Escolha uma opção: ")

        if opc == "1":
            cadastrar_produto()
        elif opc == "2":
            excluir_produto()
        elif opc == "3":
            listar_produtos()
        elif opc == "4":
            print("Encerrando... até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")


menu()
