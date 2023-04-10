import hashlib

# Leitura do arquivo com as credenciais
with open("credenciais.txt", "r") as arquivo:
    credenciais = arquivo.read().splitlines()

# Lista de usuários
usuarios = [credencial.split(":")[0] for credencial in credenciais]

while True:
    # Verificação do usuário
    login = input("Login (ou digite 'sair' para sair): ")
    if login.lower() == "sair":
        print("Saindo...")
        break
    if login not in usuarios:
        print("Usuário não encontrado!")
    else:
        # Dicionário para armazenar os usuários e senhas
        usuarios_senha = {}
        for credencial in credenciais:
            usuario, senha_hash = credencial.split(":")
            usuarios_senha[usuario] = senha_hash

        # Login do usuário
        senha = input("Senha: ")
        senha_hash = hashlib.sha512(senha.encode("utf-8")).hexdigest()
        if senha_hash == usuarios_senha[login]:
            print("Login realizado com sucesso!")
            break
        else:
            print("Senha incorreta!")
            

