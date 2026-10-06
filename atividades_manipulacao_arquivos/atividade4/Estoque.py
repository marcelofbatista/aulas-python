import json

ARQUIVO = "estoque.json"

# ============================================================
# PARTE 1 — Criando e salvando os dados
# ============================================================

loja = {
    "nome": "TechStore",
    "produtos": [
        {"nome": "Teclado", "preco": 150.00, "quantidade": 20},
        {"nome": "Mouse", "preco": 80.00, "quantidade": 35},
        {"nome": "Monitor", "preco": 1200.00, "quantidade": 8},
    ],
}

with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
    json.dump(loja, arquivo, indent=4, ensure_ascii=False)

print(f"Estoque inicial salvo em {ARQUIVO}.\n")

# ============================================================
# PARTE 2 — Lendo e atualizando os dados
# ============================================================

# 1. Leitura do arquivo
with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
    dados_lidos = json.load(arquivo)

# 2. Percorrendo e exibindo nome e preço
print(f"Produtos da {dados_lidos['nome']}:")
for produto in dados_lidos["produtos"]:
    print(f"O produto {produto['nome']} custa R$ {produto['preco']:.2f}")

# 3. Adicionando um novo produto
novo_produto = {"nome": "Fone de Ouvido", "preco": 250.00, "quantidade": 15}
dados_lidos["produtos"].append(novo_produto)

# ============================================================
# DESAFIO EXTRA — 10% de desconto em um produto
# ============================================================

produto_em_promocao = "Monitor"
for produto in dados_lidos["produtos"]:
    if produto["nome"] == produto_em_promocao:
        preco_antigo = produto["preco"]
        produto["preco"] = round(preco_antigo * 0.9, 2)
        print(f"\nDesconto aplicado: {produto['nome']} "
              f"de R$ {preco_antigo:.2f} para R$ {produto['preco']:.2f}")

# 4. Salvando o dicionário atualizado (sobrescreve o arquivo)
with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
    json.dump(dados_lidos, arquivo, indent=4, ensure_ascii=False)

print(f"\nEstoque atualizado salvo em {ARQUIVO}.")