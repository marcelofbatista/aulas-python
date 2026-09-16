#POO -> Programação Orientada a Objetos

#toda classe precisa da palavra reservada class
"""
class Aluno: #toda classe começa com letra maiúscula
    pass #significa placeholder: eu vou escrever alguma coisa futuramente

"""

class Aluno:
  #  nome_aluno = "João" # atributo -> faz referência a uma variável da classe

 #   objeto_aluno = Aluno()

       def __init__(self, nome, registro, notas): #metodo Construtor
        #define a cosntrução de um novo objeto
        #não se cria um objeto sem construtor
        #nome = novo atributo da classe = parâmetro
        self.nome = nome # nome = Aluno.nome_aluno
        self.registro = registro
        self.notas = notas
        #todos os alunos, OBRIGATORIAMENTE, precisam de nome e registro

        def mostrarNome(self): # metodo
        #todos os metodos dentro de uma classe precisam de self (algo dentro da classe)
            print(self.nome) #uso self para pegar valor dentro da classe

        #metodo de formatação
        def __str__(self):
            return print(self.nome, self.registro, self.notas)

aluno1 = Aluno("José", 11111, [10,10,10,10]) # instância da variável nome
#aluno = objeto
aluno2 = Aluno("fulano", 22222,[5,7,3,9]) #outra instância
aluno3 = aluno1 #criando um novo objeto, mas não cria instância nova

#not compara valores None ou que representam vazio
string = ""
numero_inteiro = 0
numero_quebrado = 0.0
lista = []
tupla = ()
boolean = False

if not aluno1.nome: #executa apenas quando encontra o valor vazio
    print("Aluno não tem valor registrado como nome")

print(aluno1.nome)
print(aluno1.registro)
print(aluno1.notas)

todosOsAlunos = [aluno1, aluno2, aluno3]

for aluno in todosOsAlunos:
    print(aluno)