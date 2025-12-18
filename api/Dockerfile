FROM python:3.12.6

WORKDIR /app

# Instala Poetry
RUN pip install poetry

# Copia arquivos de dependência
COPY pyproject.toml poetry.lock ./

# Instala dependências
RUN poetry install --no-root

# Copia código da aplicação
COPY app ./app

# Expõe porta da API
EXPOSE 8000

# Comando de inicialização
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
