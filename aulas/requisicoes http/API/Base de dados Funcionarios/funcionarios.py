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
                dicionario_funcionario = resposta.json()

                if dicionario_funcionario.get("erro") == "true" or dicionario_funcionario.get("erro") is True:
                    print("CEP inválido ou não encontrado! Tente novamente.\n")
                    continue

                print(f"Dados encontrados: {dicionario_funcionario}\n")

                for chave, valor in dicionario_funcionario.items():
                    if chave == "localidade":
                        funcionario["cidade"] = valor
                    if chave == "uf":
                        funcionario["estado"] = valor
                funcionario["cep"] = cep_digitado
                print(f"CEP de {funcionario['nome']} atualizado com sucesso!\n")
                break
            else:
                print("Erro na consulta do CEP")

#base de dados atualizada
print("---BASE DE DADOS ATUALIZADA---")
for funcionario in lista_funcionarios:
    print(funcionario)

#salvar os dados preenchidos em um arquivo json
with open("dados_funcionarios_atualizados.json", "w", encoding="utf-8") as arquivo:
    json.dump(lista_funcionarios, arquivo, ensure_ascii=False, indent=4)


#inserir dados onde estiver algum dado vazio
#no cep, apenas aceitar ceps válidos
#salvar os dados preenchidos em um arquivo json
# (ex.: dados_funcionarios_atualizados.json

