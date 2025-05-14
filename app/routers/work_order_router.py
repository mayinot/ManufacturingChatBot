# app/routers/inventory_router.py

from fastapi import APIRouter, Depends
from app.services.work_order_service import get_all_work_orders
from app.utils import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/", summary="Get all work orders")
def list_product_qualities(db: Session = Depends(get_db)):
    return get_all_work_orders(db)
