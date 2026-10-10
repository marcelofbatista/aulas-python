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

deletar = requests.delete(link+'/2')
print(f'STATUS DELETE {deletar.text}')

while True:
    novo_dado = {
        'nome': 'Teste',
        'email': email@email.com
    }
    