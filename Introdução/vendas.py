import pandas as pd
import numpy as np 

# --- 1. CONFIGURAÇÃO E CARREGAMENTO DE DADOS ---
try:
    caminho_arquivo = "data/Vendas.xlsx"
    vendas_df = pd.read_excel(caminho_arquivo)
    print(f"Dados carregados com sucesso de '{caminho_arquivo}'.")
except FileNotFoundError:
    print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado. Verifique o caminho e o nome do arquivo.")
    exit()

# Opcional: Visualizar as primeiras linhas para um 'sanity check'
print("\n--- Primeiras 5 linhas do DataFrame ---")
print(vendas_df.head())
print("\n--- Informações do DataFrame ---")
print(vendas_df.info())


# --- 2. MANIPULAÇÃO E LIMPEZA DE DADOS (em cadeia) ---
vendas_df['Comissão'] = vendas_df['Valor Final'] * 0.05

# Limpeza de dados: Tratar valores vazios de forma mais robusta e eficiente.


# Deletar linhas e colunas COMPLETAMENTE vazias (todos os valores são NaN)
vendas_df = vendas_df.dropna(how='all')
vendas_df = vendas_df.dropna(how='all', axis=1)

# Preencher os valores vazios (NaN) na coluna 'Comissão' com a média.
vendas_df['Comissão'] = pd.to_numeric(vendas_df['Comissão'], errors='coerce')
media_comissao = vendas_df['Comissão'].mean()
vendas_df['Comissão'] = vendas_df['Comissão'].fillna(media_comissao)

# Outras formas de preencher valores vazios.
# vendas_df = vendas_df.ffill()

# --- 3. EXEMPLOS DE SELEÇÃO E FILTRAGEM DE DADOS ---
# Separar a lógica de seleção da lógica de processamento principal.

print("\n--- Selecionando e Filtrando Dados ---")

# Selecionar linhas e colunas para a loja 'Norte Shopping' de forma eficiente.
df_norte_shopping = vendas_df.loc[vendas_df['ID Loja'] == 'Norte Shopping', ['ID Loja', 'Produto', 'Quantidade']]
print("\nDataFrame com vendas do 'Norte Shopping':")
print(df_norte_shopping.head()) 
print(f"\nTotal de linhas filtradas para 'Norte Shopping': {len(df_norte_shopping)}")

# Acessar um valor específico de forma direta
print(f"\nProduto na linha de índice 1: {vendas_df.loc[1, 'Produto']}")


# --- 4. CÁLCULO DE INDICADORES E AGRUPAMENTOS ---

print("\n--- Indicadores e Análises Agregadas ---")

# Contagem de transações por loja (Value Counts)
transacoes_por_loja = vendas_df['ID Loja'].value_counts()
print("\nNúmero de transações por loja:")
print(transacoes_por_loja)

# Faturamento total por produto (usando .groupby().sum())
faturamento_por_produto = vendas_df.groupby('Produto')['Valor Final'].sum().sort_values(ascending=False)
print("\nFaturamento total por produto (ordenado):")
print(faturamento_por_produto.head(10)) # Mostrar apenas os 10 primeiros para não poluir a saída

# Faturamento total por loja (mais um exemplo)
faturamento_por_loja = vendas_df.groupby('ID Loja')['Valor Final'].sum().sort_values(ascending=False)
print("\nFaturamento total por loja (ordenado):")
print(faturamento_por_loja)

# Exemplo de agregação múltipla (agregando soma e média)
agg_loja = vendas_df.groupby('ID Loja').agg(
    Faturamento_Total=('Valor Final', 'sum'),
    Quantidade_Total=('Quantidade', 'sum'),
    Ticket_Medio=('Valor Final', 'mean')
).sort_values(by='Faturamento_Total', ascending=False)
print("\nAnálise de desempenho por loja:")
print(agg_loja)


# --- 5. ENCERRAMENTO E RECOMENDAÇÕES ---

# salvar o DataFrame limpo em um novo arquivo:
vendas_df.to_excel("data/Vendas_limpo.xlsx", index=False) # 'index=False' evita salvar a coluna de índice
print("\nDataFrame limpo salvo como 'Vendas_limpo.xlsx'.")
