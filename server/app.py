from typing import List
from fastapi import FastAPI
from .datamodels import CreatePostDto, GetPostDto

app = FastAPI()

@app.get('/')
def hello():
  return {
    'name': 'Just Another Blog API',
    'version': '1.0'
  }

@app.post('/post')
def create_post(data: CreatePostDto) -> GetPostDto:
  raise NotImplemented()
  
@app.get('/posts')
def get_posts() -> List[GetPostDto]:
  raise NotImplemented()
