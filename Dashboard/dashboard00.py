import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from datetime import datetime, timedelta

# 🎨 CONFIGURAÇÃO DA PÁGINA
st.set_page_config(
    page_title="CSAT Analytics Dashboard", 
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="📊"
)

# 🎨 CSS CUSTOMIZADO PARA ESTILIZAÇÃO - TEMA AZUL E VERDE
st.markdown("""
<style>
    .st-ct {
        background-color: #2a5298; important!
    }  
    }
    .main-header {
        font-size: 3rem;
        font-weight: 700;
        background: linear-gradient(90deg, #1e3c72 0%, #2a5298 50%, #10a37f 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .metric-container {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        padding: 1rem;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(30,60,114,0.3);
        color: white;
        text-align: center;
        margin: 0.5rem 0;
        border: 1px solid rgba(255,255,255,0.1);
    }
    
    .metric-value {
        font-size: 2.5rem;
        font-weight: bold;
        margin: 0;
        text-shadow: 0 2px 4px rgba(0,0,0,0.3);
    }
    
    .metric-label {
        font-size: 1rem;
        opacity: 0.9;
        margin: 0;
    }
    
    .filter-container {
        background: linear-gradient(135deg, #1e3c72 0%, #2563eb 100%);
        padding: 1rem;
        border-radius: 15px;
        margin-bottom: 1rem;
        color: white;
        box-shadow: 0 4px 15px rgba(30,60,114,0.3);
    }
    
    .insights-box {
        background: linear-gradient(135deg, #0891b2 0%, #10a37f 100%);
        padding: 1.5rem;
        border-radius: 15px;
        color: white;
        margin: 1rem 0;
        box-shadow: 0 4px 15px rgba(8,145,178,0.3);
        border: 1px solid rgba(255,255,255,0.1);
    }
    
    .kpi-card {
        background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(30,60,114,0.1);
        border-left: 5px solid #1e3c72;
        border-top: 1px solid #10a37f;
        margin: 0.5rem 0;
        color: #1e3c72;
    }
    
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #1e3c72 0%, #10a37f 100%);
    }
    
    /* Customização adicional */
    .stSelectbox > div > div {
        background-color: rgba(255,255,255,0.95);
        border: 2px solid #10a37f;
    }
    
    .stSlider > div > div > div {
        color: #1e3c72;
    }
</style>
""", unsafe_allow_html=True)

# 📥 CARREGANDO E TRATANDO DADOS
@st.cache_data
def load_data():
    # Usando dados de exemplo já que não temos acesso ao arquivo
    data = {
        'ID': [5432, 5434, 5437, 5439, 5442, 5443, 5445, 5448, 5449, 5451, 5452, 5453, 5454, 5455, 5456, 5457, 5458, 5459, 5460, 5461, 5462, 5463, 5464, 5465, 5466, 5467, 5468, 5469, 5470, 5471, 5472, 5473, 5474, 5475, 5476, 5477, 5478, 5479, 5480],
        'TCSAT': [7, 10, 0, 10, 9, 9, 10, 9, 9, 7, 8, 6, 10, 7, 10, 8, 9, 5, 7, 10, 6, 8, 9, 7, 8, 9, 7, 10, 6, 9, 8, 7, 10, 5, 9, 8, 7, 10, 6],
        'DCSAT': [7, 8, 0, 10, 7, 7, 10, 7, 7, 7, 9, 6, 9, 8, 10, 7, 9, 5, 8, 9, 7, 8, 10, 6, 7, 9, 8, 10, 7, 8, 9, 7, 9, 6, 10, 8, 9, 7, 6],
        'TYPE': ['ACCOUNT', 'BET', 'OTHER', 'ACCOUNT', 'TECHNICAL ISSUES', 'TECHNICAL ISSUES', 'ACCOUNT', 'TECHNICAL ISSUES', 'TECHNICAL ISSUES', 'ACCOUNT', 'BET', 'OTHER', 'ACCOUNT', 'TECHNICAL ISSUES', 'BET', 'ACCOUNT', 'TECHNICAL ISSUES', 'OTHER', 'ACCOUNT', 'BET', 'TECHNICAL ISSUES', 'ACCOUNT', 'BET', 'OTHER', 'ACCOUNT', 'BET', 'TECHNICAL ISSUES', 'OTHER', 'ACCOUNT', 'BET', 'TECHNICAL ISSUES', 'ACCOUNT', 'OTHER', 'BET', 'TECHNICAL ISSUES', 'ACCOUNT', 'BET', 'OTHER', 'TECHNICAL ISSUES'],
        'DATA': ['18/07/2025', '18/07/2025', '18/07/2025', '18/07/2025', '18/07/2025', '18/07/2025', '18/07/2025', '18/07/2025', '18/07/2025', '18/07/2025', '18/07/2025', '18/07/2025', '18/07/2025', '18/07/2025', '19/07/2025', '19/07/2025', '19/07/2025', '19/07/2025', '19/07/2025', '19/07/2025', '19/07/2025', '19/07/2025', '19/07/2025', '19/07/2025', '20/07/2025', '20/07/2025', '20/07/2025', '20/07/2025', '20/07/2025', '20/07/2025', '20/07/2025', '20/07/2025', '20/07/2025', '20/07/2025', '20/07/2025', '20/07/2025', '20/07/2025', '20/07/2025', '20/07/2025'],
        'HORA': ['23:10:00', '20:00:00', '21:00:00', '21:50:00', '22:00:00', '23:00:00', '22:16:00', '22:20:00', '23:32:00', '23:50:00', '19:15:00', '18:30:00', '20:45:00', '17:00:00', '09:00:00', '10:30:00', '11:45:00', '13:00:00', '14:10:00', '15:20:00', '16:30:00', '17:40:00', '18:50:00', '19:05:00', '09:30:00', '10:00:00', '11:15:00', '12:00:00', '13:45:00', '14:55:00', '15:05:00', '16:15:00', '17:25:00', '18:35:00', '19:45:00', '20:55:00', '21:05:00', '22:15:00', '23:25:00']
    }
    
    df = pd.DataFrame(data)
    df['TCSAT'] = pd.to_numeric(df['TCSAT'], errors='coerce')
    df['DCSAT'] = pd.to_numeric(df['DCSAT'], errors='coerce')
    df['DATA'] = pd.to_datetime(df['DATA'], format='%d/%m/%Y')
    df['HORA'] = pd.to_datetime(df['HORA'], format='%H:%M:%S').dt.time
    return df

