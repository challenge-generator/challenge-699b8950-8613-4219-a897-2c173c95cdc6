# AGENTS.md

Instrucciones para el agente de IA que abra este repositorio (Claude Code, Cursor, Codex, Copilot, Gemini). Se cargan solas: no hay que pegar nada en ningun chat.

## Que es este repositorio

Es el codigo base de un reto de aprendizaje de Pragma: **Construcción de una API REST para gestión de productos**.

| | |
|---|---|
| Tema | Representational State Transfer (REST) |
| Nivel | advanced-l2 |
| Chapter | Ciencia de Datos — Ingeniero de Datos |
| Especialidad | Python |
| Stack | Python / FastAPI 0.115 |
| Patron arquitectonico | capas estándar (dominio, aplicación, infraestructura) |
| Tiempo estimado | 10 horas |

## Mapa de componentes

El repo tiene una carpeta por componente. Cada uno se instala y verifica dentro de la suya.

| Componente | Carpeta | Rol | Capa | Track | Tecnologias |
|---|---|---|---|---|---|
| `api` | `api/` | practice | server | Python | Amazon API Gateway |
| `data` | `data/` | chapter, support | data | Ingeniero de datos | - |

## Orden de arranque

1. `cd api && pip install -r requirements.txt && python -m compileall -q app && python -c "import app"` — componente `api` (practice).
2. `cd data && pip install -e . && python src/main.py` — componente `data` (chapter, support).

### Contratos entre componentes

