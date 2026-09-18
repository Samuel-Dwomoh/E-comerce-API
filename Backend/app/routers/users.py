from fastapi import APIRouter, Depends
from database import get_db
from sqlalchemy.orm import Session
from schemas.schemas import Users
router = APIRouter(prefix="/users", tags=["users"])

@router.get("/users/{id}")
def get_user(id:int, db: Session = Depends(get_db)):
    user = db.query(Users).filter(Users.id == id).first()
    if not user:
        return{"message":"User not found"}
    return user

@router.delete("/users/{id}")
def delete_user(id:int, db:Session =Depends(get_db)):
    user = db.query(Users).filter(Users.id == id).first()
    if not user:
        return{"message":"User not found"}
    db.delete(user)
    db.commit()
    return{"message":"User deleted successfully"}