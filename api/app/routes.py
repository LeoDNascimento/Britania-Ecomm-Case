from fastapi import APIRouter
from app.schemas import Pedido
from app.services import insert_pedido

router = APIRouter()

@router.post("/pedidos")
def criar_pedido(pedido: Pedido):
    insert_pedido(pedido)
    return {"message": "Pedido inserido com sucesso"}
