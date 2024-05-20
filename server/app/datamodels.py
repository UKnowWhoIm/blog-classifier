from typing import Optional
from pydantic import BaseModel, Field
from uuid import UUID

class CreatePostDto(BaseModel):
  headline: str = Field(None, max_length=100)
  body: str = Field(None, max_length=2048)

class GetPostDto(CreatePostDto):
  id: UUID
  category: str | None

  class Config:
    from_attributes = True
  
class GenerateCategoryBody(BaseModel):
  iteration: Optional[int] = None

class ModelResponseBase(BaseModel):
  response: str | None
  model: str
  total_duration: int | None

  class Config:
    from_attributes = True

class ModelResponseFromDB(ModelResponseBase):
  id: UUID
  iteration: Optional[int]
  error: int | None
  category: str | None
  
  post: GetPostDto

  class Config:
    from_attributes = True
