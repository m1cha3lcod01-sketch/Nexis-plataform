"""Comprobación básica de estado de la API."""

from fastapi import APIRouter

router = APIRouter()


@router.get("/health", tags=["salud"])
def health() -> dict[str, str]:
    """Indica que el proceso de la API responde."""
    return {
        "status": "ok",
        "mensaje": "NEXIS está funcionando correctamente",
    }
