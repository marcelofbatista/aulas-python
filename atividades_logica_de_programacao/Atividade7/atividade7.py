
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


# funcionarios = []
#
# while True:
#     funcionarios.append(input("Digite o nome do funcionário: "))
#     opcao = input("Deseja continuar? [S/N]: ")
#     if opcao.strip().upper() != "S":
#         break
#
# aumento = []
# demitido = []
#
# for funcionario in funcionarios:
#     if funcionario == funcionarios[0] or funcionario == funcionarios[2]:
#         aumento.append(funcionario)
#     else:
#         demitido.append(funcionario)
# print("Recebem aumento: ", aumento)
# print("Serão demitidos: ", demitido)




funcionarios = []

while True:
    funcionarios.append(input("Digite o nome do funcionário: "))
    opcao = input("Deseja continuar? [S/N]: ")
    if opcao.strip().upper() != "S":
        print(f"Todos os funcionários: {funcionarios}")
        print("Quantidade de funcionários: ", len(funcionarios)) # len = tamanho
        break

aumento = [funcionarios[0]]
demitido = [funcionarios[1]]

repeticao = 0

while len(funcionarios) > repeticao:
    print(f"Funcionário {repeticao}: {funcionarios[repeticao]}")
    repeticao += 1

print("Lista de todos os funcionários: ")
for index in range(len(funcionarios)):
    print(f"Funcionário {index}: {funcionarios[index]}")

print("Lista dos funcionários demitidos: ")
for index in range(len(funcionarios)):
    repeticao += 2
    if repeticao < len(funcionarios):
        demitido.append(funcionarios[index])
print("Lista de demitidos: ", index)

    # print(f"Funcionário {index}: {funcionarios[index]}")




#item   função ou lista
# for index in demitido:
#     print(f"Lista demitido: {index}")
#
# for index in aumento:
#     print(f"Lista aumento: {index}")

