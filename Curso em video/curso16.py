import math
print("Seno, Cosseno e Tangente\n")
print("-" * 30)

seno = float(input("Digite o valor do ângulo em graus: "))
if seno < 0 or seno > 360:
    print("Erro: O valor do ângulo deve estar entre 0 e 360 graus.")
    exit()
else:
    print("O valor do seno é: {:.2f}".format(math.sin(math.radians(seno))))
cosseno = float(input("Digite o valor do ângulo em graus: "))
if cosseno < 0 or cosseno > 360:
    print("Erro: O valor do ângulo deve estar entre 0 e 360 graus.")
    exit()
else:
    print("O valor do cosseno é: {:.2f}".format(math.cos(math.radians(cosseno))))
tangente = float(input("Digite o valor do ângulo em graus: "))
if tangente < 0 or tangente > 360:
    print("Erro: O valor do ângulo deve estar entre 0 e 360 graus.")
    exit()
else:
    print("O valor da tangente é: {:.2f}".format(math.tan(math.radians(tangente))))