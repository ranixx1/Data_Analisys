import pandas as pd

# DataFrame de exemplo
dados = {
    'Id': ["1", "2","3"],
    "Nome": ["Ranilton", "Lucas", "Leonardo"],
    "Idade": [19, 25, 22],
    "Salario": [3000, 6000, 4500]
}
df = pd.DataFrame(dados)

# Series de exemplo
s = pd.Series([10, 20, 30])

# Imprimindo DataFrame

# Lendo arquivos
# di = pd.read_csv('planilha.csv')
# di_df = pd.read_excel('planilha.xlsx', sheet_name='nome')

# Manipulação básica
print(df.head())      # 5 primeiras linhas
print(df.tail())      # 5 últimas linhas

# Colunas específicas
print(df[['Nome', 'Idade']])
print(df['Idade'])

# Filtros booleanos
print(df['Idade'] > 30)                    # Série booleana
print(df[df['Idade'] > 30])               # Filtrando por idade
print(df[df['Salario'] > 5000])           # Filtrando por salário

# Filtros combinados
filtro_maior_que30 = df['Idade'] > 30
filtro_mais_de_5mil = df['Salario'] > 5000
print(df[filtro_maior_que30 & filtro_mais_de_5mil])

# Criando nova coluna
df['Salario Anual'] = df['Salario'] * 12

# Removendo colunas
df = df.drop('Salario Anual', axis=1)

# Resumos
df.info()
print(df.describe())
print("Soma dos salários:", df['Salario'].sum())
print("Média salarial:", df['Salario'].mean())

# Limpeza de dados
df = df.dropna()

