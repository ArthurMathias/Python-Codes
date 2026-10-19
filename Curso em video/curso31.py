
print("Maior e menor valor")

valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
valor3 = int(input("Digite o terceiro valor: "))

# Encontrando o maior valor
if valor1 >= valor2 and valor1 >= valor3:
    maior = valor1
elif valor2 >= valor1 and valor2 >= valor3:
    maior = valor2
else:
    maior = valor3

# Encontrando o menor valor
if valor1 <= valor2 and valor1 <= valor3:
    menor = valor1
elif valor2 <= valor1 and valor2 <= valor3:
    menor = valor2
else:
    menor = valor3

print(f"O maior valor é {maior}")
print(f"O menor valor é {menor}")
