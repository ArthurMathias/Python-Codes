print("Calculando o valor do aumento salarial\n")
print("-" * 20)

while True:
    salario = float(input("Digite o salário atual: R$"))
    aumento = int(input("Digite o aumento em porcentagem: "))
    novo_salario = salario + (salario * aumento / 100)
    print("O novo salário com aumento de {}% é: R${:.2f}".format(aumento, novo_salario))