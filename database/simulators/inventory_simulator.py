# database/simulators/inventory_simulator.py

from sqlalchemy.orm import Session
from ..models.inventory import Inventory
from ..schemas.inventory_schema import InventoryCreate
import random

class InventorySimulator:
    @staticmethod
    def insert_inventory(session: Session) -> dict:
        """Insert synthetic inventory data into the database."""
        inventory_ids = {}
        inventory_names = ["Steel Bolts", "Rubber Grips", "Aluminum Tubing", "Control Circuits", "Battery Cells"]
        
        for name in inventory_names:
            # Use the schema to create the inventory item
            inventory = InventoryCreate(
                item_name=name,
                quantity=random.randint(100, 1000),
                unit_cost=round(random.uniform(0.5, 5.0), 2)
            )
            
            # Insert into the database
            db_inventory = Inventory(
                item_name=inventory.item_name,
                quantity=inventory.quantity,
                unit_cost=inventory.unit_cost
            )
            
            session.add(db_inventory)
            session.flush()
            inventory_ids[db_inventory.item_name] = db_inventory.id
        
        session.commit()
        return inventory_ids
