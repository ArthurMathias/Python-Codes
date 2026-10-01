# Tabuada

print("Tabuada de um número\n")
print("-" * 20)

while True:
    n = int(input("Digite um número: "))

    for c in range(1, 11):
        print(f"{n} x {c} = {n * c}")

    print("-" * 20)