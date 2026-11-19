# Construcción de una API REST para gestión de productos

Como Ingeniero de Datos en una fintech, debes construir una API REST que gestione productos. La API debe permitir la creación, lectura, actualización y eliminación de productos. Cada producto tiene un nombre, precio, stock y categoría. Debes asegurar que los nombres de los productos sean únicos y que los precios no sean negativos. Además, debes manejar adecuadamente los errores y casos límite del dominio.

## Informacion General

| Campo | Valor |
|-------|-------|
| **Tema** | Representational State Transfer (REST) |
| **Nivel** | advanced-l2 |
| **Tipo** | practical |
| **Tiempo estimado** | 10 horas |

## Fases del Reto

### Fase 0: Configuración del Proyecto

**Objetivo:** Obtener el proyecto base funcional enviando el Código Base a un asistente de IA, que lo analizará, corregirá errores y entregará cada archivo con su ruta.

**Tiempo estimado:** 15-30 minutos

**Instrucciones:**

- Asegúrate de tener instalado para ejecutar el proyecto: Python 3.10+, pip, VS Code o similar.
- Copia todo el contenido del campo **Código Base** de este reto — incluyendo el texto de instrucciones que aparece al inicio.
- Abre un asistente de IA (Claude en claude.ai, ChatGPT o Gemini — se recomienda Claude), pega el contenido copiado en el chat y envíalo.
- El asistente analizará los archivos, corregirá errores y entregará cada archivo con su ruta. Guárdalos en la carpeta donde quieras trabajar, respetando las rutas.
- Ejecuta `pip install -r requirements.txt` y luego arranca el proyecto. Si no hay errores, estás listo.

**Entregable:** El proyecto compila/arranca sin errores.

<details>
<summary>Pistas de conocimiento</summary>

- Copia el Código Base completo incluyendo el texto de instrucciones al inicio — esas instrucciones le indican al asistente exactamente qué hacer con los archivos.
- Si el asistente no entrega todos los archivos al terminar el análisis, escríbele: "entrégame todos los archivos con su ruta".
- Si el proyecto tiene errores al arrancar, comparte el mensaje de error con el mismo asistente para que lo corrija.

</details>

### Fase 1: Definición del modelo de producto

**Objetivo:** Definir el modelo de producto con sus atributos y restricciones.

**Tiempo estimado:** 2 horas

**Instrucciones:**

- Identifica los atributos necesarios para un producto (nombre, precio, stock, categoría).
- Establece las restricciones para los atributos (nombres únicos, precios no negativos).

**Entregable:** Modelo de producto definido con sus atributos y restricciones.

<details>
<summary>Pistas de conocimiento</summary>

- Considera cómo representar los atributos del producto en el modelo de datos.
- Piensa en las validaciones necesarias para asegurar la integridad de los datos.

</details>

### Fase 2: Implementación de endpoints CRUD

**Objetivo:** Implementar los endpoints para crear, leer, actualizar y eliminar productos.

**Tiempo estimado:** 4 horas

**Instrucciones:**

- Implementa los endpoints REST para las operaciones CRUD sobre productos.
- Asegura que los endpoints manejen adecuadamente las validaciones y errores.

**Entregable:** Endpoints REST implementados para las operaciones CRUD sobre productos.

<details>
<summary>Pistas de conocimiento</summary>

- Considera cómo estructurar los endpoints para que sean intuitivos y seguidos.
- Piensa en las respuestas HTTP adecuadas para cada tipo de error.

</details>

### Fase 3: Manejo de casos límite y errores

**Objetivo:** Manejar adecuadamente los casos límite y errores del dominio.

**Tiempo estimado:** 2 horas

**Instrucciones:**

- Identifica los casos límite y errores comunes en el dominio de productos.
- Implementa la lógica para manejar estos casos y errores de manera adecuada.

**Entregable:** Lógica implementada para manejar casos límite y errores del dominio.

<details>
<summary>Pistas de conocimiento</summary>

- Considera cómo detectar y manejar casos como productos con stock cero o categorías inválidas.
- Piensa en cómo comunicar estos errores al usuario de la API de manera clara y concisa.

</details>

### Fase 4: Optimización y refactorización

**Objetivo:** Optimizar y refactorizar la implementación de la API REST.

**Tiempo estimado:** 2 horas

**Instrucciones:**

- Identifica áreas de la implementación que pueden ser optimizadas o refactorizadas.
- Aplica técnicas de optimización y refactorización para mejorar el rendimiento y mantenibilidad de la API.

**Entregable:** Implementación optimizada y refactorizada de la API REST.

<details>
<summary>Pistas de conocimiento</summary>

- Considera cómo reducir la complejidad de la lógica de negocio.
- Piensa en cómo mejorar la mantenibilidad del código a largo plazo.

</details>

## Dimensiones Evaluadas

- **queEs**: ¿Qué es una API REST y cuáles son sus componentes principales?
- **paraQueSirve**: ¿Para qué sirve una API REST en el contexto de una fintech?
- **comoSeUsa**: ¿Cómo se usan los endpoints REST para realizar operaciones CRUD sobre productos?
- **erroresComunes**: ¿Cuáles son los errores comunes al implementar una API REST y cómo se pueden manejar?
- **queDecisionesImplica**: ¿Qué decisiones de diseño implica la implementación de una API REST robusta y escalable?

## Criterios de Evaluacion

- Definición del modelo de producto con atributos y restricciones.
- Implementación de endpoints REST para operaciones CRUD.
- Manejo adecuado de casos límite y errores del dominio.
- Optimización y refactorización de la implementación de la API REST.

## Como trabajar con un asistente de IA

Hay dos caminos, elegi uno:

- **AGENTS.md** (recomendado) — instrucciones nativas del repo. Abri esta carpeta con tu agente local (Claude Code, Cursor, Codex, Copilot, Gemini) y las carga solo. Sabe que archivos faltan y con que comando se verifica, y completa el scaffold escribiendo en disco.
- **PROMPT_MEJORA.md** — para copiar y pegar en un chat (claude.ai, ChatGPT) si no tenes un agente en el IDE. Declara lo mismo que AGENTS.md; los archivos que te devuelva el chat los guardas en esta carpeta respetando las rutas.

Ninguno de los dos resuelve las fases del reto: eso es tu trabajo.

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

## Verificacion

El proyecto esta listo para trabajar cuando este comando corre sin errores:

```bash
(cd api && pip install -r requirements.txt && python -m compileall -q app && python -c "import app") && (cd data && pip install -e . && python src/main.py)
```

---

*Reto generado automaticamente por Challenge Generator - Pragma*
