<h1 align="center">✨ Reto Técnico FullStack - Casa Mecate</h1>

<p align="center">
  <b>FullStack Technical Challenge</b><br/>
  <i>API REST + SQL Database + Angular Dashboard + Docker + HTTPS + Unit Tests</i>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Backend-FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white"/>
  <img src="https://img.shields.io/badge/Language-Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Frontend-Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white"/>
  <img src="https://img.shields.io/badge/Database-SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white"/>
  <img src="https://img.shields.io/badge/Docker-Enabled-2496ED?style=for-the-badge&logo=docker&logoColor=white"/>
  <img src="https://img.shields.io/badge/Swagger-OpenAPI-85EA2D?style=for-the-badge&logo=swagger&logoColor=black"/>
  <img src="https://img.shields.io/badge/Tests-Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white"/>
</p>

---

## 🧩 Description | Descripción

**EN 🇺🇸**  
This project is a FullStack technical challenge developed for Casa Mecate. It implements a complete flow from SQL data storage and external API consumption to backend processing and frontend visualization.

The application includes:

- A REST API built with Python and FastAPI.
- A SQL database using SQLite.
- External data consumption from StackExchange / StackOverflow API.
- A frontend dashboard built with Angular.
- Dockerized backend.
- Swagger/OpenAPI documentation.
- Unit tests with pytest.
- HTTPS support using a self-signed certificate inside Docker.
- Frontend interaction logs sent to the backend.

**ES 🇲🇽**  
Este proyecto es una prueba técnica FullStack desarrollada para Casa Mecate. Implementa un flujo completo desde almacenamiento de datos SQL y consumo de una API externa, hasta procesamiento en backend y visualización en frontend.

La aplicación incluye:

- Una API REST desarrollada con Python y FastAPI.
- Una base de datos SQL utilizando SQLite.
- Consumo de datos externos desde la API de StackExchange / StackOverflow.
- Un dashboard frontend desarrollado en Angular.
- Backend dockerizado.
- Documentación Swagger/OpenAPI.
- Pruebas unitarias con pytest.
- Soporte HTTPS con certificado autofirmado dentro de Docker.
- Logs de interacción del frontend enviados hacia el backend.

---

## 🎯 Problem | Problema

**EN 🇺🇸**  
The challenge required building a small but complete FullStack application where:

- The backend consumes data from an external API.
- SQL data is stored in a database.
- Backend endpoints expose processed data.
- The frontend consumes all API services.
- The backend is dockerized.
- The project is easy to run, review and understand.

**ES 🇲🇽**  
El reto solicitaba construir una aplicación FullStack pequeña pero completa donde:

- El backend consuma datos desde una API externa.
- Los datos SQL se almacenen en una base de datos.
- El backend exponga la información procesada mediante endpoints.
- El frontend consuma todos los servicios de la API.
- El backend esté dockerizado.
- El proyecto sea fácil de ejecutar, revisar y entender.

---

## 💡 Solution | Solución

**EN 🇺🇸**  
The solution was implemented with a layered architecture. The backend works as the main intermediary between the external API, the SQL database and the Angular frontend.

Angular does not directly consume StackOverflow or the database. Instead, Angular consumes clean REST endpoints exposed by FastAPI.

**ES 🇲🇽**  
La solución se implementó con una arquitectura por capas. El backend funciona como intermediario principal entre la API externa, la base de datos SQL y el frontend en Angular.

Angular no consume directamente StackOverflow ni la base de datos. En su lugar, consume endpoints REST limpios expuestos por FastAPI.

```txt
SQL Database      -> Backend FastAPI -> Angular Dashboard
External JSON API -> Backend FastAPI -> Angular Dashboard
Frontend Events   -> Backend Logs
```

---

## ⚙️ Stack

