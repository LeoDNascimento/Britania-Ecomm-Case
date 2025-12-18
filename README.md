# E-commerce – Integração de Pedidos

Este projeto implementa uma **arquitetura completa de integração de dados** entre sistemas,
simulando um cenário real de e-commerce com ingestão, persistência, camada analítica e visualização.

---

## Visão Geral da Arquitetura

CSV Upload (Streamlit)
│
▼
API FastAPI
│
▼
PostgreSQL
(Raw / Silver / Gold)
│
▼
Dataviz (Streamlit)


### Componentes
- **Streamlit (Ingestão)**: valida CSV e envia pedidos
- **API FastAPI**: recebe pedidos e persiste no banco
- **PostgreSQL**: armazena dados e executa transformações via SQL
- **Dataviz**: consome a camada Gold e exporta relatórios

---

## Estrutura do Repositório

```text
Britania-Ecomm-Case/
├── api/               # API de ingestão (FastAPI)
├── streamlit_app/     # Interface de upload e validação
├── data_lake/         # Camadas Raw, Silver e Gold (SQL)
├── dataviz/           # Visualização analítica e exportação CSV
├── docker-compose.yml # Orquestração dos serviços
└── README.md
```

---

## Camadas de Dados

| Camada | Implementação | Descrição                   |
| ------ | ------------- | --------------------------- |
| Raw    | Tabela        | Dados crus recebidos da API |
| Silver | View SQL      | Padronização leve           |
| Gold   | View SQL      | Agregações analíticas       |

As camadas Silver e Gold são views, garantindo dados sempre atualizados sem necessidade de jobs ou triggers.

# Execução do Projeto

```
docker-compose down -v
docker-compose up --build
```

## Serviços disponíveis

API (Swagger): http://localhost:8000/docs

Streamlit (Ingestão): http://localhost:8501

Dataviz (Gold): http://localhost:8502

# Documentação Detalhada por Serviço

Cada módulo possui documentação própria:

Streamlit (Upload & Validação)
streamlit_app/README.md

API FastAPI
api/README.md

Data Lake (Raw / Silver / Gold)
data_lake/README.md

📊 Dataviz & Exportação CSV
dataviz/README.md

## Testes

Testes automatizados na API com pytest

Validação de contratos e payloads

Documentação disponível no módulo da API