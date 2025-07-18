import streamlit as st
import pandas as pd
import plotly.express as px
import os # Importe o módulo os

st.set_page_config(layout="wide")
page_title = "Dashborad"

df = pd.read_csv("/home/ranilton/Área de Trabalho/Data_Analisys/data/SATS_PESQ.csv")
df['TC_SAT']= pd.to_numeric

st.title("Tabela de Dados SATS_PESQ")
st.dataframe(df)
st.write(f"Dados carregados com sucesso! Número de linhas: {len(df)}")

col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)

#Mediatcsat 


#Mediatdsat 

#media csat por type

#quantidade de notas

#media dia