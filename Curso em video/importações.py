import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print(f'A raiz quadrada de {num} é {raiz:.2f}')

import datetime
data_atual = datetime.datetime.now()
print(f'Data e hora atual: {data_atual}')

import random
numero_aleatorio = random.randint(1, 100) 
print(f'Número aleatório entre 1 e 100: {numero_aleatorio}')

from time import sleep
print("Contagem regressiva:")
sleep(1)
print("3...")
sleep(1)
print("2...")
sleep(1)
print("1...")
sleep(1)
print("Parabéns! A contagem regressiva terminou.")


