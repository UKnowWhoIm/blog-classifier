from sqlalchemy import String, Text, UUID, SMALLINT, BIGINT, ForeignKey, INT
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .db import Base

class Post(Base):
  __tablename__ = 'posts'
  
  id: Mapped[str] = mapped_column(UUID, primary_key=True, server_default='uuid_generate_v4()')
  headline: Mapped[str] = mapped_column(String(100), nullable=False)
  body: Mapped[str] = mapped_column(String(2048), nullable=False)
  category: Mapped[str] = mapped_column(String(30), nullable=True)

  model_responses = relationship('ModelResponse', back_populates='post')


class ModelResponse(Base):
  __tablename__ = 'model_responses'

  id: Mapped[str] = mapped_column(UUID, primary_key=True, server_default='uuid_generate_v4()')
  error: Mapped[int] = mapped_column(SMALLINT, nullable=True)
  model: Mapped[str] = mapped_column(String(30), nullable=True)
  category: Mapped[str]= mapped_column(String(30), nullable=True)
  prompt: Mapped[str] = mapped_column(Text, nullable=False)
  system_prompt: Mapped[str] = mapped_column(Text, nullable=False)
  response: Mapped[str] = mapped_column(Text, nullable=False)
  total_duration: Mapped[BIGINT] = mapped_column(BIGINT, nullable=True)
  iteration: Mapped[int] = mapped_column(INT, nullable=True)
  post_id: Mapped[str] = mapped_column(ForeignKey('posts.id'))

  post: Mapped[Post] = relationship("Post", back_populates="model_responses")
