import pandas as pd

df_dados_incompletos = pd.DataFrame([
    {
        "nome": "João Menezes",
        "cpf": "123.456.789-10"
    },
{
        "nome": "Jose Batista",
        "cpf": "72345678920"
    },
{
        "nome": "Marcelo Batista",
        "cpf": "333 333 444-56"
    }
]
)
print(df_dados_incompletos)

df_dados_incompletos.to_csv("cargos_dados_incompletos.csv", index=False, sep=";")

dados = pd.read_csv("cargos_dados_incompletos.csv", sep=";", dtype={"cpf": "string"})

dados["cpf_formatado"] = dados["cpf"].str.replace(r"\D", "", regex=True)

"""
dados["salario_formatado"] = (dados["salario"]
                              .str.replace(r"[^\d",.\-, "", regex=True).str.replace(".","-", regex=True))
"""
print(dados)
