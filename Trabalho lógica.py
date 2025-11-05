pets = []

while True:
    print("\nSejam bem vindos ao pet shop do Alcei Nogueira")
    print("\n--- MENU ---")
    print("1: Adicionar")
    print("2: Renomear")
    print("3: Remover")
    print("4: Buscar")
    print("5: Listar")
    print("0: Sair")
    
    opcao = input("Escolha: ")

    if opcao == "1":
        nome = input("Nome do pet: ")
        pets.append(nome)
        print("Adicionado.")

    elif opcao == "2":
        antigo = input("Renomear qual pet? ")
        if antigo in pets:
            i = pets.index(antigo)
            novo = input("Novo nome: ")
            pets[i] = novo
            print("Atualizado.")
        else:
            print("Pet não encontrado.")

    elif opcao == "3":
        remover = input("Remover qual pet? ")
        if remover in pets:
            pets.remove(remover)
            print("Removido.")
        else:
            print("Pet não encontrado.")

    elif opcao == "4":
        busca = input("Buscar qual pet? ")
        if busca in pets:
            print("Pet encontrado.")
        else:
            print("Pet não encontrado.")

    elif opcao == "5":
        print("Lista:", pets)

    elif opcao == "0":
        print("Saindo...")
        break
    
    else:
        print("Opção inválida.")