df = load_data()

# 🎯 CABEÇALHO PRINCIPAL
st.markdown('<h1 class="main-header">📊 CSAT Analytics Dashboard</h1>', unsafe_allow_html=True)

with st.sidebar:
    with st.expander("📅 Filtros Temporais", expanded=True):
        col_data1, col_data2 = st.columns(2)
        
        with col_data1:
            data_inicio = st.date_input(
                "📅 Data Início",
                value=df['DATA'].min(),
                min_value=df['DATA'].min(),
                max_value=df['DATA'].max(),
                help="Selecione a data inicial para análise"
            )
        
        with col_data2:
            data_fim = st.date_input(
                "📅 Data Fim",
                value=df['DATA'].max(),
                min_value=df['DATA'].min(),
                max_value=df['DATA'].max(),
                help="Selecione a data final para análise"
            )
        
        # Mostrar período selecionado
        if data_inicio and data_fim:
            dias = (data_fim - data_inicio).days + 1
            st.info(f"📊 Período: {dias} dia(s) selecionado(s)")
    
    with st.expander("🎯 Filtros por Categoria", expanded=True):
        tipos_selecionados = st.multiselect(
            "Tipos de Atendimento",
            options=df['TYPE'].unique(),
            default=df['TYPE'].unique(),
            help="Selecione os tipos de atendimento para análise"
        )
    
    with st.expander("⭐ Filtros por Nota", expanded=True):
        tcsat_range = st.slider(
            "Faixa de Notas TCSAT",
            min_value=0,
            max_value=10,
            value=(0, 10),
            help="Defina a faixa de notas TCSAT para análise"
        )
        
        dcsat_range = st.slider(
            "Faixa de Notas DCSAT",
            min_value=0,
            max_value=10,
            value=(0, 10),
            help="Defina a faixa de notas DCSAT para análise"
        )

# 🔍 APLICANDO FILTROS
if data_inicio and data_fim:
    df_filtrado = df[
        (df['DATA'] >= pd.to_datetime(data_inicio)) &
        (df['DATA'] <= pd.to_datetime(data_fim)) &
        (df['TYPE'].isin(tipos_selecionados)) &
        (df['TCSAT'] >= tcsat_range[0]) &
        (df['TCSAT'] <= tcsat_range[1]) &
        (df['DCSAT'] >= dcsat_range[0]) &
        (df['DCSAT'] <= dcsat_range[1])
    ]
else:
    df_filtrado = df[df['TYPE'].isin(tipos_selecionados)]

