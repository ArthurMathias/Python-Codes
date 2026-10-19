print("Analisador de Triângulos\n")
print("-" * 20)

r1 = int(input("Digite o valor da primeira reta: "))
r2 = int(input("Digite o valor da segunda reta: "))
r3 = int(input("Digite o valor da terceira reta: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os segmentos acima podem formar um triângulo.")
else:
    print("Os segmentos acima não podem formar um triângulo.")