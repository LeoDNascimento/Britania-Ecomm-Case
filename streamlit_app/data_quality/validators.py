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
