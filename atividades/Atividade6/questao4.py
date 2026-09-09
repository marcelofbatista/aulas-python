"""
Questão 4: Menu Interativo
Crie um programa que mostre repetidamente um menu com duas opções:
1 - Mostrar saudação
2 - Sair do programa
O programa deve pedir para o usuário escolher uma opção. Usando while:
Se ele digitar 1, exiba "Olá, seja muito bem-vindo(a)!".
Se ele digitar qualquer número diferente de 1 e 2, exiba "Opção inválida!".
O programa só deve parar de repetir e encerrar quando o usuário digitar 2, exibindo a mensagem "Programa encerrado."

"""
print("Escolha uma opção: \n1 - Mostrar saudação \n2 - Sair do programa")
opcao = input("Insira apenas o número (1 ou 2): ")
while opcao != "1" and opcao != "2":
    print("Opção inválida!")
    opcao = input("Insira novamente o número (1 ou 2): ")
    if opcao == "1":
        print("Olá, seja muito bem-vindo(a)!")

    elif opcao == "2":
        print("Programa encerrado.")

