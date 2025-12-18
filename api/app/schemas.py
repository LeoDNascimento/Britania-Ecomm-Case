from pydantic import BaseModel

class Pedido(BaseModel):
    id_pedido: int
    cliente: str
    valor: float
    status: str
