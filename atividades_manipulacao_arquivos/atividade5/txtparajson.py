import json

with open("banco_livros.txt", "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()
    catalogo_livros = []
    for linha in linhas:
        linha = linha.strip().split(";")
        catalogo_livros.append(linha)
    print(f"Id: {linha[0]}\n"
          f"Nome: {linha[1]}\n"
          f"Descrição: {linha[2]}\n"
          f"Preço: {linha[3]}\n"
          f"Em estoque: {linha[4]}\n")