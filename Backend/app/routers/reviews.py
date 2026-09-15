from fastapi import APIRouter
from sqlalchemy.orm import Session
from database import get_db
router = APIRouter(prefix="/reviews", tags=["reviews"])

@router.get("/reviews")
def get_reviews():
    pass