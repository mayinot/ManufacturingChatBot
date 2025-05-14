# app/services/inventory_service.py
from database.models.work_order import WorkOrder
from app.utils.logging import get_logger
from sqlalchemy.orm import Session

logger = get_logger(__name__)

def get_all_work_orders(db_session):
    logger.info("Fetching all qualities")
      # Query the database for all inventory items
    work_orders = db_session.query(WorkOrder).all()
    
    # Convert to a list of dicts (or use a schema for more structured responses)
    return work_orders
