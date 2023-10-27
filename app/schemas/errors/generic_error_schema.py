from pydantic import BaseModel

class GenericErrorSchema(BaseModel):
    """
    Define representation of error message.
    """
    mesage: str
