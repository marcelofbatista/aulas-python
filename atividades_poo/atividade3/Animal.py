class Animal:
    def __init__(self, nome, idade, nivel_fome):
        self.__nome = nome
        self.__idade = 0
        self.idade = idade
        self.nivel_fome = nivel_fome

    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade

    @property
    def nivel_fome(self):
        return self.__nivel_fome

    @idade.setter
    def idade(self, idade):
        if idade < 0:
            print("Erro: Idade inválida")
        else:
            self.__idade = idade

    @nivel_fome.setter
    def nivel_fome(self, nivel_fome):
        if nivel_fome < 0:
            nivel_fome = 0
        elif nivel_fome > 100:
            nivel_fome = 100
        self.__nivel_fome = nivel_fome

    def alimentar(self,porcao):
        if porcao <= 0:
            print("Erro: Porção inválida")
        else:
            self.nivel_fome = self.nivel_fome - porcao


    def emitir_som(self):
        print(f"{self.nome} faz um som genérico.")

    def exibir_resumo(self):
        print(f"Nome: {self.nome} | Idade: {self.idade} | Fome: {self.nivel_fome}")