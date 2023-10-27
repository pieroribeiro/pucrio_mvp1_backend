from pydantic import BaseModel

class GenericMessageSchema(BaseModel):
    """
    Define representation of message.
    """
    mesage: str
