import pandas as pd

#verificar versão
#print(pd.__version__)
"""
#SÉRIES - conjunto de listas de uma dimensão (lista, dicionário, tupla)
nomes = ["João","Felipe","André"]
indexes=["a", "b", "c"]
nomes_series = pd.Series(nomes, index=indexes)

print(nomes_series["a"])

coluna_idade = pd.Series([25,30,35,40,45])
print(coluna_idade[coluna_idade == 25])
"""
#DATAFRAMES
#converte dicionário em dataframe
notas = {
    "nome": ["italo","bruno"],
    "turma": ["Python", "Ruby"],
    "notas": [10,8]
}

indexes = ["a", "b"]
df = pd.DataFrame(notas,index=indexes)
print("===PRIMEIRA LISTA===")
print(df)
print(df.loc["a"])
#adiciona nomes para index
print("\n")
print("===LISTA ATUALIZADA===")
df["Status"] = ["Aprovado", "Reprovado"]
print(df)

nova_linha = pd.DataFrame([{
    "nome": "Victor",
    "turma": "Python",
    "notas": 7,
    "Status": "Aprovado"
}], index=["c"])

#faz a concatenação de valores
df = pd.concat([df, nova_linha])

print("\n")
print("===LISTA ATUALIZADA LINHA NOVA===")

print(df)
"""
print("\n")
print("===LISTA PYTHON===")
df_filtrado = df[df["turma"] == "Python" or df["turma"] == "Ruby"]

print(df_filtrado)
print("\n")
"""
print("\n")
df_filtrado = df[df["turma"].isin(["Python","Ruby"])]

print(df_filtrado)
print("\n")