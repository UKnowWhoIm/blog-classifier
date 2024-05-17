from fastapi import FastAPI, Depends, BackgroundTasks
from contextlib import asynccontextmanager
from .controller import router
from .service import create_all_tables, get_db
from .models import Base

app = FastAPI()
app.include_router(router)

@asynccontextmanager
def startup(_):
  create_all_tables()


def create_all_tables():
  engine = next(get_db())
  Base.metadata.create_all(engine)