- `api` expone http (api: http://localhost:8000):
  - `POST /products`
  - `GET /products/{product_id}`
  - `PUT /products/{product_id}`
  - `DELETE /products/{product_id}`
  - `GET /products`

## Receta del stack

Esqueleto obligatorio:

- `pyproject.toml o requirements.txt en la raiz`
- `app/main.py con la instancia de FastAPI`
- `app/domain con entidades y puertos (Protocol o ABC)`
- `app/application con casos de uso`
- `app/infrastructure con repositorios y routers`

Dependencias:

- fastapi ==0.162.4
- uvicorn ==0.54.0
- pydantic ==2.14.3
- pytest ==9.2.0
- httpx ==0.28.1
- asyncpg ==0.32.0
- psycopg2-binary ==2.9.13
- pytest-asyncio ==1.5.0
- python-dotenv ==1.2.4
- sqlalchemy ==2.1.9

## Tu tarea

Dejar este proyecto en estado **verificable**: que el comando de verificacion corra sin errores. Escribi los archivos en disco, en este repositorio. No generes ZIPs ni archivos adjuntos.

En orden:

1. Segui el orden de arranque del mapa de componentes (infraestructura local primero) y corre `(cd api && pip install -r requirements.txt && python -m compileall -q app && python -c "import app") && (cd data && pip install -e . && python src/main.py)` desde la raiz: mira que falla.
2. Completa lo que falte de la lista de abajo: manifiesto de dependencias, punto de entrada, capa de interfaz y las capas del patron declarado.
3. Arregla SOLO los errores que impiden compilar o arrancar.
4. Volve a correr `(cd api && pip install -r requirements.txt && python -m compileall -q app && python -c "import app") && (cd data && pip install -e . && python src/main.py)` hasta que pase.
5. Pará ahí.

## Regla dura: las fases son trabajo del humano

**PROHIBIDO implementar los entregables de las fases.** El valor del reto esta en que la persona los resuelva. Tu trabajo es que tenga un proyecto que arranca; el hueco pedagogico se queda como esta.

No resuelvas nada de esto:

- **Fase 1 — Definición del modelo de producto**: Modelo de producto definido con sus atributos y restricciones.
- **Fase 2 — Implementación de endpoints CRUD**: Endpoints REST implementados para las operaciones CRUD sobre productos.
- **Fase 3 — Manejo de casos límite y errores**: Lógica implementada para manejar casos límite y errores del dominio.
- **Fase 4 — Optimización y refactorización**: Implementación optimizada y refactorizada de la API REST.

Distincion operativa:

- **Arreglar** (si): import faltante, tipo que no existe, dependencia sin declarar, error de sintaxis, archivo referenciado que no existe.
- **No tocar** (no): logica de negocio incompleta, validaciones ausentes, secretos hardcodeados, APIs deprecadas que funcionan, concurrencia insegura, patrones mejorables. Eso es lo que la persona tiene que encontrar.

## Superficie de practica (NO completes)

Estos archivos SON el ejercicio de la persona. No los implementes; deja stubs. No toques la logica que el reto pide completar.

- [ ] `api/app/api/routers.py` — La fase "Definición del modelo de producto" se implementa aqui: este archivo es el ejercicio.
- [ ] `api/app/application/services.py` — La fase "Implementación de endpoints CRUD" se implementa aqui: este archivo es el ejercicio.
- [ ] `api/app/infrastructure/database.py` — La fase "Definición del modelo de producto" ya venia resuelta por el codigo base: este archivo pasa a ser el ejercicio.

## Lo que falta y tenes que completar

Referencias no verificadas para: .py. El analisis estatico no cubre esos lenguajes: que no se haya listado nada NO garantiza que no haya referencias colgando. Corre el comando de verificacion para encontrarlas.

### 1. Boilerplate del stack (1)

Sin esto el proyecto no compila ni arranca. **Es tu trabajo crearlo**, y no toca nada de lo pedagogico: es andamiaje del stack.

- [ ] **api/app/__init__.py** — Sin __init__.py, app no es un paquete importable y "import app.main" falla.

### 2. Referencias colgando (2)

Salieron de un analisis estatico del codigo que SI esta en el repo. Cada una rompe la compilacion:

- [ ] `api/app/infrastructure/repositories.py` — `ProductCreate.model_dump`
      Se invoca `model_dump` sobre `ProductCreate`, pero esa clase no declara ese metodo. Agregalo con su implementacion real, o usa uno de los que si declara.
- [ ] `api/app/infrastructure/repositories.py` — `ProductUpdate.model_dump`
      Se invoca `model_dump` sobre `ProductUpdate`, pero esa clase no declara ese metodo. Agregalo con su implementacion real, o usa uno de los que si declara.

### Presentes (20)

- `api/main.py`
- `api/requirements.txt`
- `api/app/domain/models.py`
- `api/app/domain/exceptions.py`
- `api/app/domain/repositories.py`
- `api/app/application/services.py`
- `api/app/infrastructure/repositories.py`
- `api/app/infrastructure/database.py`
- `api/app/api/dependencies.py`
- `api/app/api/routers.py`
- `api/app/app.py`
- `data/pyproject.toml`
- `data/src/infrastructure/__init__.py`
- `data/src/infrastructure/database.py`
- `data/src/main.py`
- `data/src/contracts/__init__.py`
- `data/src/domain/models/product.py`
- `data/src/domain/repositories/product_repository.py`
- `data/src/domain/migrations/env.py`
- `data/src/domain/migrations/versions/initial_migration.py`

### Capas del patron declarado

Son las capas que la propuesta arquitectonica plantea, marcadas segun existan hoy en el repo. Orientan donde poner el codigo nuevo; no son una condicion para compilar.

- `api` (presente)
- `api/app/domain` (presente)
- `api/app/application` (presente)
- `api/app/infrastructure` (presente)
- `api/app/api` (presente)
- `api/tests` (ausente)
- `data` (presente)
- `data/data/models` (ausente)
- `data/data/repositories` (ausente)
- `data/data/migrations` (ausente)

## Verificacion

```bash
(cd api && pip install -r requirements.txt && python -m compileall -q app && python -c "import app") && (cd data && pip install -e . && python src/main.py)
```

El comando tiene que pasar SIN implementar los archivos de la superficie de practica: solo andamiaje.

Ese comando pasando es la definicion de "terminado" para vos.

## Convenciones que tenes que respetar

- Un solo ecosistema: no declares librerias de otro lenguaje ni mezcles gestores de paquetes.
- Toda libreria que uses tiene que estar declarada en el manifiesto de dependencias.
- Todo import declarado tiene que usarse; todo tipo usado tiene que existir o venir de una dependencia declarada.
- Cada componente vive en su carpeta: instala y compila dentro de ella, y no muevas archivos entre componentes.
- Respeta los contratos entre componentes (endpoints, topics) tal como estan declarados en el mapa de componentes.
- El patron es **capas estándar (dominio, aplicación, infraestructura)**: los contratos (interfaces, puertos) los define la capa interna y los implementa la externa, nunca al revés.
- Los archivos que crees llevan implementacion real, no stubs: sin `TODO`, sin cuerpos vacios, sin `// getters y setters`.

## Contexto del candidato

Sirve para calibrar el nivel del codigo, no para resolver las fases.

- Perfil: Chapter Ciencia de Datos, Especialidad Ingeniero de Datos, Tecnología Python, Advanced L2
- Brecha que el reto ataca: Realiza por medio de un Framework sobre su lenguaje de programacion primario, enrutamiento de peticiones, consultas, creación de un API REST., Realiza por medio de un Framework sobre su lenguaje de programacion primario, enrutamiento de peticiones, consultas, creación de un API REST.

---

*Generado por Challenge Generator — Pragma. `README.md` tiene el enunciado completo del reto para la persona. `PROMPT_MEJORA.md` es la variante para pegar en un chat, si se prefiere ese flujo.*
