<center>

# Aula 1 - Alura imersão de dados com python</h1>

</center>

<h4> Importar uma biblioteca</h4>

```python
import pandas as pd
```

<h4> Importar dados de um documento</h4>

```python
df = pd.read_csv('LINK PARA O DOCUMENTO')
```

<h4> Mostrar as 5 primeiras linhas </h4>

```python
df.head() #todo método precisa ter ()
```

<h4> Mostrar informações gerais do dataframe</h4>

```python
df.info()
```
<h4> Extrair descrição de dados númericos</h4>

```python
df.describe()
```
<h4> Extrair dimensões do documento</h4>

```python
df.shape
```
<h5>Exemplo de utilização</h5>

```python
df linhas,colunas = df.shape[0], df.shape[1]
print(f"Quantidade de linhas: {linhas}")
print(f"Quantidade de colunas: {colunas}")
```
<h4> Extrair dados das colunas</h4>

```python
df.columns()
```

<h4> Renomear colunas</h4>

```python
name_dicionario = {
    'coluna_name_anterior' : 'coluna_name_novo',
    'coluna2_name_anterior' :'coluna2_name_novo'
}
```

<h5>Aplicando renomeação</h5>

```python
df.rename(columns=name_dicionario, inplace = True)
df.head()
```
<h4>Mostrar dados de uma coluna</h4>

```python
df['name_colunm'].value_counts()
```
<h4> Renomear categorias</h4>

```python
name_dicionario = {
    'name_category'{
        'coluna_name_anterior' : 'coluna_name_novo',
        'coluna2_name_anterior' :'coluna2_name_novo'
    },
}
```

<h5>Aplicando renomeação</h5>

```python

df['senioridade']=df['senioridade'].replace(renomear_categorias_senioridade['senioridade'])
df['senioridade'].value_counts()
```
<h4> Descrição geral das categorias </h4>

```python
df.describe(include='object')

```
<center>

# Aula 2- Limpeza de dados e preparação

</center>

<h4> Verificar as tabelas se são nulas</h4>

```python
df.isnull()

#exemplo de como utilizar

df.isnull().sum() # soma todas as linhas null por categoria

#pegar valores existentes

df.['tabela'].unique()

#pegar apenas as tabelas com os valores null

df.[df.isnull().any(axis=1)]

```

<center>
<h4> Criar um dataframe</h4>
<h5>Prenencher os valores com a média e com a mediana</h5>
<h3>método fillna()</h3>


```python
import numpy as pd # importar numpy, que manipula dados
df_salarios = pd.DataFrame[{
    'nome':['Ranilton','André','Ramon','Agenor'],
    'salario':[4000,np.nan,5000,np.nan] #np.nun deixa o valor como nulo
# calcula a média salarial e substitui os nulos pela média e arredonda valores
df_salarios['salario_media'] = df_salarios['salario'].fillna(df_salarios['salario'].mean().round(2))
# Calcula a mediana e substitui os nulos pela mediana
df_salarios['salario_mediana'] = df_salarios['salario'].fillna(df_salarios['salario'].median())
}]

```
<center><h4>Exemplo 2</h4><h5>usando a substituição pelo valor anterior <h3>método ffill()</h3></h5></center>

```python
df_temperaturas = pd.DataFrame({
    'Dia': ['segunda','Terça','Quarta','Quinta','Sexta','Sabádo','Domingo'],
    'Temperatura': [30,30,np.nan,np.nan,28,np.nan,27]
})
df_temperaturas['Preenchido_ffill'] = df_temperaturas['Temperatura'].ffill()
df_temperaturas

```

<center><h4>Exemplo 2</h4><h5>usando a substituição pelo próximo valor <h3>método bfill()</h3></h5></center>

```python
df_temperaturas = pd.DataFrame({
    'Dia': ['segunda','Terça','Quarta','Quinta','Sexta','Sabádo','Domingo'],
    'Temperatura': [30,30,np.nan,np.nan,28,np.nan,27]
})
df_temperaturas['Preenchido_bfill'] = df_temperaturas['Temperatura']bffill()
df_temperaturas

```