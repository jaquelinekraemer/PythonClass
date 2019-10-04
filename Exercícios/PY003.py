# 29/09/2019

# Criar um programa que:
# 1. Cadastre usuário e senha.
# 2. Liste usuários cadastrados e suas respectivas senhas.
# 3. Efetue login, validando usuário e senha.
# Obs: O programa deve apresentar um menu para que o usuário possa realizar a ação que
# desejar e no momento em que desejar.

cad_usuario = []
cad_senha = []
opcao = 0


while opcao != 4:

    print('''MENU
    [1] Cadastrar usuário e senha
    [2] Exibir usuários e senhas cadastradas
    [3] Fazer login
    [4] Sair do programa''')

    opcao = int(input('Selecione uma opção do MENU: '))

    if opcao == 1:
        cad_usuario.append(input('Informe o seu usuário: '))
        cad_senha.append(input('Informe a sua senha: '))
        print('Os usuários e as suas respectivas senhas cadastradas são: \n Usuário: {}\nSenha: {}'.format(cad_usuario, cad_senha))  

    elif opcao == 2:
        print('Usuários cadastrados: {}'.format(cad_usuario))
        print('Senhas cadastradas: {}'.format(cad_senha))
    
    elif opcao == 3:
        usuario = input('Digite o seu usuário cadastrado: ')
        senha = input('Digite a sua senha cadastrada: ')
        if cad_usuario == usuario and cad_senha == senha:
            print('Login efetuado com sucesso.')
        else:
            print('Opção inválida. Tente novamente')
print('Programa finalizado, volte sempre!')