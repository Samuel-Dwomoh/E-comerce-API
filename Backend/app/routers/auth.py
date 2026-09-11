from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models import UserModel
from database import get_db
from schemas.schemas import Users


router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register")
def register(details:UserModel, db: Session = Depends(get_db)):
    
    new_user = db.query(Users).filter(Users.username == details.username).first()
    
    if new_user:
        return {"message": "User already exists"}
    
    db.add(Users(username=details.username, email=details.email, password=details.password))
    db.commit()
    db.refresh
    