| Layer | Technology |
|---|---|
| Backend | Python |
| API Framework | FastAPI |
| Frontend | Angular |
| Language | TypeScript |
| Database | SQLite |
| API Documentation | Swagger / OpenAPI |
| Containerization | Docker / Docker Compose |
| Unit Testing | pytest + FastAPI TestClient |
| HTTPS | Self-signed certificate + Uvicorn SSL |
| External API | StackExchange API |
| Styling | SCSS / Tailwind utility classes |

---

## ✨ Features | Funcionalidades

**EN 🇺🇸**

- REST API with FastAPI.
- StackOverflow API consumption from backend.
- SQL database initialization and seed.
- SQL queries exposed through API endpoints.
- Angular dashboard consuming backend services.
- Sidebar navigation.
- Light and dark mode.
- Interactive sections for StackOverflow and flights.
- Tables, cards and explanatory blocks.
- Swagger documentation.
- Dockerized backend.
- HTTPS with self-signed certificate.
- Unit tests with pytest.
- Frontend event logging into backend console.

**ES 🇲🇽**

- API REST con FastAPI.
- Consumo de StackOverflow API desde el backend.
- Inicialización y carga de datos en SQLite.
- Consultas SQL expuestas mediante endpoints.
- Dashboard en Angular consumiendo servicios del backend.
- Navegación lateral.
- Modo claro y modo oscuro.
- Secciones interactivas para StackOverflow y vuelos.
- Tablas, cards y bloques explicativos.
- Documentación Swagger.
- Backend dockerizado.
- HTTPS con certificado autofirmado.
- Pruebas unitarias con pytest.
- Logs de eventos del frontend en la consola del backend.

---

## 🧠 Architecture | Arquitectura

```txt
DesTecFullStack/
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── database.py
│   │   ├── seed.py
│   │   ├── routes/
│   │   │   ├── stackoverflow.py
│   │   │   └── flights.py
│   │   └── services/
│   │
│   ├── tests/
│   │   ├── test_root.py
│   │   ├── test_stackoverflow.py
│   │   └── test_flights.py
│   │
│   ├── Dockerfile
│   ├── requirements.txt
│   └── pytest.ini
│
├── frontend/
│   ├── src/
│   │   ├── app/
│   │   │   ├── services/
│   │   │   │   └── api.ts
│   │   │   ├── app.ts
│   │   │   ├── app.html
│   │   │   └── app.scss
│   │   └── styles.scss
│   │
│   ├── angular.json
│   └── package.json
│
├── docker-compose.yml
├── .gitignore
└── README.md
```

---

## 🔁 Data Flow | Flujo de datos

```txt
SQL -> Backend
JSON/API externa -> Backend
Backend -> Vista Angular
```

Detailed flow:

```txt
SQLite Database
      ↓
FastAPI Backend
      ↓
REST Endpoints
      ↓
Angular Frontend
      ↓
Visual Dashboard
```

```txt
StackExchange API
      ↓
FastAPI Backend
      ↓
Processed JSON
      ↓
Angular Dashboard
```

```txt
Angular User Interaction
      ↓
POST /api/logs/frontend-event
      ↓
Backend Console Logs / Docker Logs
```

---

# 🐍 Backend

## StackOverflow API consumption

The backend consumes the following external endpoint:

```txt
https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=perl&site=stackoverflow
```

The backend acts as an intermediary between StackOverflow and Angular. Angular does not consume StackOverflow directly.

---

## StackOverflow endpoints

| Requirement | Endpoint | Status |
|---|---|---|
| Number of answered and unanswered questions | `GET /api/stackoverflow/answered-summary` | Completed |
| Question related to the owner with highest reputation | `GET /api/stackoverflow/highest-reputation` | Completed |
| Question with lowest number of views | `GET /api/stackoverflow/lowest-views` | Completed |
| Oldest and newest question | `GET /api/stackoverflow/oldest-newest` | Completed |
| Print results from points 2 to 5 in console | `GET /api/stackoverflow/console-report` | Completed |

Additional helper endpoints:

