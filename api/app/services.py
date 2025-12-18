from app.database import get_connection

def insert_pedido(pedido):
    conn = get_connection()
    cur = conn.cursor()

    query = """
        INSERT INTO pedidos_raw (id_pedido, cliente, valor, status)
        VALUES (%s, %s, %s, %s)
    """

    cur.execute(
        query,
        (
            pedido.id_pedido,
            pedido.cliente,
            pedido.valor,
            pedido.status
        )
    )

    conn.commit()
    cur.close()
    conn.close()
