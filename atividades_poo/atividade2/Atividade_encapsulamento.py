class Produto:
    def __init__(self, nome, preco, quantidade_estoque):
        self.__nome = nome
        self.__preco = preco
        self.__quantidade_estoque = quantidade_estoque

    @property
    def nome(self):
        return self.__nome

    @property
    def preco(self):
        return self.__preco

    @property
    def quantidade_estoque(self):
        return self.__quantidade_estoque

    @quantidade_estoque.setter
    def quantidade_estoque(self, nova_quantidade_estoque):
        if nova_quantidade_estoque <= 0:
            print("Erro: Quantidade inválida")
        else:
            self.__quantidade_estoque = nova_quantidade_estoque

    def realizar_venda(self, quantidade_venda):
        if quantidade_venda <= 0 or quantidade_venda > self.__quantidade_estoque:
            print("Venda negada: Estoque insuficiente")
        else:
            self.__quantidade_estoque = (self.__quantidade_estoque - quantidade_venda)

    def aplicar_desconto(self, desconto):
        if desconto <= 0 or desconto > 0.8:
            print("Erro: Desconto inválido")
        else:
            self.__preco = (self.__preco - (self.__preco*desconto))

    def exibir_resumo(self, resumo):
        return f"Nome: {self.__nome}\nPreço: {self.__preco}\nQuantidade de estoque: {self.__quantidade_estoque}"


meu_produto = Produto("Alicate", 15, 100)
meu_produto.realizar_venda(50)
print(meu_produto.exibir_resumo(meu_produto))


print(meu_produto.__dict__)