| Endpoint | Description |
|---|---|
| `GET /api/stackoverflow/oldest` | Returns only the oldest question |
| `GET /api/stackoverflow/newest` | Returns only the newest question |

---

## StackOverflow console report

The endpoint:

```txt
GET /api/stackoverflow/console-report
```

prints a real report in the backend console / Docker logs:

```txt
====================================================
REPORTE STACKOVERFLOW - RETO TÉCNICO CASA MECATE
====================================================

[PUNTO 2] Pregunta asociada al usuario con mayor reputación:
Título: How do you read the system time and date in Perl?
Usuario: Bill the Lizard
Reputación: 407715
Link: https://stackoverflow.com/questions/487791/how-do-you-read-the-system-time-and-date-in-perl

[PUNTO 3] Pregunta con menor número de vistas:
Título: Disable Perl warnings for call to remote function
Vistas: 102
Link: https://stackoverflow.com/questions/79761082/disable-perl-warnings-for-call-to-remote-function

[PUNTO 4] Pregunta más vieja:
Título: How do you read the system time and date in Perl?
Fecha de creación: 2009-01-28 14:23:43
Link: https://stackoverflow.com/questions/487791/how-do-you-read-the-system-time-and-date-in-perl

[PUNTO 4] Pregunta más actual:
Título: Ffailing to build OpenSSL from msquic via PowerShell during cross compiling due to perl errors
Fecha de creación: 2026-04-20 16:50:49
Link: https://stackoverflow.com/questions/79928933/ffailing-to-build-openssl-from-msquic-via-powershell-during-cross-compiling-due

====================================================
FIN DEL REPORTE STACKOVERFLOW
====================================================
```

---

# 🗄️ SQL Database

## Database

**EN 🇺🇸**  
SQLite was used as the SQL database because it is lightweight, portable and easy to run inside the challenge environment.

**ES 🇲🇽**  
Se utilizó SQLite como base de datos SQL porque es ligera, portable y fácil de ejecutar dentro del entorno del reto.

---

## Tables | Tablas

### Airlines | Aerolíneas

| id_aerolinea | nombre_aerolinea |
|---|---|
| 1 | Volaris |
| 2 | Aeromar |
| 3 | Interjet |
| 4 | Aeromexico |

### Airports | Aeropuertos

| id_aeropuerto | nombre_aeropuerto |
|---|---|
| 1 | Benito Juarez |
| 2 | Guanajuato |
| 3 | La Paz |
| 4 | Oaxaca |

### Movements | Movimientos

| id_movimiento | descripcion |
|---|---|
| 1 | Salida |
| 2 | Llegada |

### Flights | Vuelos

| id_aerolinea | id_aeropuerto | id_movimiento | dia |
|---|---|---|---|
| 1 | 1 | 1 | 2021-05-02 |
| 2 | 1 | 1 | 2021-05-02 |
| 3 | 2 | 2 | 2021-05-02 |
| 4 | 3 | 2 | 2021-05-02 |
| 1 | 3 | 2 | 2021-05-02 |
| 2 | 1 | 1 | 2021-05-02 |
| 2 | 3 | 1 | 2021-05-04 |
| 3 | 4 | 1 | 2021-05-04 |
| 3 | 4 | 1 | 2021-05-04 |

---

## Flights endpoints

| Requirement | Endpoint | Status |
|---|---|---|
| Airport with most movement during the year | `GET /api/flights/top-airport` | Completed |
| Airline with highest number of flights | `GET /api/flights/top-airline` | Completed |
| Day with highest number of flights | `GET /api/flights/busiest-day` | Completed |
| Airlines with more than 2 flights per day | `GET /api/flights/airlines-more-than-two-flights-per-day` | Completed |

Additional endpoints:

