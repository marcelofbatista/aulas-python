#OPERADORES LÓGICOS
"""
    ATRIBUIÇÃO
    = -> variavel = 10
    ! = NÃO, NOT, CONTRÁRIO
    SIM -> !SIM = NÃO

    COMPARAÇÃO
    esperar uma resposta de True ou False
    != -> se for diferente retorna True, se for igual retorna False
    == -> se for diferente retorna False, se for igual retorna True
    >= -> se for diferente retorna False ou True
    > ->
    < ->
    >= -> se for maior E igual retorna True, contrario retorna False
    <= ->se for menor E igual retorna True, contrario retorna False

    PARA MAIS COMPARAÇÕES
    and -> se toas as comparações forem True, retora True
    or -> se ao menos uma das comparações forem True, retorna True
    not

ATIVIDADE 2
Crie um algoritmo, que faça um formulário em que o usuário digite seu nome, sua idade e se ele tem plano de saúde (True ou False)
O eu sistema deve retornar em um único print(), todas as informações, e se  ele for menor de idade ou idoso ou se não tiver plano de saúde, que ele não será aceito no nosso formulário;
Exemplo de retorno: Seu nome é João, você tem 22 anos, Tem plano? False. Você foi aceito? False
"""

#TESTES
idade = 70 # INTEIRO
pais_acompanham = False
print("Nossa balada, não aceita criança, nem idoso nem pais dos convidados")
print("Você pode entrar em uma balada?")
print(idade>=18 and idade < 65 and pais_acompanham != True)



