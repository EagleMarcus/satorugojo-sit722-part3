from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DATABASE_URL = "postgresql://dbassignment7_2_user:UchKrHNotpXwhuKVF5wHs611MDq14aVk@dpg-crcukl3v2p9s73cnbbs0-a.oregon-postgres.render.com/dbassignment7_2" #os.getenv("DATABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
