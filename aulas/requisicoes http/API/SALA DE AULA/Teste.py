import requests

link = 'http://192.168.205.100:8080/usuarios'
resposta = requests.get(link)
print(f'STATUS BUSCA DADOS:{resposta}')

#chave aceitas na API da aula: 'nome', 'email'
meus_dados = {
    'nome': 'Marcelo',
    'email': 'marcelo@senai.com.br'
}

envio = requests.post(link, json=meus_dados)
print(f'STATUS BUSCA DADOS:{envio}')

#REQUISIÇÃO DE PUT
meus_atualizado = {
    'nome': 'Marcelo Ferreira Batista',
    'email': 'marcelo@senai.com.br'
}

atualizacao = requests.put((link+'/2'), json=meus_atualizado)

#REQUISIÇÃO DELETE

deletar = requests.delete(link+'/3')
print(f'STATUS DELETE {deletar.text}')

# ====================================================
# Fazendo buscas e salvado na minha base de dados

busca_cep = requests.get(link_cep)
busca_pessoa = requests.get(link+'/1')

lista_de_pessoas = []

lista_de_pessoas.append(busca_pessoa.json())
lista_de_pessoas.append(busca_cep.json())

print(lista_de_pessoas)

print(f'\n\nNome da pessoa: {lista_de_pessoas[0]['nome']}\n'
      f'CEP da pessoa: {lista_de_pessoas[1]['cep']}\n')

with open('pessoas.json', 'w', encoding='utf-8') as arquivo:
    json.dump(lista_de_pessoas, arquivo, indent=4, ensure_ascii=False)