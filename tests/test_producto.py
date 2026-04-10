from fastapi.testclient import TestClient
from app.main import app
from app.models.Producto import Producto

client = TestClient(app)

def test_producto():
  producto = Producto("Cigarro", 5400)
  assert producto.nombre == "Cigarro"
  assert producto.precio == 5400
