"""
class ContaBancaria:
    def __init__(self, titular, saldo): # metodo construtor
        self.titular = titular # self.atributo = valor do parametro
        self.__saldo = saldo # atributo private


    #metodos Getters e Setters (Get = Pegar e Set = Inserir)
    def get_titular(self):
        senha = 1234
        senha_digitada = int(input('(GET)Digite sua senha: '))

        if senha == senha_digitada:
            return self.titular
        else:
            return 'Senha incorreta.'

    def set_titular(self, novo_titular):
        senha = 1234
        senha_digitada = int(input('(SET)Digite sua senha: '))

        if senha == senha_digitada:
            self.titular = novo_titular
            return 'Titular atualizado'
        else:
            return 'Senha incorreta.'

conta_banco = ContaBancaria("João", 10000)
print(conta_banco.get_titular()) # Acesso diretamente o atribut

conta_banco.titular = "Fulano" #modificando diretamente o atributo
print(conta_banco.get_titular())

conta_banco.set_titular('Ciclano') #modificando por metodo
print(conta_banco.get_titular())


class ContaBancariaCorreta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo #private

    @property #decorador ou anotation = anotação
    def saldo(self): # funciona como GET
        print("Acessando a info do saldo:")
        return self.__saldo

    @saldo.setter # criando um SET novo no metodo
    #acessa metodo
    def saldo(self, novo_saldo):
        self.__saldo = novo_saldo

usuario_banco_correto = ContaBancariaCorreta("José", 500)

print(usuario_banco_correto.saldo)

usuario_banco_correto.saldo = 1000
print(usuario_banco_correto.saldo)
print(usuario_banco_correto.__dict__)
"""

class ContaBancariaCorreta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo #private

    @property #decorador ou anotation = anotação
    def saldo(self): # funciona como GET
        print("Acessando a info do saldo:")
        return self.__saldo

    @saldo.setter # criando um SET novo no metodo
    #acessa metodo
    def saldo(self, novo_saldo):
        if novo_saldo < 0:
            print("Não é possível colocar saldo negativo")
        else:
            self.__saldo = novo_saldo

    def sacar(self, valor_saque):
        if valor_saque <= self.__saldo:
            self.__saldo -= valor_saque
            print(f"Quantidade retirada: {valor_saque}")
            print(f"Saldo: {self.__saldo}")
        else:
            print("Saldo insuficiente")



usuario_banco_correto = ContaBancariaCorreta("José", 500)

print(usuario_banco_correto.saldo)

usuario_banco_correto.saldo = 1000

print("Saldo: ", usuario_banco_correto.saldo)
usuario_banco_correto.sacar(100)
print(usuario_banco_correto.saldo)
print(usuario_banco_correto.__dict__)