| Endpoint | Description |
|---|---|
| `GET /api/flights/airlines` | Returns airline catalog |
| `GET /api/flights/airports` | Returns airport catalog |
| `GET /api/flights/movements` | Returns movement catalog |
| `GET /api/flights/all` | Returns all flights with joined readable data |
| `GET /api/flights/summary` | Returns general database totals |
| `GET /api/flights/by-airline` | Groups flights by airline |
| `GET /api/flights/by-airport` | Groups movements by airport |
| `GET /api/flights/by-day` | Groups flights by day |

---

# 🖥️ Frontend

## Angular Dashboard

**EN 🇺🇸**  
The frontend was developed with Angular and consumes all backend services using `HttpClient`.

**ES 🇲🇽**  
El frontend fue desarrollado con Angular y consume todos los servicios del backend utilizando `HttpClient`.

---

## Frontend sections | Secciones del frontend

| Section | Description |
|---|---|
| Home | General project presentation, architecture, stack and module summary |
| StackOverflow API | Displays challenge questions, endpoints, answers and interpretation |
| Vuelos México SQL | Displays SQL questions, endpoints, answers, interpretation and data table |

---

## Frontend features

- Sidebar navigation.
- Responsive layout.
- Light mode and dark mode.
- Pink / purple editorial visual style.
- Cards for results.
- Tables for general data.
- Expandable question blocks.
- External links to StackOverflow questions.
- Button to refresh data.
- Button to open Swagger.
- Frontend events sent to backend logs.

---

# 🧾 Frontend to Backend Logs

An extra endpoint was implemented:

```txt
POST /api/logs/frontend-event
```

This endpoint receives user interactions from Angular and prints them in the backend console.

Examples of logged actions:

```txt
cargar_dashboard
dashboard_cargado
cambio_seccion
abrir_pregunta
cerrar_pregunta
abrir_link_externo
cambio_tema
```

Example log:

```txt
====================================================
FRONTEND EVENT - ANGULAR DASHBOARD
====================================================
Fecha backend: 2026-05-01 08:11:36
Fecha frontend: 2026-05-01T08:11:36.463Z
Acción: abrir_pregunta
Sección: stackoverflow
Detalle: El usuario abrió la pregunta stack-4
Metadata: {'questionId': 'stack-4', 'opened': True}
====================================================
```

This feature was added to demonstrate traceability between frontend interactions and backend logs.

---

# 🐳 Docker

## Dockerized backend

The backend is dockerized using:

```txt
backend/Dockerfile
docker-compose.yml
```

The backend runs inside Docker and exposes port:

```txt
8000
```

---

## Docker Compose

The Docker Compose configuration:

- Builds the backend image.
- Mounts the backend app folder.
- Mounts HTTPS certificates.
- Runs Uvicorn.
- Exposes the FastAPI app on port `8000`.

---

# 🔐 HTTPS with Self-Signed Certificate

## HTTPS implementation

**EN 🇺🇸**  
The backend supports HTTPS inside Docker using a local self-signed certificate.

**ES 🇲🇽**  
El backend soporta HTTPS dentro de Docker utilizando un certificado autofirmado local.

Certificates are generated locally in:

```txt
certs/
  localhost.crt
  localhost.key
```

> The `certs/` folder is intentionally ignored by Git for safety. Certificates should be generated locally before running HTTPS.

Docker Compose mounts the certificates into the container:

```yaml
volumes:
  - ./certs:/certs:ro
```

Uvicorn is executed with:

```bash
--ssl-keyfile /certs/localhost.key
--ssl-certfile /certs/localhost.crt
```

The HTTPS backend is available at:

```txt
https://localhost:8000
```

Swagger over HTTPS:

```txt
https://localhost:8000/docs
```

Example endpoint:

```txt
https://localhost:8000/api/stackoverflow/answered-summary
```

Response example:

```json
{"answered":28,"unanswered":2,"total":30}
```

> Note: Since the certificate is self-signed, the browser may show a security warning. This is expected in local development. The user must allow/continue to localhost manually.

---

# 📚 Swagger / OpenAPI

