# app/routers/inventory_router.py

from fastapi import APIRouter, Depends
from app.services.inventory_service import get_all_inventory_items
from app.utils import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/", summary="Get all inventory items")
def list_inventory_items(db: Session = Depends(get_db)):
    return get_all_inventory_items(db)
