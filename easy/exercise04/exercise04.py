# Defina uma senha no código. Peça ao usuário para digitá-la.
# Enquanto errar, continue pedindo. Exiba uma mensagem de boas-vindas ao acertar.


senha = 1234

senha_usuario = int(input("Me informe sua senha: "))

while senha_usuario != senha:
    print("Senha incorreta! Tente novamente.")
    senha_usuario = int(input("Me informe sua senha: "))
else:
    print("Senha correta!")