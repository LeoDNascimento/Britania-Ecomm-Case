# API de Ingestão de Pedidos

Esta API é responsável pela **ingestão confiável de pedidos**, recebendo dados validados pela camada de interface (Streamlit) e persistindo-os no **PostgreSQL (camada Bronze / Raw)**.

Ela foi construída com foco em:
- Separação de responsabilidades
- Contratos claros
- Facilidade de testes
- Prontidão para containerização (Docker)

---

## Objetivo

- Receber pedidos via API REST
- Validar o payload automaticamente
- Persistir os dados no banco PostgreSQL
- Servir como camada de ingestão desacoplada do frontend

---

## Arquitetura

Streamlit
|
| POST /pedidos
v
FastAPI
|
v
PostgreSQL (pedidos_raw)

---

## Tecnologias Utilizadas

- **Python 3.10+**
- **FastAPI**
- **Pydantic**
- **PostgreSQL**
- **Poetry**
- **Docker**
- **pytest**

---

## Estrutura do Projeto

```text
api/
├── app/
│   ├── __init__.py
│   ├── main.py        # Inicialização da aplicação
│   ├── routes.py      # Definição das rotas
│   ├── schemas.py     # Contratos de entrada (Pydantic)
│   ├── services.py    # Lógica de persistência
│   └── database.py    # Conexão com o PostgreSQL
│
├── tests/
│   ├── conftest.py    # Fixtures compartilhadas
│   ├── test_pedidos.py
│   └── test_healthcheck.py
│
├── Dockerfile
├── pyproject.toml
└── README.md

```

## Endpoints Disponíveis

### Healthcheck
GET /
Endpoint simples para verificar se a API está ativa.

```
{
  "status": "ok"
}
```

### Criar Pedido
POST /pedidos
Recebe um pedido individual e o persiste no banco de dados.

```
{
  "id_pedido": 101,
  "cliente": "Ana",
  "valor": 1500.75,
  "status": "PENDENTE"
}

```
### Erros
| Código | Descrição                          |
| ------ | ---------------------------------- |
| 422    | Payload inválido                   |
| 500    | Erro interno ao persistir no banco |



# Como executar a API

## Usando Poetry
```
poetry install
poetry run python -m uvicorn app.main:app --reload
```
Acessar SWAGGER:
/docs

## Usando PIP
```
python -m venv .venv
source .venv/bin/activate
pip install fastapi uvicorn psycopg2-binary python-dotenv
python -m uvicorn app.main:app --reload

```
Acessar SWAGGER:
/docs

# EXECUTAR DOCKER

Raiz do projeto:
```
docker-compose up --build
```


# Rodar Testes

```
poetry run pytest -v

OU

pytest -v
no pip

```
