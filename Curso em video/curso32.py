print("Aumentos Salarial\n")
print("-" * 20)

salario = int(input("Qual é o salário atual? R$"))
novo_salario = (salario * 0.15) + salario

if salario <= 5000:
    novo_salario = (salario * 0.10) + salario

print("O novo salário é {}".format(novo_salario))
