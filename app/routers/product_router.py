# app/routers/inventory_router.py

from fastapi import APIRouter, Depends
from app.services.product_service import get_all_products
from app.utils import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/", summary="Get all products")
def list_product_items(db: Session = Depends(get_db)):
    return get_all_products(db)
