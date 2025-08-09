<h1>Aula 1 - Alura imersão de dados com python</h1>
<h2>Comandos utilizados</h2>

<h4> Importar uma biblioteca</h4>

```
import pandas as pd
```

<h4> Importar dados de um documento</h4>

```
df = pd.read_csv('LINK PARA O DOCUMENTO')
```

<h4> Mostrar as 5 primeiras linhas </h4>

```
df.head() --> todo método precisa ter ()
```

<h4> Mostrar informações gerais do dataframe</h4>

```
df.info()
```
<h4> Extrair descrição de dados númericos</h4>

```
df.describe()
```
<h4> Extrair dimensões do documento</h4>

```
df.shape
```
<h5>Exemplo de utilização</h5>

```
df linhas,colunas = df.shape[0], df.shape[1]
print(f"Quantidade de linhas: {linhas}")
print(f"Quantidade de colunas: {colunas}")
```
<h4> Extrair dados das colunas</h4>

```
df.columns()
```

<h4> Renomear colunas</h4>

```
name_dicionario = {
    'coluna_name_anterior' : 'coluna_name_novo',
    'coluna2_name_anterior' :'coluna2_name_novo'
}
```

<h5>Aplicando renomeação</h5>

```
df.rename(columns=name_dicionario, inplace = True)
df.head()
```
<h4>Mostrar dados de uma coluna</h4>

```
df['name_colunm'].value_counts()
```
<h4> Renomear categorias</h4>

```
name_dicionario = {
    'name_category'{
        'coluna_name_anterior' : 'coluna_name_novo',
        'coluna2_name_anterior' :'coluna2_name_novo'
    },
}
```

<h5>Aplicando renomeação</h5>

```

df['senioridade']=df['senioridade'].replace(renomear_categorias_senioridade['senioridade'])
df['senioridade'].value_counts()
```
<h4> Descrição geral das categorias </h4>

```
df.describe(include='object')
´´´
