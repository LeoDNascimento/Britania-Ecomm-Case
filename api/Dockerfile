FROM python:3.12-slim

# Diretório de trabalho
WORKDIR /app

# Instala dependências de sistema necessárias
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Instala Poetry
RUN pip install poetry

# Desativa virtualenv dentro do container
RUN poetry config virtualenvs.create false

# Copia arquivos de dependência
COPY pyproject.toml poetry.lock ./

# Instala dependências
RUN poetry install --no-interaction --no-ansi

# Copia o código da aplicação
COPY app ./app

# Expõe a porta da API
EXPOSE 8000

# Comando de inicialização
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "]()
