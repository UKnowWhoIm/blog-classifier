import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = f'postgresql://{os.environ['DB_USERNAME']}:{os.environ['DB_PASSWORD']}@{os.environ['DB_HOST']}'

Base = declarative_base()


def get_db():
  engine = create_engine(DATABASE_URL)
  session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
  db = session_local()
  try:
    yield db
  finally:
    db.close_all()
