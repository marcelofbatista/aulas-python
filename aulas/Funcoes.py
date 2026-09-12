#CONHECENDO
# #retorna um valor -> precisa desse valorFUNÇÕES
# função vazia (void) -> não retorna nada, mas executa algo
def soma():
    print("Fazendo a soma")
    numero1 = int(input("Insira um numero 1: "))
    numero2 = int(input("Insira um numero 2: "))
    return print(numero1 + numero2)

def subtracao():
    print("Fazendo a subtração")
    numero1 = int(input("Insira um numero 1: "))
    numero2 = int(input("Insira um numero 2: "))
    return print(numero1 - numero2)

def multiplicacao():
    print("Fazendo a multiplicação")
    numero1 = int(input("Insira um numero 1: "))
    numero2 = int(input("Insira um numero 2: "))
    return print(numero1 * numero2)

def divisao():
    print("Fazendo a divisão")
    numero1 = int(input("Insira um numero 1: "))
    numero2 = int(input("Insira um numero 2: "))
    return print(numero1 / numero2)

def potencia():
    print("Fazendo a potência")
    numero1 = int(input("Insira um numero 1: "))
    numero2 = int(input("Insira um numero 2: "))
    return print(numero1 ** numero2)

def olaUsuario(nome):
    print(f"Olá {nome}")