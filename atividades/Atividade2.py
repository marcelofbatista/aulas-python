"""
ATIVIDADE 2
Crie um algoritmo, que faça um formulário em que o usuário digite seu nome, sua idade e se ele tem plano de saúde (True ou False)
O sistema deve retornar em um único print(), todas as informações, e se  ele for menor de idade ou idoso ou se não tiver plano de saúde, que ele não será aceito no nosso formulário;
idade < 18 or idade >65 or possue_plano = False
Exemplo de retorno: Seu nome é João, você tem 22 anos, Tem plano? False. Você foi aceito? False
"""
#RESPOSTA
nome = input("Insira seu nome: ")
idade = int(input("Insira sua idade: "))
possue_plano = str(input("Tem plano de saúde? "))
print("Seu nome é",nome,"você tem", idade,"anos. Tem plano?",possue_plano,"Você foi aceito?", (idade < 18 or idade > 65 or possue_plano == False))