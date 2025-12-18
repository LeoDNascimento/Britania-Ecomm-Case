FROM python:3.12-slim

# Evita arquivos .pyc e buffer no stdout
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Instalar dependências de sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Instalar Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"

# Copiar arquivos de dependência primeiro (cache de build)
COPY pyproject.toml poetry.lock* /app/

# Configurar Poetry para NÃO criar virtualenv
RUN poetry config virtualenvs.create false

# Instalar dependências
RUN poetry install --no-interaction --no-ansi --no-root

# Copiar código da aplicação
COPY app /app/app

# Expor porta
EXPOSE 8000

# Comando de inicialização
CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
