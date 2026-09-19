#validação de dados


#verificar se é número inteiro ou real
n = float(input('Digite um número: '))
print(type(n))

#verificar se é número
m = input('Digite algo: ')
print(m.isnumeric())

#verificar se é letra
l = input('Digite algo: ')
print(l.isalpha())

#verificar se é alfanumérico (ver se possui letras e números) - caso não escreva nada, retorna False
k = input('Digite algo: ')
print(k.isalnum())


#EXEMPLO DE VALIDAÇÃO DE DADOS
idade = input('Digite sua idade: ')

if idade.isnumeric():
    print('Entrada válida!')
else:
    print('Digite apenas números!')

