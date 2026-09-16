from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.schemas import Reviews
from database import get_db
router = APIRouter(prefix="/reviews", tags=["reviews"])

@router.get("/reviews/{id}/reviews")
def get_reviews(id:int, db:Session = Depends(get_db)):
    get_review = db.query(Reviews).filter(Reviews.product_id == id).all()
    return get_review

@router.post("/reviews/{id}/reviews")
def add_review(id:int, review:str, rating:int, db:Session = Depends(get_db)):
    pass)