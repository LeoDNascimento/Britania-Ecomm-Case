import requests
import os

API_URL = os.getenv("API_URL", "http://api:8000")


def send_pedido(pedido: dict):
    response = requests.post(
        f"{API_URL}/pedidos",
        json=pedido,
        timeout=10
    )
    response.raise_for_status()
    return response.json()


def send_pedido_bulky(pedido: dict):
    payload = {"pedidos": pedido}

    try:
        response = requests.post(
            f"{API_URL}/pedidos/bulk",
            json=payload,
            timeout= 10
        )

        response.raise_for_status()
        return response.json()

    except requests.exceptions.Timeout:
        raise RuntimeError("Timeout ao tentar se comunicar com a API.")

    except requests.exceptions.ConnectionError:
        raise RuntimeError("Não foi possível conectar à API.")

    except requests.exceptions.HTTPError as e:
        try:
            error_detail = response.json()
        except Exception:
            error_detail = response.text
        raise RuntimeError(f"Erro da API: {error_detail}") from e