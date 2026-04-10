class Persona:
    def __init__(self, nombre: str) -> None:
        self._nombre = nombre

    @property
    def nombre(self):
        return self._nombre
