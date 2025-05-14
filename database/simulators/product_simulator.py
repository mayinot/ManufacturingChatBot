from sqlalchemy.orm import Session
from ..models.product import Product
from ..schemas.product_schema import ProductCreate
import random
from faker import Faker

fake = Faker()

class ProductSimulator:
    @staticmethod
    def insert_products(session: Session) -> dict:
        """Insert synthetic product data into the database."""
        product_ids = {}
        product_names = ["eBike T101", "eBike T200", "Frame", "Battery", "Motor", "Wheel"]
        
        for name in product_names:
            product = ProductCreate(
                name=name,
                description=fake.text(max_nb_chars=50),
                cost=round(random.uniform(10, 500), 2)
            )
            
            db_product = Product(
                name=product.name,
                description=product.description,
                cost=product.cost
            )
            
            session.add(db_product)
            session.flush()
            product_ids[db_product.name] = db_product.id
        
        session.commit()
        return product_ids
