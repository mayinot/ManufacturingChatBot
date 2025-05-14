# app/services/inventory_service.py
from database.models.product import Product
from app.utils.logging import get_logger
from sqlalchemy.orm import Session

logger = get_logger(__name__)

def get_all_products(db_session):
    logger.info("Fetching all products")
      # Query the database for all inventory items
    products = db_session.query(Product).all()
    
    # Convert to a list of dicts (or use a schema for more structured responses)
    return products
