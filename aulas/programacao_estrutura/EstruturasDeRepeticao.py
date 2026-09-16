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
# list_numeros = [1,2,3,4,5,6,7,3,9,10]
#
# for numero in list_numeros:
#     if numero ==3:
#         list_numeros.remove(3)
#
# print(list_numeros)

# for (item -> variável
#        index    0         1         2
# lista_alunos = ["Joao", "Felipe", "Alberto"]
# num_aluno = 0
# for i in lista_alunos:
#     print(f"Nome do aluno {num_aluno}: {i}")
#     num_aluno += 1


# lista_alunos = ["Joao", "Felipe", "Alberto"]
# num_aluno = 0
# print("ADICIONANDO ALUNOS NA LISTA DE CHAMADA")
# while True: # adicionar alunos
#     aluno = input("Digite o nome do aluno: ")
#     lista_alunos.append(aluno)
#
#     opcao = input("Deseja continuar? [S/N] ")
#     if opcao == "N":
#         break
#
# print("A sua turma ficou com todos esses alunos.")
# for i in lista_alunos: #imprime a lista de alunos total
#     print(f"Nome do aluno {num_aluno} : {i}")
#     num_aluno += 1
#




#REPETIÇÃO FOR (para)

# for (item -> variável temporária) in (lista de valores):
#         index   0        1         2
# lista_alunos = []
# num_aluno = 0
# num_aluno_final = 0
# print("ADICIONANDO ALUNOS NA LISTA DE CHAMADA")
# while True: # sisitema de adição
#     while True: # adicionar alunos
#         aluno = input("Digite o nome do aluno: ")
#         lista_alunos.append(aluno)
#
#         opcao = input("Deseja continuar? [S/N]: ") #finalizar adição
#         if opcao == "N":
#             break
#
#     print("Lista atual dos alunos.")
#     for i in lista_alunos: # imprime a lista de alunos total
#         print(f"Nome do aluno {num_aluno}: {i}")
#         num_aluno += 1
#
#     print("Escolha uma opção:")
#
#     opcao_match = input("a) apagar um aluno da chamada\n"
#                         "b) adicionar um aluno da chamada\n"
#                         "c) finalizar o programa\n")
#
#     match opcao_match:
#         case 'a':
#             aluno_apagado = input("Digite o nome do aluno que deseja apagar: ")
#             lista_alunos.remove(aluno_apagado)
#             break
#         case 'b':
#             aluno_adicionado = input("Digite o nome do aluno que deseja adicionar: ")
#             lista_alunos.append(aluno_adicionado)
#             break
#         case _:
#             break
#
# print("A sua turma ficou com todos esses alunos:")
# for i in lista_alunos: # imprime a lista de alunos total
#     print(f"Nome do aluno {num_aluno_final}: {i}")
#     num_aluno_final += 1

# #   index   0       1           2
# alunos = ["Joao", "Fulano", "Ciclano"]
# #index    0  1  2
# notas = [10, 6, 8]
# #index     0   1   2
# faltas = [15, 20, 25]
# turma_python = [    #lista pai
#     alunos, #0  lista filho
#     notas,  #1  lista filho
#     faltas  #2  lista filho
# ]
#
# for turma in turma_python:
#     for index in turma:
#         if index in alunos:
#             if index == alunos[0]:
#                 print(f"O aluno {index}")
#         if index in notas:
#             if index == notas[0]:
#                 print(f"Tirou exatamente {index} de nota final")
#         if index in faltas:
#             if index == faltas[0]:
#                 print(f"E teve {index} de falta final")
#
#     for index in turma:
#         if index in alunos:
#             if index == alunos[1]:
#                 print(f"O aluno {index}")
#         if index in notas:
#             if index == notas[1]:
#                 print(f"Tirou exatamente {index} de nota final")
#         if index in faltas:
#             if index == faltas[1]:
#                 print(f"E teve {index} de falta final")



# Crie uma lista que ela armazene um número x de funcionários. Usando o while, adicione quantos funcionários quiser.
# Com o for, você irá imprimir duas listas.Uma lista com todos os funcionários que receberão um aumento.
# Outra lista, com todos os funcionários que serão demitidos.
# (Você irá decidir qual funcionário será demitido ou receberá aumento pelo index do funcionário lista[]


# funcionarios = ["Funcionario1", "Funcionario2", "Funcionario3"]
#
# aumento = [funcionarios[0], funcionarios[1], funcionarios[2]]
# demitido = [funcionarios[0], funcionarios[1], funcionarios[2]]
#
# funcionarios.append(input("Digite o nome do funcionário: "))
#
# print(funcionarios)
# print(aumento)
# print(demitido)



funcionarios = []


while True:
    funcionarios.append(input("Digite o nome do funcionário: "))
    opcao = input("Deseja continuar? [S/N]: ")
    if opcao.strip().upper() == "N":
        break

aumento = []
demitido = []

for funcionario in funcionarios:
    if funcionario == funcionarios[0] or funcionario == funcionarios[2]:
        aumento.append(funcionario)
    else:
        demitido.append(funcionario)
print("Recebem aumento: ", aumento)
print("Serão demitidos: ", demitido)


