"""
Atividade 8
Crie uma única função que receba como parâmetro o nome de um aluno,
sua nota do primeiro, segundo, terceiro e quarto bimestre.
Sua função dev calcular a média final desse aluno, e imprimir na
tela todos os valores e informar se o aluno foi reprovado ou aprovado
pela média final.

OBS: valor da média = 7
"""

def aluno(nome, nota1, nota2, nota3, nota4):

    media = (nota1 + nota2 + nota3 + nota4) / 4
    if media >= 7:
        print("O aluno foi aprovado!")
    else:
        print("O aluno foi reprovado!")
    return

   nome = input("Digite o nome do aluno: ")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    nota4 = float(input("Digite a quarta nota: "))

aluno(nome, nota1, nota2, nota3, nota4)