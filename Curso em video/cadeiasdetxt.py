frase = "Curso em Vídeo Python"
print(frase[9])
print("-" * 20)
print("Retornando a palavra Vídeo")
print(frase[9:14]) # Retorna a palavra Vídeo
print("-" * 20)

print("Tamanho da frase: {}".format(len(frase)))
counter = frase.count('o') # Conta quantas vezes a letra 'o' aparece na frase
print("Quantidade de vezes que 'o' aparece na frase: {}".format(counter))
print("-" * 20)

ver = "Curso" in frase
if ver == True:
    print("Sim, a palavra Curso está na frase")