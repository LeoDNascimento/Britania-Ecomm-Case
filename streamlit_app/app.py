import streamlit as st
import pandas as pd

st.set_page_config(page_title="Upload de Pedidos", layout="centered")

st.title("Upload de CSV – Pedidos")

file = st.file_uploader("Selecione o arquivo CSV", type=["csv"])

if file:
    df = pd.read_csv(
    file,
    sep=";",
    thousands=",",
    decimal="."
        )
    st.success("Arquivo carregado com sucesso!")
    st.dataframe(df)
