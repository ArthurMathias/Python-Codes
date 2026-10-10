print("Analisador de Texto")
from time import sleep

nome = str(input("Digite seu nome completo:")).strip()
print("Analisando seu nome...")
sleep(1)
print("Seu nome em Maiúsculas é {}".format(nome.upper()))
print("Seu nome em Minúsculas é {}".format(nome.lower()))
print("Seu nome tem no total {} letras".format(len(nome)))
print("Seu primeiro nome tem {} letras".format(len(nome.split()[0])))