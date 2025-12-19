from pydantic import BaseModel
from typing import List

class Pedido(BaseModel):
    id_pedido: int
    cliente: str
    valor: float
    status: str

class PedidoBulk(BaseModel):
    pedidos: List[Pedido]