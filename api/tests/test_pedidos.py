def test_create_pedido_success(client):
    payload = {
        "id_pedido": 123,
        "cliente": "Teste",
        "valor": 1500.75,
        "status": "PENDENTE",
        "contagemCliente": 1
    }

    response = client.post("/pedidos", json=payload)

    assert response.status_code == 200
    assert response.json()["message"] == "Pedido inserido com sucesso"


def test_create_pedido_invalid_payload(client):
    payload = {
        "id_pedido": "abc",  # inválido
        "cliente": "Teste",
        "valor": 1500.75,
        "status": "PENDENTE",
        "contagemCliente": 1
    }

    response = client.post("/pedidos", json=payload)

    assert response.status_code == 422
