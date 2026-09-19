class Loja: # classe pai
    def __init__(self, nome_loja):
        self.__nome_loja = nome_loja

    @property
    def nome_loja(self):
        return self.__nome_loja
    @nome_loja.setter
    def nome_loja(self, nome_loja):
        self.__nome_loja = nome_loja

#HERANÇA

class Produto(Loja): #classe filha
    def __init__(self, nome, preco, quantidade_estoque):
        super().__init__(nome_loja="Atacadão")
        self.__nome = nome
        self.__preco = preco
        self.__quantidade_estoque = quantidade_estoque

class Comprador:
    def __init__(self, nome, produto_comprado):
        self.__nome = nome
        self.__produto_comprado = produto_comprado

compra = Produto
print(compra.__dict__)