FastAPI automatically generates Swagger documentation.

Swagger URL:

```txt
https://localhost:8000/docs
```

OpenAPI schema:

```txt
https://localhost:8000/openapi.json
```

Implemented documentation includes:

- StackOverflow endpoints.
- Flights SQL endpoints.
- Frontend event logging endpoint.
- Root endpoint.

---

# 🧪 Unit Tests | Pruebas unitarias

Unit tests were implemented with:

```txt
pytest
FastAPI TestClient
```

The tests validate:

- Backend root endpoint.
- Main StackOverflow endpoints.
- Main SQL Flights endpoints.
- HTTP status code `200 OK`.
- Expected JSON response structure.

---

## Run tests

From the backend folder:

```bash
cd backend
pytest -v
```

Current result:

```txt
12 passed, 2 warnings
```

The warnings are related to FastAPI recommending lifespan handlers instead of `@app.on_event("startup")`. They do not break the application.

---

# 🚀 Installation | Instalación

## Prerequisites | Requisitos

Install:

- Python 3.11+
- Node.js
- Angular CLI
- Docker Desktop
- Git

---

## Clone repository

```bash
git clone https://github.com/Alucarduwu/DesTecFullStack.git
cd DesTecFullStack
```

---

# 🔐 Generate HTTPS certificates | Generar certificados HTTPS

Before running Docker with HTTPS, generate local certificates.

From the project root:

```bash
mkdir certs
docker run --rm -v ${PWD}/certs:/certs alpine/openssl req -x509 -newkey rsa:4096 -nodes -keyout /certs/localhost.key -out /certs/localhost.crt -days 365 -subj "/CN=localhost"
```

On Windows PowerShell, if `mkdir certs` already exists, just run:

```powershell
docker run --rm -v ${PWD}/certs:/certs alpine/openssl req -x509 -newkey rsa:4096 -nodes -keyout /certs/localhost.key -out /certs/localhost.crt -days 365 -subj "/CN=localhost"
```

Verify files:

```bash
ls certs
```

Expected:

```txt
localhost.crt
localhost.key
```

---

# ▶️ Running the Project | Ejecutar el proyecto

## 1. Run backend with Docker + HTTPS

From the project root:

```bash
docker compose down
docker compose up --build
```

Backend HTTPS:

```txt
https://localhost:8000
```

Swagger:

```txt
https://localhost:8000/docs
```

> The browser may show a certificate warning. Click Advanced and continue to localhost.

---

## 2. Run frontend

Open a second terminal:

```bash
cd frontend
npm install
ng serve --port 4200
```

Frontend URL:

```txt
http://localhost:4200
```

---

## 3. Test backend endpoints manually

Example:

```txt
https://localhost:8000/api/stackoverflow/answered-summary
```

Expected response:

```json
{
  "answered": 28,
  "unanswered": 2,
  "total": 30
}
```

---

## 4. Run unit tests

From the backend folder:

```bash
cd backend
pytest -v
```

Expected result:

```txt
12 passed
```

---

# 🧪 Main Endpoints

## StackOverflow

```txt
GET /api/stackoverflow/answered-summary
GET /api/stackoverflow/highest-reputation
GET /api/stackoverflow/lowest-views
GET /api/stackoverflow/oldest-newest
GET /api/stackoverflow/console-report
GET /api/stackoverflow/oldest
GET /api/stackoverflow/newest
```

## Flights

```txt
GET /api/flights/airlines
GET /api/flights/airports
GET /api/flights/movements
GET /api/flights/all
GET /api/flights/summary
GET /api/flights/by-airline
GET /api/flights/by-airport
GET /api/flights/by-day
GET /api/flights/top-airport
GET /api/flights/top-airline
GET /api/flights/busiest-day
GET /api/flights/airlines-more-than-two-flights-per-day
```

## Logs

```txt
POST /api/logs/frontend-event
```

---

# 📊 Status | Estado

