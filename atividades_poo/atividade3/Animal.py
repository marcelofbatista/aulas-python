class Animal:
    def __init__(self, nome, idade, nivel_fome):
        self.__nome = nome
        self.__idade = idade
        self.__nivel_fome = nivel_fome

    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade

    @property
    def nivel_fome(self):
        return self.__nivel_fome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @idade.setter
    def idade(self, idade):
        if idade < 0:
            print("Erro: Idade inválida")
        else:
            self.__idade = idade

    @nivel_fome.setter
    def nivel_fome(self, nivel_fome):
        if nivel_fome < 0 or nivel_fome > 100:
            print("Erro: Nível de fome deve estar entre 0 e 100")
        else:
            self.__nivel_fome = nivel_fome

    def alimentar(self,porcao):
        if porcao < 0:
            print("Erro: Porção inválida")
        else:
            self.__nivel_fome = porcao
