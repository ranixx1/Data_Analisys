import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

df = pd.read_csv("../data/supermarket_sales.csv", sep=";", decimal=",")

df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values(["Date"])
df["Month"] = df["Date"].apply(lambda x: str(x.year) + "-" + str(x.month))
month = st.sidebar.selectbox("Mês", df["Month"].unique())

df_filtered = df[df["Month"] == month]

st.markdown("<h1 style='text-align: center;'>Dashboard de Vendas</h1>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)

# Gráfico 1 - Faturamento por dia
fig_date = px.bar(df_filtered, x="Date", y="Total", color="City", title="Faturamento por dia")
fig_date.update_layout(title_x=0.35)
col1.plotly_chart(fig_date, use_container_width=True)

# Gráfico 2 - Faturamento por tipo de produto
df_grouped = df_filtered.groupby(["Product line", "City"])["Total"].sum().reset_index()
fig_prod = px.bar(df_grouped, x="Total", y="Product line", color="City", orientation="h", title="Faturamento por tipo de produto")
fig_prod.update_layout(title_x=0.4)
col2.plotly_chart(fig_prod, use_container_width=True)

# Gráfico 3 - Faturamento por filial
city_total = df_filtered.groupby("City")[["Total"]].sum().reset_index()
fig_city = px.bar(city_total, x="City", y="Total", title="Faturamento por filial")
fig_city.update_layout(title_x=0.4)
col3.plotly_chart(fig_city, use_container_width=True)

# Gráfico 4 - Faturamento por tipo de pagamento
fig_kind = px.pie(df_filtered, values="Total", names="Payment", title="Faturamento por tipo de pagamento")
fig_kind.update_layout(title_x=0.15)
col4.plotly_chart(fig_kind, use_container_width=True)

# Gráfico 5 - Avaliação por cidade
rating_avg = df_filtered.groupby("City")[["Rating"]].mean().reset_index()
fig_rating = px.bar(rating_avg, x="City", y="Rating", title="Avaliação")
fig_rating.update_layout(title_x=0.5)
col5.plotly_chart(fig_rating, use_container_width=True)