| Area | Status |
|---|---|
| Backend REST API | Completed |
| StackOverflow API consumption | Completed |
| SQLite database | Completed |
| SQL queries | Completed |
| Angular frontend | Completed |
| Docker backend | Completed |
| Swagger/OpenAPI | Completed |
| Unit tests | Completed |
| HTTPS self-signed certificate | Completed |
| Frontend event logs | Completed |

---

# ✅ Optional Requirements | Requerimientos opcionales

| Optional requirement | Status |
|---|---|
| Unit tests | Implemented with pytest |
| Swagger or similar | Implemented with FastAPI Swagger |
| HTTPS server over Docker with self-signed certificate | Implemented with Uvicorn SSL and Docker certificates |

---

# 🧠 What I Learned | Qué aprendí

**EN 🇺🇸**

During this challenge, I reinforced several FullStack concepts:

- Building REST APIs with FastAPI.
- Consuming external APIs from the backend.
- Structuring SQL data and exposing it through endpoints.
- Using SQLite for lightweight relational data.
- Connecting Angular with FastAPI using HttpClient.
- Dockerizing a backend application.
- Running FastAPI inside Docker.
- Generating Swagger documentation automatically.
- Writing backend tests with pytest.
- Sending frontend interaction logs to the backend.
- Configuring HTTPS with a self-signed certificate inside Docker.

**ES 🇲🇽**

Durante este reto reforcé varios conceptos FullStack:

- Construcción de APIs REST con FastAPI.
- Consumo de APIs externas desde el backend.
- Estructuración de datos SQL y exposición mediante endpoints.
- Uso de SQLite para datos relacionales ligeros.
- Conexión de Angular con FastAPI usando HttpClient.
- Dockerización de una aplicación backend.
- Ejecución de FastAPI dentro de Docker.
- Generación automática de documentación Swagger.
- Creación de pruebas unitarias con pytest.
- Envío de logs de interacción desde Angular hacia el backend.
- Configuración de HTTPS con certificado autofirmado dentro de Docker.

---

# 🧩 Technical Challenges | Retos técnicos

**EN 🇺🇸**

The most challenging parts were:

1. **Docker and WSL setup on Windows**
   - Docker required WSL2 to run correctly.
   - The Docker daemon had to be running before containers could execute.

2. **Router prefixes in FastAPI**
   - Some endpoints initially returned duplicated paths such as:
     ```txt
     /api/stackoverflow/api/stackoverflow/...
     ```
   - This was solved by keeping the StackOverflow prefix inside its router and the Flights prefix in `main.py`.

3. **Frontend failing when one endpoint failed**
   - `forkJoin()` fails completely if one request fails.
   - This was solved by adding safe fallback handling with `catchError()`.

4. **HTTPS with self-signed certificate**
   - PowerShell did not recognize OpenSSL directly.
   - A Windows certificate was not enough because Docker needed physical `.crt` and `.key` files.
   - This was solved by generating certificates inside Docker using `alpine/openssl`.
   - Then Docker Compose mounted the certificate files into the backend container.

5. **Browser certificate warning**
   - Because the certificate is self-signed, Chrome shows a security warning.
   - This is expected in local environments and must be accepted manually.

6. **Unit tests configuration**
   - Pytest initially could not find the `app` module.
   - This was solved using `pytest.ini` and `__init__.py` files.

**ES 🇲🇽**

Las partes más retadoras fueron:

1. **Configuración de Docker y WSL en Windows**
   - Docker necesitaba WSL2 para funcionar correctamente.
   - También fue necesario asegurar que el Docker daemon estuviera corriendo.

2. **Prefijos de rutas en FastAPI**
   - Al inicio algunas rutas se duplicaban:
     ```txt
     /api/stackoverflow/api/stackoverflow/...
     ```
   - Se resolvió dejando el prefijo de StackOverflow dentro de su router y el prefijo de Flights desde `main.py`.

