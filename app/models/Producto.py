class Producto:
  def __init__(self, nombre: str, precio: int) -> None:
    self._nombre = nombre
    self._precio = precio

  @property
  def nombre(self):
    return self._nombre
  
  @property
  def precio(self): 
    return self._precio