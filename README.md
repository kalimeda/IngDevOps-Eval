*Clonado de aerhedai/python-api-template con algunos archivos eliminados*

# Evaluación 1 Ingeniería DevOps

Como metodología de trabajo, hemos implementado *GitFlow*, una estrategia de ramificación que organiza el desarrollo en ramas de Producción, Desarrollo, Nuevas Funcionalidades, Preparación de Versiones y Correcciones Urgentes. Consideramos apropiada esta metodología para desacoplar, de forma estructurada, cada etapa del desarrollo de software; la rama de producción debe mantenerse *separada* de las funcionalidades experimentales.

### Naming de Ramas

- main: La rama principal, en la cual vive el código desplegable.
- develop: Desarrollo. Funcionalidades finalizadas, pero pendientes a revisión.
- feature/xyz: Funcionalidades individuales en desarrollo. Incompletas, incluso rotas.
- release/xyz: Preparación de versiones. Se revisan las nuevas funcionalidades para asegurar la correcta interacción entre componentes.
- hotfix/xyz: Correcciones urgentes al código desplegable.

### Flujo de Pull Requests

```

feature/abc
     |
     v          |--> release/v123 --|                    |-- hotfix/xyz
  develop --PR--|                   |--PR--> main <--PR--|
     ^          |--> release/v121 --|                    |-- hotfix/abc
     |
feature/xyz

```

### Estrategias de Revisión

Actualmente, se implementa GitHub Actions. Por cada push en la rama develop, y cada pull request en la rama main, se ejecutarán automáticamente las pruebas definidas en el directorio "tests" del proyecto.

### Buenas Prácticas

- Respetar el Naming de las ramas; no crear ramas como "pedrito". Toda rama feature y hotfix debe describir el trabajo que se está llevando a cabo dentro de ella.
- Los mensajes de commit deben ser breves y descriptivos. Ej. "Refactorizado modelo Personas" - NUNCA "Cambios pequeños" o "Código mejorado"

---

*README.md Original*

# Python API Boilerplate

A ready-to-use, Dockerized FastAPI boilerplate for building scalable and maintainable Python APIs quickly. This boilerplate provides a modular folder structure, logging, routing, and example code to get you started with building your own APIs efficiently.

---

## Features

- ⚡ FastAPI framework with automatic docs (`/docs` and `/redoc`)
- 🧱 Modular code organisation (routes, services, models, utils)
- 🐳 Docker support for consistent local development and deployment
- 📜 Logging included for easier debugging and monitoring
- 🚀 Easily extendable for real projects

---

## Directory Structure

```
.
├── app/
│   ├── api/
│   │   └── routes.py           # API route definitions
│   ├── services/
│   │   └── example.py          # Business logic/services
│   ├── models/
│   │   └── example_schema.py   # Pydantic models for validation
│   ├── core/
│   │   └── config.py           # Pydantic config for setup
│   ├── utils/
│   │   └── logging.py          # Logger setup
│   ├── main.py                 # FastAPI app setup and route inclusion
├── tests/
│   └── test_example.py         # Example unit tests
├── Dockerfile                  # Docker configuration
├── requirements.txt            # Python dependencies
├── README.md                   # Project readme
├── .gitignore                  # Ignore rules
├── LICENSE                     # Distribution and Usage License
├── .env.example                # Environmental variable examples
├── CHANGELOG.md                # API boilerplate changelog
```

---

## Getting Started

### 🔧 Prerequisites

- Docker installed on your machine
- (Optional) Python 3.9+ if not using Docker

### 🚀 Running with Docker

1. Build the image:
   ```bash
   docker build -t api-boilerplate .
   ```

2. Run the container:
   ```bash
   docker run -p 8000:8080 api-boilerplate
   ```

3. Access your API:
   - API base: http://localhost:8000
   - Swagger UI: http://localhost:8000/docs
   - ReDoc: http://localhost:8000/redoc

---

### 🧪 Running Locally (without Docker)

1. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate        # macOS/Linux
   venv\Scripts\activate           # Windows
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
   ```

---

## 🛠️ Extending the Boilerplate

- **Add Routes:**  
  Define new endpoints in `app/api/` and register them via the router.

- **Add Services:**  
  Place logic in `app/services/` and call from your routes.

- **Define Models:**  
  Use Pydantic in `app/models/` for request/response validation.

- **Utilities:**  
  Add helpers/loggers in `app/utils/`.

- **Tests:**  
  Write unit and integration tests in `tests/`.

- **Environment Configs (optional):**  
  Use `python-dotenv` or other tools for managing environment variables.

---

## ✅ Notes

- Docker exposes port 8080 (internal) as 8000 (host).
- Modify the Dockerfile or FastAPI config if you want different ports.
- Structure is suitable for scaling: you can add auth, DB, caching, etc.

---

## 🧪 Example Endpoint

Try:
```
GET http://localhost:8000/example
```

Response:
```json
{
  "message": "Hello from the example service!"
}
```

---

## 🧾 License

MIT License. Feel free to use and modify.

---

## 🙌 Contributing

Pull requests welcome! Open an issue for feature requests or bugs.

---
