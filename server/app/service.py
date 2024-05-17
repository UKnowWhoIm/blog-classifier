import os
from re import findall
from requests import post, Response
from sqlalchemy.orm import Session
from .datamodels import GetPostDto, CreatePostDto, ModelResponseBase
from .errors import Errors
from . import models

WORD_LIMIT = 200

def process_model_response(res: Response):
  error_type: Errors | None = None

  if res.status_code >= 500 or 300 <= res.status_code < 400:
    error_type = Errors.MODEL_SERVER_ERROR

  elif res.status_code >= 400:
    error_type = Errors.BAD_MODEL_REQUEST

  if not error_type:
    result = ModelResponseBase(**res.json())
    category = findall(r'Category: ([a-zA-Z]+)', result.response)

    if len(category) > 0:
      return [True, { 'category': category[0], **result.model_dump() }]

    return [False, {'error': Errors.BAD_MODEL_RESPONSE_TEXT, **result.model_dump() }]

  return [False, {'error': error_type }]

def _send_model_req(text: str, system: str | None = None):
  url = f'{os.environ['MODEL_HOST']}/api/generate'
  data = {
    'stream': False,
    'model': os.environ['MODEL_NAME'],
    'prompt': text
  }
  if system:
    data['system'] = system
  return post(url, json=data)

def word_count(text: str):
  return len(text.split(' '))

def shorten(text: str):
  return " ".join(text.split()[:WORD_LIMIT])

def create_post(postData: CreatePostDto, conn: Session):
  db_post = models.Post(**postData.model_dump())
  conn.add(db_post)
  conn.commit()
  conn.refresh(db_post)
  return db_post

def get_posts(conn: Session):
  return conn.query(models.Post).all()

def get_post_by_id(id: str, conn: Session):
  return conn.query(models.Post).get(id)

def get_all_model_responses(conn: Session):
  return conn.query(models.ModelResponse).all()

def update_category(post: models.Post, category: str, conn: Session):
  post.category = category
  conn.commit()

def get_category(postData: GetPostDto, conn: Session):
  prompt = f'blog excerpt: \n{shorten(f'{postData.headline}\n{postData.body}')}'
  system_prompt = '''You will be provided with a blog excerpt. You must categorize that excerpt into one of the given categories.
  The categories are "Economics", "Entertainment", "Food", "Health", "Travel", "Technology", "Politics".
  You must only reply with the categories. Here is an example of a prompt and appropriate response:
  Prompt: "First Look at Liam Hemsworth as Geralt in The Witcher Season 4"
  Response: "Category: Entertainment"
  Strictly follow the response format, do not give explanation or justification for your answer
  '''
  res = _send_model_req(prompt, system_prompt)
  [is_success, result] = process_model_response(res)
  model_response = {
    **result,
    'prompt': prompt,
    'system_prompt': system_prompt,
    'post_id': postData.id,
    'model': os.environ['MODEL_NAME']
  }
  if not is_success:
    model_response['response'] = res.text
  db_obj = models.ModelResponse(**model_response)
  conn.add(db_obj)
  conn.commit()
  conn.refresh(db_obj)
  return db_obj
