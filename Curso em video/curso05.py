#Calcular a média

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

m = (n1 + n2) / 2

print(f"A média entre {n1} e {n2} é: {m:.1f}")

if m >= 6:
    print("O Aluno foi aprovado.")
else:
    print("O Aluno foi reprovado.")