# 📊 MÉTRICAS PRINCIPAIS
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="metric-container">
        <p class="metric-value">{:.1f}</p>
        <p class="metric-label">📈 Média TCSAT</p>
    </div>
    """.format(df_filtrado['TCSAT'].mean()), unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-container">
        <p class="metric-value">{:.1f}</p>
        <p class="metric-label">📊 Média DCSAT</p>
    </div>
    """.format(df_filtrado['DCSAT'].mean()), unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-container">
        <p class="metric-value">{}</p>
        <p class="metric-label">🎯 Total Respostas</p>
    </div>
    """.format(len(df_filtrado)), unsafe_allow_html=True)

with col4:
    nps = ((df_filtrado['TCSAT'] >= 9).sum() / len(df_filtrado) * 100) if len(df_filtrado) > 0 else 0
    st.markdown("""
    <div class="metric-container">
        <p class="metric-value">{:.0f}%</p>
        <p class="metric-label">🌟 NPS Score</p>
    </div>
    """.format(nps), unsafe_allow_html=True)

# 🎯 CALCULADORA DE META INTERATIVA
st.markdown("---")
col_meta1, col_meta2 = st.columns([1, 2])

with col_meta1:
    st.markdown("""
    <div class="kpi-card">
        <h3>🎯 Calculadora de Meta</h3>
    </div>
    """, unsafe_allow_html=True)
    
    meta_desejada = st.number_input(
        "Meta TCSAT Desejada:",
        min_value=0.0,
        max_value=10.0,
        value=9.0,
        step=0.1
    )

with col_meta2:
    if len(df_filtrado) > 0:
        media_atual = df_filtrado['TCSAT'].mean()
        total_respostas = len(df_filtrado)
        soma_atual = df_filtrado['TCSAT'].sum()
        
        if media_atual < meta_desejada:
            notas_necessarias = (meta_desejada * total_respostas - soma_atual) / (10 - meta_desejada)
            notas_necessarias = max(0, int(notas_necessarias) + 1)
            
            st.markdown(f"""
            <div class="insights-box">
                <h3>🚀 Insights para Atingir a Meta</h3>
                <p><strong>Você precisa de {notas_necessarias} notas 10 consecutivas</strong></p>
                <p>📊 Média atual: {media_atual:.2f}</p>
                <p>🎯 Meta desejada: {meta_desejada:.2f}</p>
                <p>📈 Diferença: {meta_desejada - media_atual:.2f} pontos</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="insights-box">
                <h3>✅ Parabéns! Meta Atingida</h3>
                <p><strong>Sua média atual ({media_atual:.2f}) já superou a meta!</strong></p>
                <p>🏆 Você está {media_atual - meta_desejada:.2f} pontos acima da meta</p>
            </div>
            """, unsafe_allow_html=True)

# 📊 DASHBOARD DE GRÁFICOS
st.markdown("---")
st.markdown("## 📈 Análise Detalhada de Performance")

# PRIMEIRA LINHA DE GRÁFICOS
col_g1, col_g2 = st.columns(2)

with col_g1:
    # Gráfico de barras com gradiente
    media_por_tipo = df_filtrado.groupby('TYPE')[['TCSAT', 'DCSAT']].mean().reset_index()
    
    fig1 = go.Figure()
    fig1.add_trace(go.Bar(
        name='TCSAT',
        x=media_por_tipo['TYPE'],
        y=media_por_tipo['TCSAT'],
        marker_color='rgba(30, 60, 114, 0.8)',
        hovertemplate='<b>%{x}</b><br>TCSAT: %{y:.2f}<extra></extra>'
    ))
    fig1.add_trace(go.Bar(
        name='DCSAT',
        x=media_por_tipo['TYPE'],
        y=media_por_tipo['DCSAT'],
        marker_color='rgba(16, 163, 127, 0.8)',
        hovertemplate='<b>%{x}</b><br>DCSAT: %{y:.2f}<extra></extra>'
    ))
    
    fig1.update_layout(
        title="📊 Comparativo de Médias por Tipo de Atendimento",
        xaxis_title="Tipo de Atendimento",
        yaxis_title="Nota Média",
        barmode='group',
        template='plotly_white',
        hovermode='x unified',
        title_x=0.5,
        showlegend=True,
        height=400
    )
    st.plotly_chart(fig1, use_container_width=True)

with col_g2:
    # Gráfico de pizza moderno
    distribuicao_tipos = df_filtrado['TYPE'].value_counts().reset_index()
    distribuicao_tipos.columns = ['TYPE', 'Quantidade']
    
    fig2 = px.pie(
        distribuicao_tipos,
        names='TYPE',
        values='Quantidade',
        hole=0.5,
        color_discrete_sequence=['#1e3c72', '#2a5298', '#10a37f', '#0891b2', '#065f46', '#1e40af'],
        title="🎯 Distribuição por Tipo de Atendimento"
    )
    fig2.update_traces(
        textposition='inside',
        textinfo='percent+label',
        hovertemplate='<b>%{label}</b><br>Quantidade: %{value}<br>Porcentagem: %{percent}<extra></extra>'
    )
    fig2.update_layout(
        title_x=0.5,
        height=400,
        showlegend=True,
        legend=dict(orientation="v", yanchor="middle", y=0.5)
    )
    st.plotly_chart(fig2, use_container_width=True)

# SEGUNDA LINHA DE GRÁFICOS
col_g3, col_g4 = st.columns(2)

with col_g3:
    # Histograma de distribuição de notas
    fig3 = go.Figure()
    fig3.add_trace(go.Histogram(
        x=df_filtrado['TCSAT'],
        name='TCSAT',
        opacity=0.7,
        marker_color='rgba(30, 60, 114, 0.8)',
        nbinsx=11
    ))
    fig3.add_trace(go.Histogram(
        x=df_filtrado['DCSAT'],
        name='DCSAT',
        opacity=0.7,
        marker_color='rgba(16, 163, 127, 0.8)',
        nbinsx=11
    ))
    
    fig3.update_layout(
        title="📊 Distribuição das Notas",
        xaxis_title="Notas",
        yaxis_title="Frequência",
        barmode='overlay',
        template='plotly_white',
        title_x=0.5,
        height=400
    )
    st.plotly_chart(fig3, use_container_width=True)

with col_g4:
    # Evolução temporal
    evolucao = df_filtrado.groupby('DATA')[['TCSAT', 'DCSAT']].mean().reset_index()
    
    fig4 = go.Figure()
    fig4.add_trace(go.Scatter(
        x=evolucao['DATA'],
        y=evolucao['TCSAT'],
        mode='lines+markers',
        name='TCSAT',
        line=dict(color='rgba(30, 60, 114, 1)', width=3),
        marker=dict(size=8, color='rgba(30, 60, 114, 1)')
    ))
    fig4.add_trace(go.Scatter(
        x=evolucao['DATA'],
        y=evolucao['DCSAT'],
        mode='lines+markers',
        name='DCSAT',
        line=dict(color='rgba(16, 163, 127, 1)', width=3),
        marker=dict(size=8, color='rgba(16, 163, 127, 1)')
    ))
    
    fig4.update_layout(
        title="📈 Evolução Temporal das Médias",
        xaxis_title="Data",
        yaxis_title="Média",
        template='plotly_white',
        title_x=0.5,
        height=400,
        hovermode='x unified'
    )
    st.plotly_chart(fig4, use_container_width=True)

# GRÁFICO DE CORRELAÇÃO E INSIGHTS
st.markdown("---")
col_g5, col_insights = st.columns([2, 1])

with col_g5:
    # Scatter plot de correlação
    fig5 = px.scatter(
        df_filtrado,
        x='TCSAT',
        y='DCSAT',
        color='TYPE',
        size=[1]*len(df_filtrado),
        hover_data=['ID', 'DATA'],
        title="🔍 Correlação entre TCSAT e DCSAT",
        color_discrete_sequence=['#1e3c72', '#2a5298', '#10a37f', '#0891b2', '#065f46', '#1e40af']
    )
    fig5.update_layout(
        template='plotly_white',
        title_x=0.5,
        height=400
    )
    st.plotly_chart(fig5, use_container_width=True)

with col_insights:
    # Box com insights automáticos
    if len(df_filtrado) > 0:
        correlacao = df_filtrado[['TCSAT', 'DCSAT']].corr().iloc[0,1]
        melhor_tipo = df_filtrado.groupby('TYPE')['TCSAT'].mean().idxmax()
        pior_tipo = df_filtrado.groupby('TYPE')['TCSAT'].mean().idxmin()
        
        st.markdown(f"""
        <div class="insights-box">
            <h3>🧠 Insights Automáticos</h3>
            <p><strong>🔗 Correlação TCSAT/DCSAT:</strong> {correlacao:.2f}</p>
            <p><strong>🏆 Melhor Performance:</strong> {melhor_tipo}</p>
            <p><strong>⚠️ Precisa Atenção:</strong> {pior_tipo}</p>
            <p><strong>📊 Amostras Analisadas:</strong> {len(df_filtrado)}</p>
        </div>
        """, unsafe_allow_html=True)

