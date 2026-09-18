from fastapi import APIRouter, Depends
from database import get_db
from sqlalchemy.orm import Session
from schemas.schemas import Cart

router = APIRouter(tags=["cart"])

@router.get("/cart")
def get_cart(db: Session = Depends(get_db)):
    cart_items = db.query(Cart).all()
    return cart_items

@router.post("/cart/items")
def add_cart_item(user_id:int, product_id:int, quantity:int, db:Session = Depends(get_db)):
    cart_item = Cart(user_id=user_id, product_id=product_id, quantity=quantity)
    db.add(cart_item)
    db.commit()
    db.refresh(cart_item)
    return cart_item

@router.patch("/cart/items/{product_id}")
def update_cart_item(product_id:int, quantity:int, db:Session = Depends(get_db)):
    db.query(Cart).filter(Cart.product_id == product_id).update({"quantity": quantity})
    db.commit()
    return {"product_id": product_id, "quantity": quantity}

