import requests
import json

link_funcionarios = "http://192.168.205.100:8080/funcionarios"

resposta = requests.get(link_funcionarios)

print(resposta.json())

lista_funcionarios = (resposta.json())

print("---LISTA DE FUNCIONÁRIOS SEM ENDEREÇO CADASTRADO---\n")
for funcionario in lista_funcionarios:
    if funcionario['cep'] == None:
        print(f"O funcionário {funcionario['nome']} não tem cep cadastrado\n")

        while True:
            cep_digitado = input("Digite o seu CEP: ")
            link_cep = f"https://viacep.com.br/ws/{cep_digitado}/json/"
            resposta = requests.get(link_cep)

            print(resposta.status_code)

            if resposta.status_code == 200:
                print(resposta.json(value))
                dicionario_funcionario = resposta.json()
                for chave, valor in dicionario_funcionario.items():
                    if chave == "localidade":
                        funcionario["cidade"] = valor
                    if chave == "estado":
                        funcionario["estado"] = valor
                funcionario["cep"] = cep_digitado
                break

#base de dados atualizada

for funcionario in lista_funcionarios:
    print(funcionario)



#inserir dados onde estiver algum dado vazio
#no cep, apenas aceitar ceps válidos
#salvar os dados preenchidos em um arquivo json
# (ex.: dados_funcionarios_atualizados.json


"""
    print(f"Nome: {funcionario['nome']}\n"
          f"Cargo: {funcionario['cargo']}\n"
          f"CEP: {funcionario['cep']}\n"
          f"Cidade: {funcionario['cidade']}\n"
          f"Estado: {funcionario['estado']}\n")
"""