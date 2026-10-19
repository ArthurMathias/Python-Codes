print("Custo da viagem!!")

distância = float(input("Qual é a distância da viagem: "))
print("Você está prestes a começar uma viagem")

if distância >= 200:
    preço = 0.45
else:
    preço = 0.50


print("A sua viagem custará R${}".format(preço))