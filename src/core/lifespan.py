from fastapi import FastAPI
from contextlib import asynccontextmanager

from core import db_helper


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await db_helper.dispose()
