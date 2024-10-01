import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_listar_carros():
    response = client.get("/carros")
    assert response.status_code == 200
    assert len(response.json()) == 10 

def test_obter_carro_por_id():
    car_id = 1
    response = client.get(f"/carros/{car_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == car_id
    assert data["marca"] == "Toyota"
    assert data["modelo"] == "Corolla"

def test_adicionar_carro():
    novo_carro = {
        "id": 11,
        "marca": "Ferrari",
        "modelo": "F8",
        "ano": 2024
    }
    response = client.post("/carros", json=novo_carro)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 11
    assert data["marca"] == "Ferrari"
    assert data["modelo"] == "F8"
    assert data["ano"] == 2024

def test_deletar_carro():
    car_id = 1
    response = client.delete(f"/carros/{car_id}")
    assert response.status_code == 200
    assert response.json() == {"message": "Carro removido com sucesso"}
    
    # Verificar se o carro foi realmente removido
    response = client.get(f"/carros/{car_id}")
    assert response.status_code == 404

def test_obter_carro_inexistente():
    car_id = 999
    response = client.get(f"/carros/{car_id}")
    assert response.status_code == 404
    assert response.json() == {"detail": "Carro não encontrado"}
