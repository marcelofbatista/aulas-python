"""
Questão 2: A Fábrica de Caixas (Operador de Módulo)
Uma fábrica empacota maçãs em caixas que cabem exatamente 12 unidades. Crie um programa que pergunte ao usuário a quantidade total de maçãs colhidas no dia. Utilizando o operador de módulo (%), calcule e exiba na tela quantas maçãs sobrarão fora das caixas (ou seja, o resto da divisão por 12).

"""
macas_colhidas = int(input("Quantas maças você colheu hoje? "))
sobra = macas_colhidas % 12
print("Ficaram",sobra, "maças fora das caixas.")