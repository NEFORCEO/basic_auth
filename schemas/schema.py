from pydantic import BaseModel

class ResponseSchema(BaseModel):
    status: int 
    username: str 
    password: str 