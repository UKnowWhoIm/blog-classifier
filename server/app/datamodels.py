from pydantic import BaseModel, Field

class CreatePostDto(BaseModel):
  headline: str = Field(None, max_length=100)
  body: str = Field(None, max_length=2048)

class GetPostDto(CreatePostDto):
  id: str
  category: str

  class Config:
    orm_mode = True

class ModelResponseBase(BaseModel):
  response: str
  model: str
  total_duration: str
  
  class Config:
    orm_mode = True

class ModelResponseFromDB(ModelResponseBase):
  id: str
  error: str
  eval_time: str
  
  class Config:
    orm_mode = True
