from sqlalchemy import Column, Integer, String, Float, Boolean
from ..connection import Base

class Machine(Base):
    __tablename__ = "machines"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    type = Column(String)
    status = Column(String)
    capacity = Column(Float)
    is_active = Column(Boolean, default=True)
