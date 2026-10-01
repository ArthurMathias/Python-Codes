print("Conversor de moedas\n")
print("-" * 20)


while True:
    moeda = input("Digite a moeda que deseja converter (dólar, euro, libra): ").lower()
    if moeda == "dólar":
        valor = float(input("Digite o valor em reais: R$ "))
        cotacao = 5.25  # Cotação do dólar em reais
        convertido = valor / cotacao
        print(f"R$ {valor:.2f} equivalem a US$ {convertido:.2f}")

    elif moeda == "euro":
        valor = float(input("Digite o valor em reais : R$ "))
        cotacao = 5.50  # Cotação do euro em reais
        convertido = valor / cotacao
        print(f"R$ {valor:.2f} equivalem a € {convertido:.2f}")

    elif moeda == "libra":
        valor = float(input("Digite o valor em reais: R$ "))
        cotacao = 6.20  # Cotação da libra em reais
        convertido = valor / cotacao
        print(f"R$ {valor:.2f} equivalem a £ {convertido:.2f}")

    else:
        print("Moeda inválida. Por favor, digite 'dólar', 'euro' ou 'libra'.")
print("-" * 20)