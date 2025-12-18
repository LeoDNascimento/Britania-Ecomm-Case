CREATE OR REPLACE VIEW pedidos_silver AS
SELECT
    id_pedido,
    cliente,
    CAST(valor AS NUMERIC) AS valor,
    UPPER(status) AS status,
    created_at
FROM pedidos_raw;
