print("Conversor de Temperatura\n")
print("-" * 30)

try:
    graus_celsius = float(input("Digite a temperatura em graus Celsius: "))
except ValueError:
    print("Erro: A temperatura digitada não é válida.")
    exit()

graus_fahrenheit = (graus_celsius * 9/5) + 32
print(f"A temperatura em Fahrenheit é: {graus_fahrenheit:.2f}°F")

print("\nConversão concluída com sucesso!")