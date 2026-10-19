import requests, json

URL_BASE = 'http://192.168.205.100:8080/funcionarios'

# Ler o arquivo
with open("C:/Users/Noturno/PycharmProjects/aulas-python/aulas/requisicoes http/API/Base de dados Funcionarios/dados_funcionarios_atualizados.json", "r", encoding='utf-8') as arquivo:
    lista_funcionarios = json.load(arquivo)

# Montar o dicionário e PUT
for funcionario in lista_funcionarios:
    novo_dicionario = {
        "cargo": funcionario['cargo'],
        "cep": funcionario['cep'],
        "cidade": funcionario['cidade'],
        "estado": funcionario['estado'],
        "id": funcionario['id'],
        "nome": funcionario['nome'],
        "salario": funcionario['salario'],
        "tempoEmpresa": funcionario['tempoEmpresa'],
    }

    id_funcionario = funcionario['id']
    atualizacao = requests.put(f'{URL_BASE}/{id_funcionario}', json=novo_dicionario)

# Validação: 200
    if atualizacao.status_code == 200:
        print(f'Funcionário {id_funcionario} atualizado com sucesso (200)')
    else:
        print(f'ERRO ao atualizar funcionário {id_funcionario}: status {atualizacao.status_code}')

# Verificação GET
busca = requests.get(URL_BASE)
print('\n--- Funcionários na API ---')
for funcionario in busca.json():
    print(funcionario)