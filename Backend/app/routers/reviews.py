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
    new_review = Reviews(product_id=id, review=review, rating=rating)
    db.add(new_review)
    db.commit()
    db.refresh(new_review)
    return{"message": "Review added successfully", "review": new_review}

@router.delete("/reviews/{id}/reviews")
def delete_review(id:int, db:Session = Depends(get_db)):
    review_to_delete = db.query(Reviews).filter(Reviews.id == id).first()
    if review_to_delete:
        db.delete(review_to_delete)
        db.commit()
        return {"message": "Review deleted successfully"}
    return {"message": "Review not found"}