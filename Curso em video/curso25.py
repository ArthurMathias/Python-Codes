print("Analisando o seu nome\n")

nome = str(input("Digite o seu nome completo: ")).strip().upper()
print("Seu primeiro nome é {}".format(nome.split()[0]))
print("Seu último nome é {}".format(nome.split()[-1]))