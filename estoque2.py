produtos = []  
id_produto = 1  

while True:
    print("\n=== MENU ===")
    print("1 - Cadastrar produto")
    print("2 - Excluir produto")
    print("3 - Relatório de produtos")
    print("4 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("\n--- Cadastro de Produto ---")
        nome = input("Nome do produto: ")
        categoria = input("Categoria: ")
        preco = float(input("Preço: "))
        quantidade = int(input("Quantidade inicial: "))

        produto = {
            "id": id_produto,
            "nome": nome,
            "categoria": categoria,
            "preco": preco,
            "quantidade": quantidade
        }
        produtos.append(produto)
        id_produto += 1
        print("Produto cadastrado com sucesso!")

    elif opcao == "2":
        print("\n--- Exclusão de Produto ---")
        excluir = input("Digite o ID ou nome do produto para excluir: ")
        encontrado = False

        for p in produtos:
            if str(p["id"]) == excluir or p["nome"].lower() == excluir.lower():
                produtos.remove(p)
                print("Produto removido com sucesso!")
                encontrado = True
                break

        if not encontrado:
            print("Produto não encontrado.")

    elif opcao == "3":
        print("\n--- Relatório de Produtos ---")
        if len(produtos) == 0:
            print("Nenhum produto cadastrado.")
        else:
            for p in produtos:
                alerta = ""
                if p["quantidade"] < 5:
                    alerta = "  ESTOQUE BAIXO"
                print(f"ID: {p['id']} | Nome: {p['nome']} | Categoria: {p['categoria']} | "
                      f"Preço: R${p['preco']:.2f} | Quantidade: {p['quantidade']} {alerta}")

    elif opcao == "4":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida, tente novamente.")