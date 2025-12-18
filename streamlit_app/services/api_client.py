import requests

API_URL = "http://localhost:8000"

def send_pedido(pedido: dict):
    response = requests.post(
        f"{API_URL}/pedidos",
        json=pedido,
        timeout=10
    )
    response.raise_for_status()
    return response.json()
