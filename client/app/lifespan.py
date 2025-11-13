from contextlib import asynccontextmanager
from typing import Any

from fastapi import FastAPI
from loger.logging import logger
from database.database.session import init_db

@asynccontextmanager
async def start_app(app: FastAPI) -> Any:
    logger.info("App started")
    await init_db()
    yield
    logger.info("App close")