print("Primeira e última ocorrência de uma string\n")

frase = str(input("Digite uma frase: ")).strip()
print("A letra A aparece {} vezes na frase".format(frase.upper().count("A")))
print("A primeira letra A aparece na posição {}".format(frase.upper().find("A")+1))
print("A última letra A aparece na posição {}".format(frase.upper().rfind("A")+1))
