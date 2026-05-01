from datetime import datetime

from fastapi import FastAPI, Request, Body
from fastapi.middleware.cors import CORSMiddleware

from app.routes.stackoverflow import router as stackoverflow_router
from app.routes.flights import router as flights_router
from app.database import initialize_database
from app.seed import seed_database

app = FastAPI(
    title="Reto Técnico FullStack - Casa Mecate",
    description="API REST para consumir datos de StackOverflow y vuelos en México.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:4200",
        "http://localhost:4300",
        "http://localhost:47128",
        "http://127.0.0.1:4200",
        "http://127.0.0.1:4300",
        "http://127.0.0.1:47128",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def log_backend_requests(request: Request, call_next):
    """
    Log general de cada petición que llega al backend.
    Sirve para ver en Docker cuándo Angular consume endpoints.
    """
    start_time = datetime.now()

    response = await call_next(request)

    duration = (datetime.now() - start_time).total_seconds() * 1000

    print(
        f"[BACKEND REQUEST] "
        f"{request.method} {request.url.path} "
        f"-> {response.status_code} "
        f"({duration:.2f} ms)"
    )

    return response


@app.post("/api/logs/frontend-event")
def frontend_event_log(payload: dict = Body(...)):
    """
    Endpoint para recibir eventos desde Angular.
    Aquí se imprimen acciones como cambio de sección,
    modo oscuro, apertura de preguntas y links externos.
    """
    print("\n")
    print("====================================================")
    print("FRONTEND EVENT - ANGULAR DASHBOARD")
    print("====================================================")
    print(f"Fecha backend: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Fecha frontend: {payload.get('timestamp')}")
    print(f"Acción: {payload.get('action')}")
    print(f"Sección: {payload.get('section')}")
    print(f"Detalle: {payload.get('detail')}")
    print(f"Metadata: {payload.get('metadata')}")
    print("====================================================")
    print("\n")

    return {
        "message": "Evento de frontend registrado en consola",
        "received": True
    }


app.include_router(stackoverflow_router)


app.include_router(
    flights_router,
    prefix="/api/flights",
    tags=["Flights"]
)


@app.on_event("startup")
def startup_event():
    initialize_database()
    seed_database()


@app.get("/")
def root():
    return {
        "message": "Backend funcionando correctamente",
        "docs": "/docs",
        "swagger": "http://localhost:8000/docs",
        "status": "running"
    }