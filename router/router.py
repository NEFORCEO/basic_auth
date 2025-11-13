from typing import Annotated

from fastapi import Depends, APIRouter, Response, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from sqlalchemy import select



from database.database.session import SessionDep
from database.models.register import Register
from schemas.schema import ResponseSchema


secret = HTTPBasic()
router = APIRouter(tags=["Пользователи"], prefix="/me")


@router.get('/basic-auth', response_model=ResponseSchema)
async def basic_auth_users(
    auth: Annotated[HTTPBasicCredentials, Depends(secret)],
    db: SessionDep
):
    user = await db.execute(select(Register).filter(Register.username == auth.username))
    result = user.scalar_one_or_none()
    if result:
        return  Response(status_code=status.HTTP_401_UNAUTHORIZED, content="User invalid")
    new_user = Register(username=auth.username, password=auth.password)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return {
        "status": 200,
        "username": new_user.username,
        "password": new_user.password
    }
    
@router.get('/basic_all')
async def all_users(db: SessionDep):
    users = await db.execute(select(Register))
    return users.scalars().all()


