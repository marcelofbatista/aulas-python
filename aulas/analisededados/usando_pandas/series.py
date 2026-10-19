import pandas as pd

#verificar versão
#print(pd.__version__)

#SÉRIES - conjunto de listas de uma dimensão (lista, dicionário, tupla)
nomes = ["João","Felipe","André"]
indexes=["a", "b", "c"]
nomes_series = pd.Series(nomes, index=indexes)

print(nomes_series["a"])

coluna_idade = pd.Series([25,30,35,40,45])
print(coluna_idade[coluna_idade == 25])

#DATAFRAMES