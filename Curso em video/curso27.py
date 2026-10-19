print("Radar eletrônico")

km = int(input("Qual é a velocidade atual do carro? "))
multa = (km - 80) * 7
if km > 80:
    print("Você foi multado em R$ {}".format(multa))
else:
    print("Você está dentro do limite de velocidade. Tenha um bom dia!")
