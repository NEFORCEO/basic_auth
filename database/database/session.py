from typing import Annotated

from fastapi import Depends
from database.database.db import engine, async_session, Base, AsyncSession

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        
async def get_sess():
    async with async_session() as session:
        yield session
        
SessionDep = Annotated[AsyncSession, Depends(get_sess)]