from Animal import Animal


class Mamifero(Animal):
    def __init__(self, nome, idade, nivel_fome, velocidade_kmh):
        super().__init__(nome, idade, nivel_fome)
        self.__velocidade_kmh = velocidade_kmh


    @property
    def velocidade_kmh(self):
        return self.__velocidade_kmh
    @velocidade_kmh.setter
    def velocidade_kmh(self, velocidade_kmh):
        self.__velocidade_kmh = velocidade_kmh
