import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard CSAT", layout="wide")

# 📥 Carregando dados
df = pd.read_csv("/home/ranilton/Área de Trabalho/Data_Analisys/data/SATS_PESQ.csv")

# 🧹 Tratamento de dados
df['TCSAT'] = pd.to_numeric(df['TCSAT'], errors='coerce')
df['DCSAT'] = pd.to_numeric(df['DCSAT'], errors='coerce')
df['DATA'] = pd.to_datetime(df['DATA'], format='%d/%m/%Y')

# 🎛️ NOVOS FILTROS com botão de aplicar
st.sidebar.header("🔍 Filtros de Análise")

with st.sidebar.form("filtros_form"):
    tipos = st.multiselect("Tipo de Atendimento", df['TYPE'].unique(), default=list(df['TYPE'].unique()))
    data_ini, data_fim = st.date_input("Período", [df['DATA'].min(), df['DATA'].max()])
    nota_min, nota_max = st.slider("Faixa de Notas TCSAT", 0, 10, (0, 10))
    aplicar = st.form_submit_button("Aplicar Filtros")

nota_minima = st.sidebar.slider("Nota mínima TCSAT", min_value=0, max_value=10, value=0)

# Filtros aplicados
df_filtrado = df.copy()
if aplicar:
    df_filtrado = df[
        (df['TYPE'].isin(tipos)) &
        (df['DATA'] >= pd.to_datetime(data_ini)) &
        (df['DATA'] <= pd.to_datetime(data_fim)) &
        (df['TCSAT'] >= nota_min) &
        (df['TCSAT'] <= nota_max)
    ]

st.title("📊 Dashboard de Satisfação (CSAT)")

# 📌 Métricas principais
col1, col2 = st.columns(2)
with col1:
    st.metric("📈 Média TC_SAT", f"{df_filtrado['TCSAT'].mean():.2f}")
with col2:
    st.metric("📉 Média DC_SAT", f"{df_filtrado['DCSAT'].mean():.2f}")

st.markdown("---")

# 🎯 META DE SATISFAÇÃO
st.subheader("🎯 Meta de Satisfação (TCSAT)")
meta = st.number_input("Digite sua meta de média TCSAT:", min_value=0.0, max_value=10.0, step=0.1, value=9.0)

total_respostas = len(df_filtrado)
soma_atual = df_filtrado['TCSAT'].sum()
media_atual = df_filtrado['TCSAT'].mean()

# Calcular quantas notas 10 são necessárias
if media_atual < meta:
    notas_necessarias = (meta * total_respostas - soma_atual) / (10 - meta)
    notas_necessarias = int(notas_necessarias) + 1
    st.info(f"🚀 Você precisa de **{notas_necessarias} notas 10** para atingir a média {meta:.2f}")
else:
    st.success("✅ Sua média atual já está acima da meta! Parabéns!")

st.markdown("---")

# 📈 Gráficos
col3, col4 = st.columns(2)

with col3:
    st.subheader("📊 Média de CSAT por Tipo")
    media_csat_tipo = df_filtrado.groupby('TYPE')['TCSAT'].mean().reset_index()
    fig1 = px.bar(
        media_csat_tipo,
        x='TYPE',
        y='TCSAT',
        color='TYPE',
        color_discrete_sequence=px.colors.qualitative.Bold,
        labels={'TCSAT': 'Média TCSAT', 'TYPE': 'Tipo'},
    )
    fig1.update_layout(title_x=0.3)
    st.plotly_chart(fig1, use_container_width=True)

with col4:
    st.subheader("📊 Quantidade de Notas por Tipo")
    count_tipo = df_filtrado['TYPE'].value_counts().reset_index()
    count_tipo.columns = ['TYPE', 'Quantidade']
    fig2 = px.pie(
        count_tipo,
        names='TYPE',
        values='Quantidade',
        hole=0.4,
        color_discrete_sequence=px.colors.qualitative.Vivid
    )
    fig2.update_traces(textinfo='percent+label')
    st.plotly_chart(fig2, use_container_width=True)

st.markdown("---")

