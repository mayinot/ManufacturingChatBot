# app/services/inventory_service.py
from database.models.quality_control import QualityControl
from app.utils.logging import get_logger
from sqlalchemy.orm import Session

logger = get_logger(__name__)

def get_all_qualities(db_session):
    logger.info("Fetching all qualities")
      # Query the database for all inventory items
    qualities = db_session.query(QualityControl).all()
    
    # Convert to a list of dicts (or use a schema for more structured responses)
    return qualities
