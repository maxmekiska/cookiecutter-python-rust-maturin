from pydantic import BaseModel

class SumRequest(BaseModel):
    a: int
    b: int

class DiffRequest(BaseModel):
    a: int
    b: int