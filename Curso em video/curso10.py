print("Calculando Descontos\n")
print("-" * 20)
while True:
    valor = float(input("Digite o valor do produto: R$"))
    desconto = int(input("Digite o desconto em porcentagem: "))
    valor_final = valor - (valor * desconto / 100)
    print("O valor do produto com desconto de {}% é: R${:.2f}".format(desconto, valor_final))

print("-\n" * 20)