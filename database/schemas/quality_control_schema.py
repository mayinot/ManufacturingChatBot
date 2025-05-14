# database/schemas/quality_control_schema.py

from pydantic import BaseModel
from datetime import datetime

class QualityControlCreate(BaseModel):
    product_id: int
    inspector_name: str
    inspection_date: datetime = datetime.utcnow()
    remarks: str
    status: str
    severity: int
