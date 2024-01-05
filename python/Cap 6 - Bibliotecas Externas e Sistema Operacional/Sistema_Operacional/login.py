import getpass

usuario = getpass.getuser()
senha = getpass.getpass("Digite sua senha:...")

if usuario == 'andre' and senha == 'teste':
    print("Bem-vindo!")
else:
    print("Você não tem acesso!")