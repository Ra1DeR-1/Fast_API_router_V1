from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from core.settings import settings
from database.database import database, engine
from database.models import Base
from router import api_router

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

# Include general API router
app.include_router(api_router, prefix=settings.API_V1_STR)
# Put our database instance into FastAPI instance's state
app.state.database = database


@app.on_event('startup')
async def connect_to_database() -> None:
    """
    Connect to database with app startup
    :return
    """
    database_ = app.state.database
    if not database_.is_connected:
        await database_.connect()
        Base.metadata.create_all(engine)


@app.on_event('shutdown')
async def disconnect_from_database() -> None:
    """
    Disconnect from database with app shutdown
    :return:
    """
    database_ = app.state.database
    if database_.is_connected:
        await database_.disconnect()