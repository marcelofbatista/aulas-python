#REPETIÇÃO WHILE -> Enquanto
#Estruturas de repetição
#Laços de repetição
#Loop

# ano_nascimento = 2004
# ano_final = 2077
#
# print("O ano atual é:", ano_nascimento)
#
# idade = 0
# while ano_nascimento <= ano_final:
#     idade += 1
#     print(idade)
#
#     if (ano_nascimento == ano_final):
#         print("O anual atual é: ", ano_nascimento)
#     ano_nascimento +=1

# tentativas = 3
# fichas = 1
# while fichas != 0:
#     print(f"Você tem {fichas} fichas")
# while True:
#     print(f"Você tem {tentativas} tentativas")
#     opcao = input("Escolha uma opção:")
#     if opcao == "1":
#         print("Você ganhou")
#         break
#     elif tentativas ==1:
#         print("Você perdeu")
#         break
#     else:
#         tentativas -= 1

#   ite, (variável) objeto, função, lista
# for numero_secreto in range(1,11):
#     numero_digitado = int(input("Digite um número: "))
#
#     if numero_secreto == numero_digitado:
#         print("Você ganhou.")


#REPETIÇÃO FOR (para)
#criando uma lista
#               index  0       1          2        3
lista_de_alunos = ["aluno1", "aluno2", "aluno3", "aluno4"]
for valor in lista_de_alunos:
    print(valor)

