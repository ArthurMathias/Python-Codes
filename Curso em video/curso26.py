print("Jogo da adivinhação")
from random import randint
from time import sleep
print("-" * 20)

numero_aleatorio = int(input("Digite um número de 0 a 5: "))
print("Processando", end="", flush=True)
for _ in range(3):
    sleep(0.5)
    print(".", end="", flush=True)
print()
sleep(2)
numero_secreto = randint(0, 5)
if numero_aleatorio == numero_secreto:
    print("Parabéns! Você acertou o número.")
else:
    print("Que pena! Você errou.")