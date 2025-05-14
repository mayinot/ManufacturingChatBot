# app/services/inventory_service.py
from database.models.inventory import Inventory
from app.utils.logging import get_logger
from sqlalchemy.orm import Session
logger = get_logger(__name__)

def get_all_inventory_items(db_session):
    logger.info("Fetching all inventory items")
      # Query the database for all inventory items
    inventory_items = db_session.query(Inventory).all()
    
    # Convert to a list of dicts (or use a schema for more structured responses)
    return inventory_items
