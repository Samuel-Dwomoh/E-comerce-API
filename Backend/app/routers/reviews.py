from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
router = APIRouter(prefix="/reviews", tags=["reviews"])

@router.get("/reviews/{id}/reviews")
def get_reviews(id:int, db:Session = Depends(get_db)):
    get_review = db.query(Reviews).filter(Reviews)