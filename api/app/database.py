import os
import psycopg2

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://admin:admin@localhost:5432/orders"
)

def get_connection():
    return psycopg2.connect(DATABASE_URL)
