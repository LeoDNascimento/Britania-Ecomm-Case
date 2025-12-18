CREATE TABLE IF NOT EXISTS pedidos_raw (
    id SERIAL PRIMARY KEY,
    id_pedido INT,
    cliente TEXT,
    valor NUMERIC,
    status TEXT,
    contagemCliente TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);