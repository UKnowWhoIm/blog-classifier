from sqlalchemy import String, Text, UUID, SMALLINT, JSON, BIGINT
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .db import Base
from .errors import Errors

class Post(Base):
  id: Mapped[str] = mapped_column(UUID, primary_key=True, server_default='uuid_generate_v4()')
  headline: Mapped[str] = mapped_column(String(100), nullable=False)
  body: Mapped[str] = mapped_column(String(2048), nullable=False)
  category: Mapped[str] = mapped_column(String(30), nullable=True)


class ModelResponse(Base):
  __tablename__ = 'model_responses'

  id: Mapped[str] = mapped_column(UUID, primary_key=True, server_default='uuid_generate_v4()')
  error: Mapped[Errors] = mapped_column(SMALLINT, nullable=True)
  model: Mapped[str] = mapped_column(String(30), nullable=True)
  category: Mapped[str]= mapped_column(String(30), nullable=True)
  prompt: Mapped[str] = mapped_column(Text, nullable=False)
  response: Mapped[str] = mapped_column(Text, nullable=False)
  eval_time: Mapped[BIGINT] = mapped_column(BIGINT, nullable=True)
  post_id: Mapped[str] = mapped_column(UUID, nullable=True)
  
  post: Mapped[Post] = relationship()
