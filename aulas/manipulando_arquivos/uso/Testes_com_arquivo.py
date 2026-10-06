lista_nomes = []

while True:
    novo_nome = input("Digite o nome: ('fim' finaliza código)\n")

    if novo_nome == 'fim':
        break

    lista_nomes.append(novo_nome)

for nome in lista_nomes:
    print(nome)




with open("lista_de_nomes.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(str(lista_nomes))

with open("lista_de_nomes.txt", "r", encoding="utf-8") as arquivo:
    texto = arquivo.read()
    print(texto)

with open("lista_de_nomes.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write("Orlando")

with open("lista_de_nomes.txt", "r", encoding="utf-8") as arquivo:
    texto = arquivo.read()

    print(texto)