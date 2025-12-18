def validate_types(df, expected_columns):
    errors = []

    for idx, row in df.iterrows():
        line_number = idx

        for column, expected_type in expected_columns.items():
            value = row.get(column)

            try:
                if expected_type == "int":
                    int(str(value).replace(",", ""))

                elif expected_type == "float":
                    float(str(value).replace(",", ""))

                elif expected_type == "str":
                    str(value)

            except Exception:
                errors.append(
                    f"Linha {line_number}: valor inválido na coluna '{column}'"
                )

    return errors


def validate_schema(df, expected_columns):
    errors = []

    # Colunas ausentes
    missing = set(expected_columns.keys()) - set(df.columns)
    if missing:
        errors.append(f"Colunas ausentes: {', '.join(missing)}")

    # Colunas extras
    extra = set(df.columns) - set(expected_columns.keys())
    if extra:
        errors.append(f"Colunas extras: {', '.join(extra)}")

    return errors
