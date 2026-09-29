carrinho = []
total = 0

usuario = input("Digite seu nome para iniciar a compra: ")

while True:
    produto = input("Digite 'fim' para finalizar."
                 "\nDigite o nome do produto: ")
    if produto == "fim":
        break
    preco = float(input("Digite o valor desse produto:"))
    total += preco

    # adicionando uma LISTA dentro de uma LISTA
    carrinho.append([produto, preco])

with open("pagamento.txt", 'w', encoding='utf-8') as arquivo:
    arquivo.write("RECIBO DO CARRINHO\n\n")

    arquivo.write(str(carrinho[0]))

    for produto in carrinho:
        nome_produto = produto[0]
        preco_produto = produto[1]

        arquivo.write(f"Produto: {nome_produto} R${preco_produto:.2f}\n")

    arquivo.write(f"\nTotal a pagar: {total:.2f}\n")