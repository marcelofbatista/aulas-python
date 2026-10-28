import pandas as pd

#1. A Base de Dados (CSV)
df_mercado = pd.read_csv('estoque_supermercado.csv')

#2. Limpeza da Coluna preco:
df_preco_limpo = (df_mercado["preco"]
                              .str.replace(r"[^\d,.\-]", "", regex=True)
                              .str.replace(r"\.(?=\d{3}(?:\.|,|$))", "", regex=True)
                              .str.replace(r",",".", regex=False))
df_preco_limpo = pd.to_numeric(df_preco_limpo, errors="coerce")

print(df_preco_limpo)
######Preencha os valores nulos (NaN) com a média de preços da base.
df_preco_limpo.info()


#3. Limpeza da Coluna quantidade:

print("\n--- BASE DE DADOS LIMPA ---")
# print(df.head())

#4. Padronização da Coluna setor:



#5. Tratamento de Datas:


#6. Análise de Dados e Filtragem:

print("\n--- PRODUTOS VENCENDO ESTA SEMANA ---")
# (Seu filtro de alerta de vencimento)

print("\n--- MAIOR QUANTIDADE A VENCER ---")
# (Seu lógica de qualidade de estoque)

print("\n--- MAIOR VALOR PATRIMONIAL POR SETOR ---")
# (Sua lógica de agrupamento e soma do valor total de estoque)


#Testes Obrigatórios na Atividade: