from random import shuffle
print("Ordem de apresentação\n")
print("-" * 30)

pessoa_1 = input("Digite o nome da primeira pessoa: ")
pessoa_2 = input("Digite o nome da segunda pessoa: ")
pessoa_3 = input("Digite o nome da terceira pessoa: ")
pessoa_4 = input("Digite o nome da quarta pessoa: ")
lista = [pessoa_1, pessoa_2, pessoa_3, pessoa_4]
shuffle(lista)
print("A ordem de apresentação será:")
print(lista)