from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from uvicorn import run

from core import lifespan, settings
from api import router as api_router

app = FastAPI(default_response_class=ORJSONResponse, lifespan=lifespan)
app.include_router(api_router)

if __name__ == "__main__":
    run(
        app=settings.run.app,
        host=settings.run.host,
        port=settings.run.port,
        reload=settings.run.reload,
    )
