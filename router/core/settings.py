from src.settings import Settings
import os

settings = Settings(
    PROJECT_NAME="Kroki Project",
    # Database settings
    POSTGRES_SERVER=os.getenv("POSTGRES_SERVER"),
    POSTGRES_DB=os.getenv("POSTGRES_DB"),
    POSTGRES_USER=os.getenv("POSTGRES_USER"),
    POSTGRES_PASSWORD=os.getenv("POSTGRES_PASSWORD"),
    # Server settings
    SERVER_NAME="Kroki Server",
    SERVER_HOST="http://0.0.0.0:8000/",
    SENTRY_DSN="http://0.0.0.0:8000/"
)