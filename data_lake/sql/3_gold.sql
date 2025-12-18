CREATE OR REPLACE VIEW pedidos_por_status AS
SELECT
    status,
    COUNT(*) AS total_pedidos,
    SUM(valor) AS valor_total
FROM pedidos_silver
GROUP BY status;
