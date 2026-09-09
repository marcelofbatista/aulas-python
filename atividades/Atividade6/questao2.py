"""
Questão 2: Validação de Senha
Escreva um programa que defina uma senha fixa no código (por exemplo, "123456"). Peça para o usuário digitar a senha.
Enquanto a senha digitada não for igual à senha correta, exiba a mensagem: "Senha incorreta. Tente novamente." e peça a senha de novo
(igual ao exemplo do "Joao" visto em aula). Quando o usuário acertar, exiba: "Acesso permitido!".

"""

senha_correta = "123456"
senha_digitada = input("Digite a senha: ")
while senha_digitada != senha_correta:
    senha_digitada = input("Senha incorreta. Tente novamente: ")
print("Acesso permitido!")