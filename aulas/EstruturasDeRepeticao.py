#REPETIÇÃO WHILE -> Enquanto
#Estruturas de repetição
#Laços de repetição
#Loop
from operator import index

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
# lista_de_alunos = ["aluno1", "aluno2", "aluno3", "aluno4"] #mutável
#
# print("Lista antiga", lista_de_alunos)
#
# lista_de_alunos[0] = "Fulano" #troca o aluno 1 da lista
#
# lista_de_alunos.append("aluno5") #modificação
#
# print("Lista atualizada", lista_de_alunos)
#
#
# #Criando uma Tupla
# tupla_de_alunos = ["aluno1", "aluno2", "aluno3", "aluno4"] #Imutável
#
#
# # for valor in lista_de_alunos:
# #     print(valor)
#
# #MODIFICANDO TIPOS DE DADOS DA LISTA
# turma_python = [
#     ["Joao", 12, 5.5], # list
#     ("Jose", 0, 10.0), # tuple
#     "Jão"  # string
# ]
# print("Tipo de lista: ",type(turma_python))
# print("Tipo do primeiro valor: ",type(turma_python[0]))
# print("Tipo do segundo valor: ",type(turma_python[1]))
# print("Tipo do terceiro valor: ",type(turma_python[2]))


#FUNÇÕES DE LISTAS
#        index  0 1 2 3 4 5 6 7 8 9
list_numeros = [1,2,3,4,5,6,7,3,9,10]

for numero in list_numeros:
    if numero ==3:
        list_numeros.remove(3)

print(list_numeros)