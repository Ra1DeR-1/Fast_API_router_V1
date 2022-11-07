from fastapi import APIRouter

from api.auth import auth_router

api_router = APIRouter()

api_router.include_router(auth_router, prefix='/auth', tags=["auth"])