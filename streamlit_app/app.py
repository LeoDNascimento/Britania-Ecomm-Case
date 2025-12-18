import streamlit as st
import pandas as pd

from data_quality.validators import (
    validate_schema,
    validate_types,
    validate_status_domain,
)
from data_quality.schema import EXPECTED_COLUMNS
from data_quality.transforms import apply_transforms

can_send = False
df_transformed = None

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
        status_errors = validate_status_domain(df)

        if type_errors:
            st.error("Erros de tipo de dados encontrados:")
            for err in type_errors:
                st.write(f"❌ {err}")
            st.stop()

        st.success("Tipos de dados validados com sucesso!")


        if schema_errors:
            st.error("Erro de schema detectado:")
            for err in schema_errors:
                st.write(f"- {err}")
            st.stop()

        st.success("Schema validado com sucesso!")

        if status_errors:
            st.error("Erro de domínio do status:")
            for e in status_errors:
                st.write(f"❌ {e}")
            st.stop()

        st.success("Dados validados e transformados com sucesso!")
        
        df_transformed = apply_transforms(df)
        can_send = True
        st.dataframe(df_transformed)

        if can_send and df_transformed is not None:
            if st.button("Enviar pedidos"):
                st.info("Envio iniciado...")
                st.success("Envio concluído (simulação) ✅")

    except Exception as e:
        st.error("Erro ao processar o arquivo CSV")
        st.exception(e)
