# app/services/inventory_service.py
from database.models.machine import Machine
from app.utils.logging import get_logger
from sqlalchemy.orm import Session

logger = get_logger(__name__)

def get_all_machines(db_session):
    logger.info("Fetching all machines")
      # Query the database for all inventory items
    machines = db_session.query(Machine).all()
    
    # Convert to a list of dicts (or use a schema for more structured responses)
    return machines
