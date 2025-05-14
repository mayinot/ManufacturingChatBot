from sqlalchemy.orm import Session
from ..models.work_order import WorkOrder
from ..schemas.work_order_schema import WorkOrderCreate
import random
from datetime import datetime, timedelta

class WorkOrderSimulator:
    @staticmethod
    def insert_work_orders(session: Session, product_ids: dict, machine_ids: dict) -> dict:
        """Insert synthetic work order data into the database."""
        work_order_ids = {}
        
        for product_name, product_id in product_ids.items():
            for i in range(random.randint(1, 5)):
                machine_name, machine_id = random.choice(list(machine_ids.items()))
                
                work_order = WorkOrderCreate(
                    product_id=product_id,
                    machine_id=machine_id,
                    quantity=random.randint(10, 100)
                )
                
                db_work_order = WorkOrder(
                    product_id=work_order.product_id,
                    machine_id=work_order.machine_id,
                    quantity=work_order.quantity,
                    start_time=datetime.now() - timedelta(days=random.randint(1, 30)),
                    end_time=datetime.now(),
                    status=random.choice(["scheduled", "in_progress", "completed"])
                )
                
                session.add(db_work_order)
                session.flush()
                work_order_ids[db_work_order.id] = db_work_order.id
        
        session.commit()
        return work_order_ids
