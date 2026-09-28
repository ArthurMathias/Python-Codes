print("\nCalculadora Simples")
print("Projeto criado 16/09/2026")

while True:
    print("Escolha a operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Dobro ou Triplo")

    opcao = input("Digite a operação desejada: ")

    try:
        num1 = float(input("Digite o primeiro número: "))
    except ValueError:
        print("Erro: O primeiro número não é válido.")
    exit()

    try:
        num1 = float(input("Digite o primeiro número: "))
    except ValueError:
        print("Erro: O primeiro número não é válido.")
        exit()

    if opcao != "5":
        try:
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Erro: O segundo número não é válido.")
            exit()
    print()

    if opcao == "1":
        print(f"A soma de {num1} + {num2} é: {num1 + num2}")
    elif opcao == "2":
        print(f"A subtração de {num1} - {num2} é: {num1 - num2}")
    elif opcao == "3":
        print(f"A multiplicação de {num1} * {num2} é: {num1 * num2}")
    elif opcao == "4":
        if num2 == 0:
            print("Divisão por zero não é permitida.")
        else:
            print(f"A divisão de {num1} / {num2} é: {num1 / num2}")
    elif opcao == "5":
        print(f"\nO dobro de {num1} é: {num1 * 2}")
        print(f"\nO triplo de {num1} é: {num1 * 3}")
    else:
        print("Opção inválida. Por favor, escolha uma operação válida.")