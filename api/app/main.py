from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Pedidos API")

app.include_router(router)
