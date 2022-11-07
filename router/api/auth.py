from fastapi import APIRouter
from sqlalchemy import select
from database.models import User
from database.database import engine

auth_router = APIRouter()


@auth_router.get("/status")
async def login() -> dict:
    """
    Simple function
    :return:
    """
    return {"status": "ok"}


@auth_router.get("/all")
async def getAllUsers():
    query = select(User)
    connection = engine.connect()
    result = connection.execute(query).fetchall()
    return {"result": result}