from fastapi.testclient import TestClient
from app.main import app
from app.models.Producto import Producto

client = TestClient(app)

def test_producto():
  producto = Producto("Menta Fresca 80g", 2500)
  assert producto.nombre == "Menta Fresca 80g"
  assert producto.precio == 2500
