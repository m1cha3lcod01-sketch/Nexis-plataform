"""Ruta de bienvenida de NEXIS."""

from fastapi import APIRouter

router = APIRouter()


@router.get("/", tags=["inicio"])
def inicio() -> dict[str, str]:
    """Devuelve el mensaje de bienvenida de la API."""
    return {
        "proyecto": "NEXIS",
        "estado": "operativo",
        "mensaje": "Bienvenido a NEXIS API",
    }
