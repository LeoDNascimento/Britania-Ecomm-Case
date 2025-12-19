# E-commerce – Integração de Pedidos

Este projeto implementa uma **arquitetura completa de integração de dados** entre sistemas,
simulando um cenário real de e-commerce com ingestão, persistência, camada analítica e visualização.

---

## Visão Geral da Arquitetura
```text
┌──────────────────────────┐
│   CSV Upload (Streamlit) │
└─────────────┬────────────┘
              │
              ▼
┌──────────────────────────┐
│      API FastAPI         │
└─────────────┬────────────┘
              │
              ▼
┌──────────────────────────┐
│      PostgreSQL          │
│  Raw • Silver • Gold     │
└─────────────┬────────────┘
              │
              ▼
┌──────────────────────────┐
│   Dataviz (Streamlit)    │
└──────────────────────────┘
```


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

[Streamlit (Upload & Validação)](./streamlit_app/README.md)

[Documentação da API](./api/README.md)

[Documentação do Data Lake](./data_lake/README.md)

[Documentação do Dataviz](./dataviz/README.md)

## O que o Docker executa (passo a passo)

O projeto utiliza **Docker Compose** para orquestrar todos os serviços.
A execução segue a ordem e responsabilidades descritas abaixo.

---

### 1. Criação da rede Docker

Ao executar:

```bash
docker compose up --build
```
O Docker cria automaticamente uma rede interna compartilhada, permitindo que
os containers se comuniquem entre si usando o nome do serviço (api, postgres, etc.).

### 2. Inicialização do PostgreSQL

O serviço postgres é iniciado primeiro.

Durante a primeira inicialização:

1. O container cria o banco orders

2. Executa automaticamente todos os scripts SQL presentes em:
```
/docker-entrypoint-initdb.d
```
3. Esses scripts criam:
- Tabela Raw;
- View Silver;
- View Gold.

Os scripts SQL estão versionados em data_lake/sql.

O Postgres expõe a porta 5432 e **só é considerado pronto após o healthcheck**.

### 3. Inicialização da API (FastAPI)

Após o Postgres ficar saudável:

1. O container da API é iniciado

2. O Docker executa o Dockerfile da API:

- Instala dependências com Poetry

- Inicia o servidor Uvicorn

3. A API fica disponível na porta 8000

4. A conexão com o banco é feita via:
```
postgresql://admin:admin@postgres:5432/orders
```
A API expõe endpoints REST para ingestão de pedidos.

### 4. Inicialização do Streamlit (Upload de CSV)

Com a API ativa:

1. O container do Streamlit é iniciado

2. O Docker executa o Dockerfile do Streamlit

3. A aplicação:

- Recebe upload de CSV

- Valida schema e tipos

- Aplica transformações

- Envia os dados em lote para a API

O Streamlit acessa a API pela rede Docker usando:
```
http://api:8000
```
A interface fica disponível na porta 8501.

### 5. Inicialização do Dataviz

O serviço dataviz é iniciado.

1. O container executa seu próprio Dockerfile

2. Conecta diretamente ao PostgreSQL

3. Consulta a camada Gold

4. Exibe:

- Tabela analítica

- Gráfico agregado

- Opção de exportação CSV

A aplicação fica disponível na porta 8502.

### Comunicação entre serviços

Dentro do Docker Compose, os containers não utilizam localhost. 
A comunicação ocorre via nome do serviço

Exemplo:

- Streamlit → API: http://api:8000

- API → Banco: postgres:5432

## Testes

Testes automatizados na API com pytest

Validação de contratos e payloads

Documentação disponível no módulo da API
