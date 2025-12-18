import streamlit as st
import pandas as pd

from data_quality.schema import EXPECTED_COLUMNS
from data_quality.validators import validate_schema, validate_types

st.title("Upload de CSV - Pedidos")

file = st.file_uploader("Selecione o arquivo CSV", type=["csv"])

if file:
    try:
        df = pd.read_csv(
            file,
            sep=";",
            thousands=",",
            decimal="."
        )

        st.success("Arquivo carregado com sucesso!")
        st.dataframe(df)

        schema_errors = validate_schema(df, EXPECTED_COLUMNS)
        type_errors = validate_types(df, EXPECTED_COLUMNS)

        if type_errors:
            st.error("Erros de tipo de dados encontrados:")
            for err in type_errors:
                st.write(f"❌ {err}")
            st.stop()

        st.success("Tipos de dados validados com sucesso ✅")


        st.success("Tipos de dados validados com sucesso ✅")


        if schema_errors:
            st.error("Erro de schema detectado:")
            for err in schema_errors:
                st.write(f"- {err}")
            st.stop()

        st.success("Schema validado com sucesso ✅")

    except Exception as e:
        st.error("Erro ao processar o arquivo CSV")
        st.exception(e)
