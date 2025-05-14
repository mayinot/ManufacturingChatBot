# database/models/quality_control.py

from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from ..connection import Base
from datetime import datetime

class QualityControl(Base):
    __tablename__ = "quality_control"

    id = Column(Integer, primary_key=True, index=True)
    work_order_id = Column(Integer, ForeignKey("work_orders.id"), nullable=False)
    inspector_name = Column(String, nullable=False)
    result = Column(String, nullable=False)  # e.g., "Passed", "Failed"
    defect_rate = Column(Float, nullable=False)  # Percentage of defects
    remarks = Column(Text, nullable=True)
    inspection_date = Column(DateTime, default=datetime.utcnow)

    # Optional relationship for better ORM usage
    work_order = relationship("WorkOrder", back_populates="quality_controls")
