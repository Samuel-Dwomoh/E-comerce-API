from fastapi import APIRouter, Depends
from database import get_db
from schemas.schemas import Products
from sqlalchemy.orm import Session
from models import ProductModel

router = APIRouter( tags=["product"])

@router.get("/products")
def get_products(db:Session = Depends(get_db)):
    products = db.query(Products).all()
    return products

@router.get("/products/{product_id}")
def get_product(product_id:int, db:Session = Depends(get_db)):
    product = db.query(Products).filter(Products.id == product_id).first()
    return product

@router.post("/products")
def create_product(product:ProductModel, db:Session = Depends(get_db)):
    new_product = Products(name=product.name, description=product.description, price=product.price, quantity=product.quantity)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product
