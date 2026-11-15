# Backend inicial de NEXIS

API inicial de NEXIS construida con Python y FastAPI. Incluye los endpoints `GET /` y `GET /health`.

## Requisitos

- Python 3.10 o posterior
- Una terminal abierta en esta carpeta (`backend`)

## Crear el entorno virtual

Desde la carpeta `backend`, ejecuta:

```bash
python3 -m venv .venv
```

En Windows, si `python3` no está disponible, usa `python -m venv .venv`.

## Activar el entorno virtual

En Linux o macOS:

```bash
source .venv/bin/activate
```

En Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

## Instalar dependencias

Con el entorno virtual activo y aún desde la carpeta `backend`:

```bash
python -m pip install -r requirements.txt
```

## Ejecutar la API

Desde la carpeta `backend`, con el entorno virtual activo:

```bash
python -m uvicorn app.main:app --reload
```

Uvicorn mostrará la dirección local, normalmente `http://127.0.0.1:8000`. Puedes abrir estas rutas en el navegador:

- `http://127.0.0.1:8000/` — bienvenida de NEXIS.
- `http://127.0.0.1:8000/health` — estado del servicio.
- `http://127.0.0.1:8000/docs` — documentación interactiva de FastAPI.

Para detener el servidor, presiona `Ctrl+C` en la terminal.
