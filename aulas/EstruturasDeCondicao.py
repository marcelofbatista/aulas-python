#IF e ELSE -> SE e SENÃO
#CASE SENSITIVE -> E != e

"""
if 1 == 1: #executa se a resposta boleana for True
    print("Verdadeiro")

idade = 80
#criando uma condição na execução do código
if idade >= 18: #executa se a resposta boleana for True
    print("Pode entrar")
#if idade < 18:  # executa se a resposta boleana for True
    if idade > 65:
        print("Não pode entrar, senhor")

else: #executa se a condição do IF for False
    print("Não pode entrar")

"""
#ELIF
idade = int(input('Digite sua idade: '))

if idade >= 18:  # executa se a resposta boleana for True
        if idade > 65:
            print("Não pode entrar, senhor")
        else:
            print("Pode entrar")
elif idade < 5:  # executa se a condição do IF for False
    print("Não pode entrar sozinho")
else:
    print("Não pode entrar, é menor de idade")

nome = input('Digite seu nome: ')
if nome == "":
    print("Por favor, digite um nome válido.")
else:
    print("Olá "+ nome +"! Seja bem vindo a nossa balada")