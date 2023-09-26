senha_correta = 2002

while True:
    senha_usuario = int(input())
    if senha_usuario != senha_correta:
        print('Senha Invalida')
        continue
    elif senha_usuario == senha_correta:
        print('Acesso Permitido')
        break
