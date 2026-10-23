import pandas as pd

df = pd.read_csv('funcionarios.csv')

#todos os salários menores do que 3000, maiores do que 5000 mil e iguais a 3100
filtro_salario = df[(df['salario'] < 3000) | (df['salario'] > 5000) | (df['salario'] == 3100)]
print("=== Salários < 3000, > 5000 ou = 3100 ===")
print(filtro_salario)

#todos os cargos de Analista de Dados, Analista de Sistemas, Desenvolvedor Java e Cientista de dados

cargos = ['Analista de Dados', 'Analista de Sistemas', 'Desenvolvedor Java','Cientista de Dados']

#cargos_minusculos = [c.lower() for c in cargos]
#filtro_cargo = df[df['cargo'].str.strip().str.lower().isin(cargos_minusculos)]
print("\n=== Cargos selecionados ===")
print(cargos)

#listar os nomes e cargos de quem tem um salário maior do que 6000
filtro_6000 = df.loc[df['salario'] > 6000, ['nome', 'cargo']]
print("\n=== Salário > 6000 (nome e cargo) ===")
print(filtro_6000)

#listar todos os funcionarios com id par
filtro_par = df[df['id'] % 2 == 0]
print("\n=== Funcionários com id par ===")
print(filtro_par)