3. **Falla completa del frontend si un endpoint fallaba**
   - `forkJoin()` falla por completo si una sola petición falla.
   - Se solucionó agregando manejo seguro de errores con `catchError()`.

4. **HTTPS con certificado autofirmado**
   - PowerShell no reconocía OpenSSL directamente.
   - El certificado de Windows no era suficiente porque Docker necesitaba archivos físicos `.crt` y `.key`.
   - Se solucionó generando los certificados desde Docker con `alpine/openssl`.
   - Después se montaron los certificados dentro del contenedor mediante Docker Compose.

5. **Advertencia del navegador**
   - Al usar certificado autofirmado, Chrome muestra una advertencia de seguridad.
   - Esto es normal en entorno local y se debe aceptar manualmente.

6. **Configuración de pruebas unitarias**
   - Pytest inicialmente no encontraba el módulo `app`.
   - Se solucionó agregando `pytest.ini` y archivos `__init__.py`.

---

# 🔮 Future Improvements | Mejoras futuras

**EN 🇺🇸**

- Add more detailed unit tests with mocked StackExchange API responses.
- Add end-to-end tests for Angular.
- Add production-ready HTTPS with a trusted certificate.
- Add pagination and filters in the dashboard.
- Add charts for flights grouped by airline, airport and day.
- Improve accessibility and keyboard navigation.
- Add environment files for development and production API URLs.
- Add CI/CD pipeline to run tests automatically.

**ES 🇲🇽**

- Agregar pruebas unitarias más detalladas usando mocks para StackExchange API.
- Agregar pruebas end-to-end para Angular.
- Configurar HTTPS productivo con certificado confiable.
- Agregar paginación y filtros en el dashboard.
- Agregar gráficas para vuelos agrupados por aerolínea, aeropuerto y día.
- Mejorar accesibilidad y navegación por teclado.
- Agregar archivos de environment para URLs de desarrollo y producción.
- Agregar pipeline CI/CD para ejecutar pruebas automáticamente.

---

# 📝 Personal Comment | Comentario personal sobre el reto

**EN 🇺🇸**  
This challenge was a great opportunity to practice a complete FullStack workflow. I enjoyed building not only the required endpoints, but also a visual dashboard that makes the results easy to understand.

The HTTPS setup was the most difficult part because I had to understand the difference between a Windows certificate and the physical certificate files required by Docker. Solving that helped me better understand how local HTTPS works inside containers.

I also improved my understanding of FastAPI routing, Docker Compose, Angular HTTP services, unit testing and frontend-backend communication.

**ES 🇲🇽**  
Este reto fue una muy buena oportunidad para practicar un flujo FullStack completo. Me gustó construir no solo los endpoints solicitados, sino también un dashboard visual que permite entender fácilmente los resultados.

La parte más difícil fue configurar HTTPS, porque tuve que entender la diferencia entre un certificado creado en Windows y los archivos físicos que Docker necesita para poder ejecutar Uvicorn con SSL. Resolverlo me ayudó a comprender mejor cómo funciona HTTPS local dentro de contenedores.

También reforcé mis conocimientos sobre rutas en FastAPI, Docker Compose, servicios HTTP en Angular, pruebas unitarias y comunicación entre frontend y backend.

---

# ⚙️ SYSTEM DATA (DO NOT EDIT FORMAT)

<!-- Used for portfolio parsing -->

## PROJECT_DATA

name:
  en: Casa Mecate FullStack Technical Challenge
  es: Reto Técnico FullStack Casa Mecate

description:
  en: FullStack technical challenge built with FastAPI, Angular, SQLite, Docker, Swagger, unit tests and HTTPS with self-signed certificate.
  es: Reto técnico FullStack desarrollado con FastAPI, Angular, SQLite, Docker, Swagger, pruebas unitarias y HTTPS con certificado autofirmado.

