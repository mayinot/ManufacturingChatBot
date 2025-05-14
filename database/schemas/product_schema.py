from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    description: str
    cost: float

class ProductUpdate(BaseModel):
    description: str
    cost: float
