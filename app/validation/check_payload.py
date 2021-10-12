from pydantic import BaseModel

class Check(BaseModel):
    id: int
    name: str
    