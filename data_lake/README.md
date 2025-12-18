# Data Lake – Camadas Raw, Silver e Gold

Este módulo é responsável pela **camada analítica do projeto**, utilizando **PostgreSQL + SQL puro** para organizar os dados em camadas conceituais **Raw, Silver e Gold**.

---

## Objetivo

- Organizar os dados recebidos pela API em camadas analíticas
- Garantir dados sempre atualizados sem jobs ou triggers
- Permitir fácil consumo por dashboards e exportação de relatórios
- Manter todas as transformações **versionadas em SQL**

---

## Arquitetura de Dados

pedidos_raw (Raw / Bronze)
│
▼
pedidos_silver (Silver)
│
▼
pedidos_por_status (Gold)


### Conceitos
- **Raw**: dados crus, exatamente como chegam da API
- **Silver**: padronização e limpeza leve
- **Gold**: agregações analíticas prontas para consumo

---

## 📂 Estrutura do Diretório

```text
data_lake/
├── sql/
│   ├── 01_create_raw.sql
│   ├── 02_create_silver.sql
│   └── 03_create_gold.sql
└── README.md
```

---
## Estruturas das Camadas

🟤 Camada Raw (Bronze)
Tabela: pedidos_raw
Script: 1_bronze.sql

Responsável por armazenar os pedidos sem transformação, servindo como fonte de verdade.

---

⚪ Camada Silver
View: pedidos_silver
Script: 2_silver.sql

Aplica padronizações leves, preparando os dados para análises.

---

🟡 Camada Gold
View: pedidos_por_status
Script: 3_gold.sql

    Camada analítica final, com métricas agregadas.

    Esta view atende diretamente ao requisito de:

    - Total de pedidos por status

    - Valor total por status

# Execução dos Scripts SQL
## Execução automática via Docker

Os scripts são executados automaticamente na primeira inicialização do PostgreSQL, pois a pasta data_lake/sql é montada em:

/docker-entrypoint-initdb.d



## Execução manual (modo desenvolvimento)

Durante o desenvolvimento, os scripts podem ser executados diretamente no container:
```
docker exec -i postgres psql -U admin -d orders < data_lake/sql/1_bronze.sql
docker exec -i postgres psql -U admin -d orders < data_lake/sql/2_silver.sql
docker exec -i postgres psql -U admin -d orders < data_lake/sql/3_gold.sql
```
Ou todos de uma vez:
```
cat data_lake/sql/*.sql | docker exec -i postgres psql -U admin -d orders
```

# Atualização dos Dados

Como Silver e Gold são views, não existe necessidade de Jobs, Triggers ou Refresh manual

Sempre que novos dados são inseridos em pedidos_raw, as camadas analíticas refletem automaticamente as mudanças.