from pydantic import BaseModel

class WorkOrderCreate(BaseModel):
    product_id: int
    machine_id: int
    quantity: int

class WorkOrderUpdate(BaseModel):
    status: str
