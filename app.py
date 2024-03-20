from getpass import getpass


def verificar_usuario(nome, senha, arquivo):
    try:
        with open(arquivo, 'r') as f:
            for linha in f:
                dados = linha.strip().split(',')
                if dados[0] == nome and dados[1] == senha:
                    return True
        return False
    except FileNotFoundError:
        print("O arquivo não foi encontrado.")
        return False


def bem_vindo():
    mensagem = 'Bem-vindo ao sistema de Cadastro!'
    print('*' * len(mensagem))
    print(mensagem)
    print('*' * len(mensagem))


def opcoes():
    opcoes = {
        '1': 'Fazer Login',
        '2': 'Cadastrar novo usuário'
        }
    for key, value in opcoes.items():
        print(f'[{key}] - {value}')


def sistema():
    while True:
        escolha = input('Digite a sua opção: ')
        if escolha == '1':
            nome = input(str('Digite o nome: '))
            senha = getpass('Digite a senha: ')
            usuarios = "usuarios.txt"
            if verificar_usuario(nome, senha, usuarios):
                print(f'Olá {nome}, você fez login com sucesso!')
                break
            else:
                print(f'O usuário {nome}, não existe!')
        elif escolha == '2':
            while True:
                novo_nome = input(str('Digite o nome para o novo usuário: '))
                nova_senha = getpass('Digite a senha para o novo usuário: ')
                print(f'O usuário {novo_nome} foi registado com sucesso!')
                with open('usuarios.txt', 'a') as arquivo:
                    arquivo.write(f'{novo_nome},{nova_senha}' + '\n')
                novo_cadastro = input('Deseja cadastrar mais algum usuário? [S/N]: ')
                if novo_cadastro.upper() == 'N':
                    break
        else:
            print('Escolha uma das opções apresentadas!')


bem_vindo()
opcoes()
sistema()
