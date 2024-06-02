from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.orm import DeclarativeBase

DB_URI = "sqlite:///todo.db"
engine = create_engine(DB_URI, connect_args={"check_same_thread": False})
SessionLocal: Session = sessionmaker(bind=engine, autocommit=False, autoflush=False)

class Base(DeclarativeBase):
    ...

def create_db():
    import models
    Base.metadata.create_all(bind=engine)
