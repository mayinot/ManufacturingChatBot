from pydantic import BaseModel

class MachineCreate(BaseModel):
    name: str
    type: str
    status: str
    capacity: float

class MachineUpdate(BaseModel):
    status: str
    capacity: float
