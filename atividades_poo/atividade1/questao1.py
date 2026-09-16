"""
Crie uma classe que tenha no mínimo 5 atributos, 1 construtor,
3 métodos convencionais.
Sua classe deve ser uma das opções abaixo:
carro
banco
pessoa
Você escolhe quais atributos relacionar com o conceito da sua
classe.
No final, quero 5 objetos diferentes instanciados, e seu
programa deve exibir em uma lista fora da classe
todos os seus objetos.
"""

class Pessoa:
    def __init__(self, nome, idade, sexo, curso, turno):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.curso = curso
        self.turno = turno

    def __str__(self):
        return f"Nome: {self.nome}\nIdade: {self.idade}\nSexo: {self.sexo}\nCurso: {self.curso}\nTurno: {self.turno}\n"


pessoa1 = Pessoa("João", 18, "Masculino", "Python", "Noturno")
pessoa2 = Pessoa("Tião", 30, "Masculino", "Java", "Vespertino")
pessoa3 = Pessoa("Maria", 42, "Feminino", "C++", "Matutino")
pessoa4 = Pessoa("Carlos", 54, "Masculino", "Fortran", "Noturno")
pessoa5 = Pessoa("Clara", 16, "Feminino", "Redes Sociais", "Vespertino")


todasPessoas = [pessoa1, pessoa2, pessoa3, pessoa4, pessoa5]

for pessoa in todasPessoas:
    print(pessoa)