import streamlit as st
import pandas as pd
import psycopg2
import os

st.set_page_config(
    page_title="Dataviz - Pedidos por Status",
    layout="wide"
)

# Conexão com o banco
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://admin:admin@postgres:5432/orders"
)

@st.cache_data
def load_gold_data():
    conn = psycopg2.connect(DATABASE_URL)
    query = """
        SELECT
            status,
            total_pedidos,
            valor_total
        FROM pedidos_por_status
        ORDER BY total_pedidos DESC;
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return df


st.title("Pedidos por Status – Camada Gold")

st.markdown(
    """
    Esta visualização consome diretamente a **camada Gold** do Data Lake.
    Os dados são atualizados automaticamente sempre que novos pedidos são inseridos.
    Caso não tenha dados após o envio, limpe o Cache da página utilizando a tecla "C"
    """
)

df = load_gold_data()

if df.empty:
    st.warning("Nenhum dado disponível no momento.")
    st.stop()


col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Tabela Analítica")
    st.dataframe(df, use_container_width=True)

with col2:
    st.subheader("Total de Pedidos por Status")
    st.bar_chart(df.set_index("status")["total_pedidos"])


st.subheader("Exportar Relatório")

csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Baixar CSV",
    data=csv,
    file_name="pedidos_por_status.csv",
    mime="text/csv"
)
