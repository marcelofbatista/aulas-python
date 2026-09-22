#CLASSE FILHA
# arquivo.py    classe
from Animal import Animal

class Gato(Animal):
    def __init__(self, idade, nome):
        super().__init__(idade = idade, tipo = "Gato") #super -> acessa casse pai
        self.nome = nome

    def cospePelo(self):
        print(f"O gato {self.nome} cospiu pelo...")
