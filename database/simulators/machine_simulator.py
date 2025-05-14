from sqlalchemy.orm import Session
from ..models.machine import Machine
from ..schemas.machine_schema import MachineCreate
import random
from faker import Faker

fake = Faker()

class MachineSimulator:
    @staticmethod
    def insert_machines(session: Session, work_center_ids: dict) -> dict:
        """Insert synthetic machine data into the database."""
        machine_ids = {}
        machine_types = ["Frame Welding", "Wheel Assembly", "Paint Booth", "Battery Assembly", "Motor Assembly"]
        
        for i, machine_type in enumerate(machine_types, start=1):
            for j in range(random.randint(1, 3)):
                machine = MachineCreate(
                    name=f"Machine-{machine_type[:3]}-{i}{j}",
                    type=machine_type,
                    status=random.choice(["running", "idle", "maintenance", "breakdown"]),
                    capacity=round(random.uniform(50, 200), 2)
                )
                
                db_machine = Machine(
                    name=machine.name,
                    type=machine.type,
                    status=machine.status,
                    capacity=machine.capacity
                )
                
                session.add(db_machine)
                session.flush()
                machine_ids[db_machine.name] = db_machine.id
        
        session.commit()
        return machine_ids
