#Pintando Parede
print("Pintando Parede\n")
print("-" * 20)

while True:
    larg = float(input('Largura da parede: '))
    alt = float(input('Altura da parede: '))
    area = larg * alt

    print("Sua parede tem a dimensão de {}x{} e sua área é de {}m².".format(larg, alt, area))
    tinta = area / 2
    print("Para pintar essa parede, você precisará de {:.1f}l de tinta.".format(tinta))

    print("-\n" * 20)