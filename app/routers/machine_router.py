# app/routers/inventory_router.py

from fastapi import APIRouter, Depends
from app.services.machine_service import get_all_machines
from app.utils import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/", summary="Get all machines")
def list_machines(db: Session = Depends(get_db)):
    return get_all_machines(db)
