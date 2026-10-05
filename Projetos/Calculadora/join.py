
print('\n=== CADASTRO ===')
#nome do usuário
usuario_cadastrado = input('Crie seu usuário: ')
if usuario_cadastrado.isalnum():
    print('Nome válido!')

if len(usuario_cadastrado) < 5:
    print('Nome de usuário muito curto! Deve ter no mínimo 5 caracteres.')


senha_cadastrada = input('Crie sua senha: ')
if senha_cadastrada.isalnum():
    print('Senha válida!')

if len(senha_cadastrada) < 8:
    print('Senha muito curta! Deve ter no mínimo 8 caracteres.')

print('\nCadastro realizado com sucesso!')

print('\n=== LOGIN ===')

usuario = input('Usuário: ')
senha = input('Senha: ')

if usuario == usuario_cadastrado and senha == senha_cadastrada:
    print('\nLogin realizado!')
    import calculadora
else:
    print('Usuário ou senha incorretos!')

