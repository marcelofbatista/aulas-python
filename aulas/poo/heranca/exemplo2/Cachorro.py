#CLASSE FILHA
from Animal import Animal

class Cachorro(Animal):
    def __init__(self, idade, nome):
        super().__init__(tipo = "Cachorro", idade = idade)
        self.nome = nome

    def latir(self):
        print(f"O {self.__tipo} está latindo.")

    def aniversario(self):
