
import random
import math

print("=" * 30)
print("       QUIZ DOS AMIGOS")
print("=" * 30)

nome = input("Qual é o seu nome? ").strip().title()
print(f"\nBem-vindo ao quiz, {nome}!")

# Lista de perguntas
perguntas = [
    {
        "pergunta": "Em que ano nasceu o criador deste quiz?",
        "resposta": "2010"
    },
    {
        "pergunta": "Quanto é 3 * 5 + 4 ** 2?",
        "resposta": "31"
    },
    {
        "pergunta": "Qual é a primeira letra de PYTHON?",
        "resposta": "P"
    },
    {
        "pergunta": "Quanto é a raiz quadrada de 81?",
        "resposta": "9"
    },
    {
        "pergunta": "Quantos caracteres tem a palavra Python?",
        "resposta": "6"
    }
]

# Embaralha as perguntas
random.shuffle(perguntas)

pontos = 0

for item in perguntas:
    tentativas = 3

    print("\n" + "-" * 30)
    print(item["pergunta"])

    while tentativas > 0:
        resposta = input("Sua resposta: ").strip()

        if resposta.lower() == item["resposta"].lower():
            print("Você acertou!")
            pontos += 1
            break
        else:
            tentativas -= 1

            if tentativas > 0:
                print(
                    f"Você errou! "
                    f"Tentativas restantes: {tentativas}"
                )
            else:
                print("Suas tentativas acabaram!")
                print(f"Resposta correta: {item['resposta']}")

print("\n" + "=" * 30)
print(f"Fim do quiz, {nome}!")
print(f"Pontuação: {pontos}/{len(perguntas)}")

porcentagem = (pontos / len(perguntas)) * 100
print(f"Você acertou {porcentagem:.0f}% das perguntas.")

if pontos == len(perguntas):
    print("PERFEITO! Você acertou tudo!")
elif pontos >= 3:
    print("Muito bem! Você está aprendendo!")
else:
    print("Continue praticando. Você vai melhorar!")

print("=" * 30)

        



