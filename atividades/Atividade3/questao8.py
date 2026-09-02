"""
Questão 8: A Calculadora de Lucro da Empresa
Construa um programa para um comerciante. O sistema deve receber três dados: o nome do produto, o custo de fábrica para comprá-lo e o
preço pelo qual ele será vendido na loja.
Calcule o lucro em reais (Preço de Venda - Custo).
Verifique se o lucro é maior que 20 reais.
Exiba uma mensagem final mostrando: o nome do produto, o lucro obtido e o resultado da verificação (se o lucro foi bom = True ou False).

"""

produto = (input("Digite o nome do produto: "))
custo = float(input("Digite o custo do produto: "))
preco = float(input("Digite o preço de venda do produto: "))
lucro = preco - custo
condicao = lucro > 20
print("O nome do produto é:", produto,"O lucro obtido foi: ", lucro, "O lucro foi bom?", condicao)