problem:
  en: The challenge required a complete FullStack flow where SQL and external JSON data are processed by the backend and consumed by a frontend.
  es: El reto requería un flujo FullStack completo donde datos SQL y JSON externo fueran procesados por el backend y consumidos por un frontend.

solution:
  en: A FastAPI backend was built to consume StackOverflow API and SQLite data, exposing REST endpoints consumed by an Angular dashboard.
  es: Se construyó un backend con FastAPI para consumir StackOverflow API y datos SQLite, exponiendo endpoints REST consumidos por un dashboard en Angular.

stack:
  - Python
  - FastAPI
  - Angular
  - TypeScript
  - SQLite
  - Docker
  - Docker Compose
  - Swagger / OpenAPI
  - Pytest
  - HTTPS Self-Signed Certificate
  - SCSS

features:
  en:
    - REST API with FastAPI
    - External StackOverflow API consumption
    - SQLite database with seeded flight data
    - SQL query endpoints
    - Angular dashboard
    - Light and dark mode
    - Swagger documentation
    - Dockerized backend
    - HTTPS with self-signed certificate
    - Unit tests with pytest
    - Frontend event logs sent to backend
  es:
    - API REST con FastAPI
    - Consumo externo de StackOverflow API
    - Base de datos SQLite con datos de vuelos
    - Endpoints de consultas SQL
    - Dashboard en Angular
    - Modo claro y oscuro
    - Documentación Swagger
    - Backend dockerizado
    - HTTPS con certificado autofirmado
    - Pruebas unitarias con pytest
    - Logs de eventos del frontend enviados al backend

architecture: Layered FullStack architecture with SQL and external JSON processed by FastAPI and consumed by Angular.

technical_challenges:
  en:
    - Docker setup on Windows with WSL2
    - FastAPI router prefix duplication
    - Handling Angular forkJoin errors
    - HTTPS setup inside Docker
    - Generating physical certificate files for Docker
    - Configuring pytest module imports
  es:
    - Configuración de Docker en Windows con WSL2
    - Duplicación de prefijos en rutas de FastAPI
    - Manejo de errores en forkJoin de Angular
    - Configuración de HTTPS dentro de Docker
    - Generación de certificados físicos para Docker
    - Configuración de imports para pytest

improvements:
  en:
    - Added frontend event logging
    - Added HTTPS support
    - Added unit tests
    - Improved visual dashboard
    - Added dark mode
  es:
    - Se agregaron logs de eventos del frontend
    - Se agregó soporte HTTPS
    - Se agregaron pruebas unitarias
    - Se mejoró el dashboard visual
    - Se agregó modo oscuro

learning:
  en:
    - FastAPI REST architecture
    - Docker Compose configuration
    - Angular HTTP services
    - SQLite queries
    - HTTPS with self-signed certificates
    - Backend testing with pytest
  es:
    - Arquitectura REST con FastAPI
    - Configuración de Docker Compose
    - Servicios HTTP en Angular
    - Consultas SQLite
    - HTTPS con certificados autofirmados
    - Pruebas backend con pytest

status:
  en: Completed
  es: Completado

future:
  en:
    - Add mocked API tests
    - Add Angular E2E tests
    - Add charts and filters
    - Add CI/CD pipeline
    - Add production-ready HTTPS
  es:
    - Agregar pruebas con mocks
    - Agregar pruebas E2E en Angular
    - Agregar gráficas y filtros
    - Agregar pipeline CI/CD
    - Agregar HTTPS productivo

repo: https://github.com/Alucarduwu/DesTecFullStack
demo: Local environment

---

## 👩‍💻 Author

**Anahí Lozano**

- Portfolio: https://portafolioanahi.vercel.app/
- GitHub: https://github.com/Alucarduwu
- LinkedIn: https://www.linkedin.com/in/anahi-lozano-de-lira-a4213a187/
- Email: anahydlira@gmail.com

---

<p align="center">
💜 Built with FastAPI, Angular, Docker and a lot of debugging
</p>
