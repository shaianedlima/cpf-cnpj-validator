from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_validar_cpf_valido():
    response = client.post("/validar/cpf", json={"numero": "52998224725"})
    assert response.status_code == 200
    corpo = response.json()
    assert corpo["valido"] is True
    assert corpo["formatado"] == "529.982.247-25"


def test_validar_cnpj_invalido():
    response = client.post("/validar/cnpj", json={"numero": "11111111111111"})
    assert response.status_code == 200
    corpo = response.json()
    assert corpo["valido"] is False
    assert corpo["formatado"] is None
