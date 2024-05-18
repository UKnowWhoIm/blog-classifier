from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .datamodels import CreatePostDto, GetPostDto, ModelResponseFromDB
from .service import get_category, get_posts, create_post, get_post_by_id, update_category, get_all_model_responses
from .db import get_db
router = APIRouter()


@router.get('/')
def hello():
  return {
    'name': 'Just Another Blog API',
    'version': '1.0.2'
  }

@router.post('/post')
def create_post_api(data: CreatePostDto, database: Session = Depends(get_db)) -> GetPostDto:
  return create_post(data, database)
  
@router.get('/posts')
def get_posts_api(database: Session = Depends(get_db)) -> List[GetPostDto]:
  return get_posts(database)

@router.get('/posts/{post_id}')
def get_one_post_api(post_id: str, database: Session = Depends(get_db)) -> GetPostDto:
  post = get_post_by_id(post_id, database)
  if post is None:
    raise HTTPException(status_code=404)
  return post

@router.post('/posts/{post_id}/generate-category')
def generate_category_api(post_id: str, database: Session = Depends(get_db)) -> ModelResponseFromDB:
  post = get_post_by_id(post_id, database)
  if post is None:
    raise HTTPException(status_code=404)
  resp = get_category(post, database)
  if not resp.error:
    update_category(post, resp.category, database)
  return resp

@router.get('/model-responses')
def get_all_model_responses_api(database: Session = Depends(get_db)):
  return get_all_model_responses(database)
