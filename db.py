from sqlalchemy.orm import registry, relationship, sessionmaker
# from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Boolean, create_engine, ForeignKey

SQLALCHEMY_DATABASE_URL = 'mysql+mysqlconnector://web:230mod@localhost:3306/quiz'
engine = create_engine(
   SQLALCHEMY_DATABASE_URL, echo=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# mapper_registry = registry()

Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        