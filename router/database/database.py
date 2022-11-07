import databases
from sqlalchemy import create_engine
from core.settings import settings

# Init database for our models
database = databases.Database(settings.SQLALCHEMY_DATABASE_URI)
# Create SQLAlchemy engine for database
engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, echo=True)