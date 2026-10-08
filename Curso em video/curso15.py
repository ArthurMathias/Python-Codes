from math import hypot

print("Calculando Catetos e Hipotenusa\n")

try:
    cateto_o = float(input("Digite o valor do cateto oposto: "))
    if cateto_o <= 0:
        print("Erro: O valor do cateto oposto deve ser maior que zero.")
        exit()

    cateto_a = float(input("Digite o valor do cateto adjacente: "))
    if cateto_a <= 0:
        print("Erro: O valor do cateto adjacente deve ser maior que zero.")
        exit()
except ValueError:
    print("Erro: O valor digitado deve ser um número.")
    exit()

hipotenusa = hypot(cateto_o, cateto_a)
print("O valor da hipotenusa é: {:.2f}".format(hipotenusa))
