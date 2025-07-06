import pandas as pd
import matplotlib.pyplot as plt
import os
import matplotlib.ticker as mticker # Formata o eixo

# --- 1. Lê os dados ---
try:
    caminho_arquivo = 'data/Vendas.xlsx'
    df = pd.read_excel(caminho_arquivo)
    print(f"Dados carregados com sucesso de '{caminho_arquivo}'.")
except FileNotFoundError:
    print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado. Verifique o caminho e o nome do arquivo.")
    exit()

# --- 2. Processa os dados ---
# Agrupa por loja e soma as quantidades, depois ordena
vendas_loja = df.groupby('ID Loja')['Quantidade'].sum().sort_values(ascending=False)

# --- 3. Melhora a estética do gráfico com um estilo do Matplotlib ---
plt.style.use('seaborn-v0_8-whitegrid') 

# Tamanho da figura
plt.figure(figsize=(14, 8)) 

# Gráfico de barras
barras = vendas_loja.plot(kind='bar', color='#1f77b4', edgecolor='black', alpha=0.8) 

# --- 4. Títulos, rótulos e formatação ---
plt.title('Quantidade Total Vendida por Loja', fontsize=20, fontweight='bold', pad=20) 
plt.suptitle('Análise de Desempenho de Vendas por Filial', fontsize=12, color='gray') 
plt.xlabel('ID da Loja', fontsize=14, labelpad=15)
plt.ylabel('Quantidade Vendida', fontsize=14, labelpad=15)
plt.xticks(rotation=45, ha='right', fontsize=10) # Rotaciona os rótulos e ajusta o alinhamento
plt.yticks(fontsize=12)

# Adiciona rótulos de dados em cima de cada barra
for i, valor in enumerate(vendas_loja.values):
    plt.text(i, valor + 50, f'{valor:,.0f}', ha='center', va='bottom', fontsize=10, color='black', fontweight='bold')

# Formata o eixo Y para não ter notação científica
formatter = mticker.StrMethodFormatter('{x:,.0f}')
plt.gca().yaxis.set_major_formatter(formatter)
plt.ylim(0, vendas_loja.max() * 1.1) # Ajusta o limite do eixo Y para dar espaço aos rótulos

# Remove a grade horizontal e vertical
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.grid(axis='x', which='both', visible=False) 

# Remove as molduras superior e direita 
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

# Exibe o gráfico
plt.tight_layout() 

# --- 5. Salva a imagem do gráfico na pasta ---
pasta_destino = 'graficos_vendas'
nome_arquivo = 'vendas_por_loja.png'

if not os.path.exists(pasta_destino):
    os.makedirs(pasta_destino)
    print(f"Pasta '{pasta_destino}' criada com sucesso.")

caminho_completo = os.path.join(pasta_destino, nome_arquivo)
plt.savefig(caminho_completo, bbox_inches='tight', dpi=300)

print(f"Gráfico melhorado salvo com sucesso em: {caminho_completo}")

plt.show()