from fastapi import APIRouter, HTTPException
from app.schemas import Pedido, PedidoBulk
from app.services import insert_pedido, insert_pedidos_bulk

router = APIRouter()

@router.post("/pedidos")
def criar_pedido(pedido: Pedido):
    insert_pedido(pedido)
    return {"message": "Pedido inserido com sucesso"}

@router.post("/pedidos/bulk")
def create_pedidos_bulk(payload: PedidoBulk):
    try:
        insert_pedidos_bulk(payload.pedidos)
        return {
            "message": f"{len(payload.pedidos)} pedidos inseridos com sucesso"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
