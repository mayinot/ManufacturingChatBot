from pydantic import BaseModel

class InventoryCreate(BaseModel):
    item_name: str
    quantity: int
    unit_cost: float

class InventoryUpdate(BaseModel):
    quantity: int
    unit_cost: float
