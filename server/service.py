import os
from re import findall
from requests import post, Response
from .datamodels import CreatePostDto
from .errors import Errors

def process_model_response(prompt: str, res: Response):
  error_type: Errors | None
  if res.status_code >= 500 or 300 <= res.status_code < 400:
    error_type = Errors.MODEL_SERVER_ERROR
  elif res.status_code >= 400:
    error_type = Errors.BAD_MODEL_REQUEST
  if not error_type:
    res_json: dict = res.json()
    if 'response' in res_json.keys():
      category = findall(r'Category: ([a-zA-z\w]+)', res_json['response'])
    else:
      error_type = Errors.BAD_MODEL_RESPONSE
  if error_type:
    # TODO report error
    print(error_type)
  else:
    # TODO update category
    print('updated category')

def get_tag(postData: CreatePostDto):
  url = f'{os.environ['MODEL_HOST']}/api/generate'
  prompt = f'{postData.headline}\n\{postData.body}'
  systemPrompt = ''
  data = {
    'model': os.environ['MODEL_NAME'],
    'system': systemPrompt,
    'prompt': prompt,
    'stream': False,
  }
  res = post(url, json=data)
  process_model_response(prompt, res)
