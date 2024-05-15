from .errors import Errors

class Error:
  id: str
  type: Errors
  prompt: str
  response: str
