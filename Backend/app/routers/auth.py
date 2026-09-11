from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models import User
from database import get_db

router = APIRouter(prefix="/auth", tags=["auth"])

@router.get("/register")
def register(details:User, db: Session = Depends(get_db)):
    pass
    