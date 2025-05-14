# database/simulators/quality_control_simulator.py

from sqlalchemy.orm import Session
from ..models.quality_control import QualityControl
from faker import Faker
import random

fake = Faker()

class QualityControlSimulator:
    @staticmethod
    def insert_quality_controls(session: Session, work_order_ids: list) -> dict:
        """Insert synthetic quality control data into the database."""
        qc_ids = {}
        results = ["Passed", "Failed", "Rework Needed", "Minor Defect", "Critical Defect"]

        for work_order_id in work_order_ids:
            qc_entry = QualityControl(
                work_order_id=work_order_id,
                inspector_name=fake.name(),
                result=random.choice(results),
                defect_rate=round(random.uniform(0, 5), 2),
                remarks=fake.text(max_nb_chars=200)
            )

            session.add(qc_entry)
            session.flush()
            qc_ids[qc_entry.id] = qc_entry.work_order_id

        session.commit()
        return qc_ids
