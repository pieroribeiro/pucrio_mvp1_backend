from pydantic import BaseModel

class GenericErrorSchema(BaseModel):
    """
    Define representation of error message.
    """
    message: str
