from abc import ABC, abstractmethod

class Veiculo(ABC):
    @abstractmethod
    def acelerar(self):
        pass

class Carro(Veiculo):
    def acelerar(self):
        print("Carro acelerar")

class Moto(Veiculo):
    def acelerar(self):
        print("Moto acelerar")


moto = Moto()
carro = Carro()

lista_veiculos = [moto, carro]

for veiculo in lista_veiculos:
    veiculo.acelerar()