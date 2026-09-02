"""
Questão 4: O Boletim Escolar Automático (Aritmética + Lógica AND)
Construa um sistema escolar que leia a Nota 1 e a Nota 2 de um aluno, além da sua Porcentagem de Frequência.
O programa deve primeiro calcular a média das notas.
Para o aluno ser aprovado, ele precisa de duas coisas ao mesmo tempo: uma média maior ou igual a 6.0 E uma frequência maior ou igual a 75.
Exiba a média calculada e, em seguida, exiba True se ele foi aprovado ou False se reprovou, usando o operador and.

"""
nota1 = float(input("Insira sua nota 1: "))
nota2 = float(input("Insira sua nota 2: "))
frequencia = float(input("Insira sua frequencia: "))
media = (nota1 + nota2) / 2
condicao = media >= 6 and frequencia >= 75
print("Sua média foi:", media, "Foi aprovado?", condicao)