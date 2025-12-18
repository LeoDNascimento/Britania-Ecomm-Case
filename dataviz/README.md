# Dataviz – Camada Gold

Este módulo é responsável pela **visualização dos dados analíticos** da camada Gold,
consumindo diretamente a view `pedidos_por_status` no PostgreSQL.

---

## Objetivo

- Exibir métricas agregadas por status
- Visualizar os dados em tabela e gráfico
- Permitir exportação do relatório em CSV

---

## Estrutura

```text
dataviz/
├── app.py
├── pyproject.toml
└── README.md
```