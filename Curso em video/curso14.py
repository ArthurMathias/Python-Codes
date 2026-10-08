from math import trunc
num = float(input("Digite um número: "))
print("O número digitado foi {} e a sua porção inteira é {}").format(num, trunc(num))

#sem importação:
num= float(input("Digite um número: "))
print("O número digitado foi {} e a sua porção inteira é {}".format(num, int(num)))