print("-" * 30)
print("Aluguel de Carros\n")
print("-" * 30)
#-------------------------------------
while True:
    print("Modelos disponíveis para aluguel:")
    print("1. Gol")
    print("2. Uno")
    print("3. Civic")
    print("-" * 30)
    carro = input("Digite o modelo do carro que deseja alugar: ")

    if carro == "Gol" or carro == "1":
        dias = int(input("Digite a quantidade de dias alugados: "))
        km_rodados = float(input("Digite a quantidade de quilômetros rodados: "))

        valor_dias = dias * 60
        valor_km = 0.15 * km_rodados
        valor_total = valor_dias + valor_km

        print(f"\nO valor total a ser pago é: R${valor_total:.2f}")
        break  # Sai do loop após calcular o valor para o Gol

    elif carro == "Uno" or carro == "2":
        dias = int(input("Digite a quantidade de dias que deseja alugar o carro: "))
        km_rodados = float(input("Digite a quantidade de quilômetros rodados: "))

        valor_dias = dias * 50
        valor_km = 0.12 * km_rodados
        valor_total = valor_dias + valor_km

        print(f"\nO valor total a ser pago é: R${valor_total:.2f}")
        break  # Sai do loop após calcular o valor para o Uno
    elif carro == "Civic" or carro == "3":
        dias = int(input("Digite a quantidade de dias que deseja alugar o carro: "))
        km_rodados = float(input("Digite a quantidade de quilômetros rodados: "))

        valor_dias = dias * 100
        valor_km = 0.20 * km_rodados
        valor_total = valor_dias + valor_km

        print(f"\nO valor total a ser pago é: R${valor_total:.2f}")
        break  # Sai do loop após calcular o valor para o Civic
    else:
        print("Modelo de carro inválido. Por favor, escolha um modelo disponível.")
