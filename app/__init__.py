# app/__init__.py

from fastapi import FastAPI
from .routers import (
    inventory_router,
    machine_router,
    product_router,
    quality_router,
    work_order_router, 
    chat_router
)
from .utils.logging import setup_logging

app = FastAPI(
    title="Manufacturing ChatBot API",
    version="0.1.0",
    description="API for managing manufacturing processes"
)

# Initialize logging
setup_logging()

# Register routers
app.include_router(inventory_router, prefix="/inventory", tags=["Inventory"])
app.include_router(machine_router, prefix="/machines", tags=["Machines"])
app.include_router(product_router, prefix="/products", tags=["Products"])
app.include_router(quality_router, prefix="/quality", tags=["Quality Control"])
app.include_router(work_order_router, prefix="/work_orders", tags=["Work Orders"])
app.include_router(chat_router, prefix="/chat", tags=["Chat"])

# Add a root endpoint
@app.get("/", tags=["Root"])
async def root():
    return {"message": "Manufacturing ChatBot API is running"}
