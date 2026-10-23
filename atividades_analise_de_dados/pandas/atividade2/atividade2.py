import pandas as pd

base_de_dados = "../atividade1/funcionarios.csv"
df = pd.read_csv(base_de_dados, sep=";")

print(df.columns.tolist())

salarios_altos = df[
    (df["salario"] > 6000)
]

print(salarios_altos)

salarios_altos = pd.DataFrame(salarios_altos)

salarios_altos.to_csv("cargos_altos.csv", index=False, sep=";")

print(salarios_altos)

