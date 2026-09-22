#CLASSE PAI

class Animal:
    def __init__(self, tipo, idade, regiao):
        self.__tipo = tipo
        self.__idade = idade
        self.__regiao = regiao

    @property
    def idade(self):
        return self.__idade

    def comer(self):
        print(f"O animal {self.__tipo} está comendo")

    def dormir(self):
        print(f"O animal {self.__tipo} está dormindo")

    def mostrarIdade(self):
        print(f"O animal {self.__tipo} tem {self.__idade} anos de idade.")