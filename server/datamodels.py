from pydantic import BaseModel, Field

class CreatePostDto(BaseModel):
  headline: str = Field(None, max_length=50)
  body: str = Field(None, max_length=280)

class GetPostDto(CreatePostDto):
  id: str
  category: str
