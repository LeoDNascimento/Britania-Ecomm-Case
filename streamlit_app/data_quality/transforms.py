def apply_transforms(df):
    df = df.copy()

    # Padronizar status
    status_map = {
        "PENDENTE": "PENDENTE",
        "PENDING": "PENDENTE",
        "APROVADO": "APROVADO",
        "APPROVED": "APROVADO",
        "CANCELADO": "CANCELADO",
        "CANCELED": "CANCELADO",
        "CANCELLED": "CANCELADO",
        "HANDLING": "PROCESSANDO",
        "PAYMENT-APPROVED": "PAGAMENTO-APROVADO"
    }

    df["status"] = (
        df["status"]
        .astype(str)
        .str.strip()
        .str.upper()
        .map(status_map)
    )

    # Converter tipos numéricos
    df["id_pedido"] = df["id_pedido"].astype(int)

    df["valor"] = (
        df["valor"]
        .astype(str)
        .str.replace(",", "", regex=False)
        .astype(float)
    )

    # Limpar strings
    df["cliente"] = df["cliente"].astype(str).str.strip()

    return df
