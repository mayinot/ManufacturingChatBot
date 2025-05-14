# database/seed.py

from .connection import SessionLocal
from .simulators.machine_simulator import MachineSimulator
from .simulators.product_simulator import ProductSimulator
from .simulators.inventory_simulator import InventorySimulator
from .simulators.work_order_simulator import WorkOrderSimulator
from .simulators.quality_control_simulator import QualityControlSimulator

def seed_data():
    """Seed the database with initial data."""
    session = SessionLocal()

    try:
        # Insert synthetic data
        machine_ids = MachineSimulator.insert_machines(session, {})
        product_ids = ProductSimulator.insert_products(session)
        inventory_ids = InventorySimulator.insert_inventory(session)
        work_order_ids = WorkOrderSimulator.insert_work_orders(session, product_ids, machine_ids)
        QualityControlSimulator.insert_quality_controls(session, list(work_order_ids.values()))

        print("Database seeding completed successfully.")
    finally:
        session.close()

if __name__ == "__main__":
    seed_data()
