from fastapi.testclient import TestClient

from app.main import app
from app.models.persona import Persona

client = TestClient(app)


def test_persona():
    persona = Persona("Pedro")
    assert persona.nombre == "Pedro"
