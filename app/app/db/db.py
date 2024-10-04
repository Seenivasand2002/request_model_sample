from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker
from core import settings

Base = declarative_base()
engine = create_engine(settings.SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

