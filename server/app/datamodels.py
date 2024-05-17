from pydantic import BaseModel, Field
from uuid import UUID

class CreatePostDto(BaseModel):
  headline: str = Field(None, max_length=100)
  body: str = Field(None, max_length=2048)

class GetPostDto(CreatePostDto):
  id: UUID
  category: str | None

  class Config:
    orm_mode = True

class ModelResponseBase(BaseModel):
  response: str | None
  model: str
  total_duration: int

  class Config:
    orm_mode = True

class ModelResponseFromDB(ModelResponseBase):
  id: UUID
  error: str | None
  category: str | None

  class Config:
    orm_mode = True