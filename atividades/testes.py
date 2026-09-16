# compra = 250.50
# desconto = round((compra *0.15),2)
# valorFinal = round((compra - desconto),2)
# print("Valor da compra",compra)
# print("Valor do desconto",desconto)
# print("Valor final com desconto",valorFinal)


contador = 1
soma = 0
while contador <= 5:
    if contador == 4:
        break
    soma = soma + contador
    contador = contador + 1
print(soma)