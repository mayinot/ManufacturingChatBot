# database/init_db.py

from .connection import engine, Base
from .models.inventory import Inventory
from .models.machine import Machine
from .models.product import Product
from .models.quality_control import QualityControl
from .models.work_order import WorkOrder

def init_db():
    print("Creating tables...")
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully.")

if __name__ == "__main__":
    init_db()
