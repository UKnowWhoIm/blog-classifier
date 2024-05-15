from enum import Enum

class Errors(Enum):
  MODEL_SERVER_ERROR = 1
  BAD_MODEL_REQUEST = 2
  BAD_MODEL_RESPONSE = 3
  CATEGORY_NOT_FOUND = 4