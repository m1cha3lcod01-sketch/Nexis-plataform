from fastapi import FastAPI

app = FastAPI(
    title="NEXIS API",
    description="API central de NEXIS",
    version="1.0.0",
)


@app.get("/")
def inicio():
    return {
        "proyecto": "NEXIS",
        "estado": "operativo",
        "mensaje": "Bienvenido a NEXIS API",
    }


@app.get("/health")
def health():
    return {
        "status": "ok",
        "mensaje": "NEXIS está funcionando correctamente",
    }
