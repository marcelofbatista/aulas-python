from Animal import Animal

from Gato import Gato
from Cachorro import Cachorro

class Main:
    print("INICIANDO CLASSE PRINCIPAL")

    gato1 = Gato(2, Tom)
    gato1.mostrarIdade()

    animal = Animal("Gato", 10)

    cachorro1 = Cachorro(3, "Zeus")
    cachorro1.comer()
