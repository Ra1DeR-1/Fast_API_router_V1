from sqlalchemy.orm import declarative_base
from sqlalchemy import Column
from sqlalchemy import Integer, String

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(32))
    password = Column(String(255))