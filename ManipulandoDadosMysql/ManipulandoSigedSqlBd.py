import streamlit as st
import mysql.connector
import pandas as pd
from mysql.connector import Error
import os
from dotenv import load_dotenv



load_dotenv()

# --- CONFIGURAÇÃO DA CONEXÃO COM O BANCO DE DADOS ---
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
# --- FUNÇÕES OTIMIZADAS PARA ACESSO AOS DADOS ---

# O cache de recursos evita recriar a conexão com o banco a cada interação do usuário.
@st.cache_resource
def get_connection():
    """Cria e retorna uma conexão com o banco de dados."""
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        if conn.is_connected():
            return conn
    except Error as e:
        st.error(f"Erro ao conectar ao MySQL: {e}")
        return None

# O cache de dados evita re-executar a mesma query no banco se os filtros não mudarem.
@st.cache_data
def fetch_data(query):
    """Executa uma query e retorna os dados como um DataFrame do Pandas."""
    conn = get_connection()
    if conn:
        try:
            df = pd.read_sql(query, conn)
            return df
        except Error as e:
            st.error(f"Erro ao executar a consulta: {e}")
            return pd.DataFrame()
    return pd.DataFrame()


# --- CONSTRUÇÃO DO DASHBOARD INTERATIVO ---

st.set_page_config(page_title="Dashboard de Chamados", layout="wide")
st.title("📊 Dashboard de Análise de Chamados")

# A query principal é executada apenas uma vez (ou quando o cache expira).
query_chamados = "SELECT * FROM App_chamado"
df_chamados = fetch_data(query_chamados)

if not df_chamados.empty:
    # --- FILTRO NA BARRA LATERAL ---
    st.sidebar.header("Filtros")
    setores = df_chamados['setor'].unique()
    setor_selecionado = st.sidebar.selectbox("Filtrar por Setor:", ['Todos'] + list(setores))

    # Aplica o filtro selecionado ao DataFrame principal.
    if setor_selecionado == 'Todos':
        df_filtrado = df_chamados
    else:
        df_filtrado = df_chamados[df_chamados['setor'] == setor_selecionado]

    # --- TODO O DASHBOARD ABAIXO É RENDERIZADO USANDO OS DADOS JÁ FILTRADOS ---

    st.subheader(f"Visão Geral para: {setor_selecionado}")

    total_chamados = len(df_filtrado)
    chamados_abertos = len(df_filtrado[df_filtrado['status'] == 'aberto'])
    chamados_resolvidos = len(df_filtrado[df_filtrado['status'] == 'resolvido'])

    col1, col2, col3 = st.columns(3)
    col1.metric("Total de Chamados", total_chamados)
    col2.metric("Chamados Abertos", chamados_abertos)
    col3.metric("Chamados Resolvidos", chamados_resolvidos)

    st.divider()

    col_graf1, col_graf2 = st.columns(2)

    with col_graf1:
        st.subheader("Chamados por Status")
        status_counts = df_filtrado['status'].value_counts()
        st.bar_chart(status_counts)

    with col_graf2:
        st.subheader("Chamados por Urgência")
        urgencia_counts = df_filtrado['urgencia'].value_counts()
        st.bar_chart(urgencia_counts)

    st.divider()

    st.subheader("Detalhes dos Chamados")
    st.dataframe(df_filtrado)

else:
    st.warning("Não foi possível carregar os dados dos chamados.")