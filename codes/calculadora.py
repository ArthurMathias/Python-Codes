print("Calculadora Simples")
print()
print("\nProjeto criado 16/09/2026")


print("Escolha a operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = input("Digite a operação desejada: ")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print()

Soma = (num1 + num2)
Subtração = (num1 - num2)
Multiplicação = (num1 * num2)
Divisão = (num1 / num2)

if opcao == "1":
    print(f"A soma de {num1} + {num2} é: {Soma}")
elif opcao == "2":
    print(f"A subtração de {num1} - {num2} é: {Subtração}")
elif opcao == "3":
    print(f"A multiplicação de {num1} * {num2} é: {Multiplicação}")
elif opcao == "4":
    if num2 == 0:
        print("Erro: Divisão por zero não é permitida.")
    else:
        print(f"A divisão de {num1} / {num2} é: {Divisão}")
else:
    print("Opção inválida. Por favor, escolha uma operação válida.")
