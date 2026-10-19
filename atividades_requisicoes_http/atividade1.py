import requests, json

ARQUIVO = "historico_pesquisa.json"


def carregar_historico():
    """Lê o histórico do arquivo. Se não existir (ou estiver vazio/corrompido), começa uma lista nova."""
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        print("Arquivo de histórico ainda não existe. Ele será criado.")
        return []
    except json.JSONDecodeError:
        print("Arquivo de histórico vazio ou inválido. Começando uma lista nova.")
        return []


def salvar_historico(historico):
    """Grava a lista inteira de volta no arquivo."""
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(historico, arquivo, ensure_ascii=False, indent=4)


def consultar_cep(cep):
    """Consulta a ViaCEP. Retorna o dicionário do endereço ou None se der erro."""
    try:
        resposta = requests.get(f"https://viacep.com.br/ws/{cep}/json/", timeout=10)
    except requests.exceptions.ConnectionError:
        print("Erro: falha de conexão. Verifique sua internet.")
        return None
    except requests.exceptions.Timeout:
        print("Erro: a API demorou demais para responder.")
        return None

    if resposta.status_code != 200:
        print(f"Erro: a API respondeu com status {resposta.status_code}.")
        return None

    dados = resposta.json()

    # A ViaCEP devolve status 200 com {"erro": true} quando o CEP não existe
    if "erro" in dados:
        print("Erro: CEP inexistente.")
        return None

    return dados


# ----- Programa principal -----
historico = carregar_historico()

while True:
    cep = input("\nDigite o CEP (só números) ou ENTER para sair: ").strip().replace("-", "")

    if cep == "":
        break

    if len(cep) != 8 or not cep.isdigit():
        print("Erro: o CEP precisa ter exatamente 8 números.")
        continue

    endereco = consultar_cep(cep)

    if endereco is not None:
        print(f"Logradouro: {endereco['logradouro']}")
        print(f"Bairro:     {endereco['bairro']}")
        print(f"Cidade:     {endereco['localidade']}")
        print(f"Estado:     {endereco['uf']}")

        registro = {
            "cep": endereco["cep"],
            "logradouro": endereco["logradouro"],
            "bairro": endereco["bairro"],
            "cidade": endereco["localidade"],
            "estado": endereco["uf"],
        }
        historico.append(registro)
        salvar_historico(historico)
        print(f"Pesquisa salva. Total no histórico: {len(historico)}")

print("Programa encerrado.")