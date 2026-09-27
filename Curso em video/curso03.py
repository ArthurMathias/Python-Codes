# operadores aritméticos

# centralizado
nome = input("Qual é o seu nome? ")
print("Prazer em te conhecer, {:=^20}".format(nome))


# para a esquerda
nome1 = input("Qual é o seu nome? ")
print("Prazer em te conhecer, {:=<20}".format(nome1))

# para a direita
nome2 = input("Qual é o seu nome? ")
print("Prazer em te conhecer, {:=>20}".format(nome2))

numero = int(input("Digite um número: "))
print(
    'O número digitado foi {} e seu antecessor é {} e o sucessor é {}'.format(
        numero, (numero - 1), (numero + 1))
)

# duas formas
numero1 = int(input("Digite um número: "))
print("O Dobro de {} é {}, o Triplo é {} e a Raiz Quadrada é {}".format(
    numero1,
    (numero1 * 2),
    (numero1 * 3),
    (numero1 ** (1/2))
))

numero2 = int(input("Digite um número: "))

dobro = numero2 * 2
triplo = numero2 * 3
raiz = numero2 ** (1/2)

print("O Dobro de {} é {}, o Triplo é {} e a Raiz Quadrada é {}".format(
    numero2, dobro, triplo, raiz))
