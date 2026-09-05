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


switch case (escolha caso)
match case no python
switch case é usado para várias respostas
para duas respostas (boleanos) usa o if + else

print("1 + 1 é igual a: \na)1 \nb)2 \nc)3 \nd)4")
primeira_resposta = input('Digite sua primeira resposta: ')
match primeira_resposta: #espera um string
    case "a":
        print("Resposta errada")
    case "b":
        print("Resposta correta")
    case "c":
        print("Resposta errada")
    case "d":
        print("Resposta errada")
    case _: #significa valor default, ou seja, valor padrão
        print("Resposta inválida")


#VÁRIAS OPÇÕES EM UM CASE
match dia:
    case "sabado"
        print("Final de semana")
    case "segunda"
        print("Dia de semana")

dia = input('Digite o dia da semana: ')
match dia:
    case "sábado" | "domingo":
        print("Final de semana")
    case "segunda" | "terça" | "quarta" | "quinta" | "sexta":
        print("Dia de semana")
    case _:
        print("Resposta errada")

"""
idade = 10
match idade:
    case n if n < 10:
        print("Você tem menos de 10 anos.")
    case n if (n > 10 and n < 18):
        print("Você tem mais de 10 anos.")
    case n if n > 18:
        print("Você tem mais de 18 anos.")
    case n if n == 18:
        print("Você tem 18 anos.")