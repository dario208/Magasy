from sqlmodel import SQLModel, create_engine, Session
from core.config import DATABASE_URL
import psycopg2
from typing import Annotated
from fastapi import Depends
engine = create_engine(DATABASE_URL)

def init_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
SessionDep = Annotated[Session, Depends(get_session)]

