"""
Questão 3: Somador de Números
Faça um programa que peça ao usuário para digitar números inteiros repetidamente. O programa deve continuar pedindo números até
que o usuário digite o número 0 (zero). Quando o usuário digitar 0, o laço deve ser encerrado e o programa deve exibir a
soma de todos os números que foram digitados até aquele momento.

"""
soma = 0
numero = int(input("Digite o número (0 para encerrar): "))
while numero != 0:
    soma += numero
    numero = int(input("Digite o número (0 para encerrar): "))
print(soma)