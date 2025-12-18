FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Dependências de sistema
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Instalar Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"

# Copiar arquivos de dependência primeiro (cache)
COPY pyproject.toml poetry.lock* /app/

# Configurar Poetry
RUN poetry config virtualenvs.create false

# Instalar dependências (sem instalar o projeto como pacote)
RUN poetry install --no-interaction --no-ansi --no-root

# Copiar código
COPY app.py /app/app.py

# Expor porta padrão do Streamlit
EXPOSE 8501

# Comando de inicialização
CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0"]
