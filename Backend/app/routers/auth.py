from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models import UserModel, LoginModel
from database import get_db
from schemas.schemas import Users
from passlib.context import CryptContext


router = APIRouter(prefix="/auth", tags=["auth"])

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password:str, hashed_password:str):
    return pwd_context.verify(plain_password, hashed_password)

@router.post("/register")
def register(details:UserModel, db: Session = Depends(get_db)):
    
    new_user = db.query(Users).filter(Users.username == details.username).first()
    
    if new_user:
        return {"message": "User already exists"}

    hashedPassword = hash_password(details.password)

    db.add(Users(username=details.username, email=details.email, password=hashedPassword))
    db.commit()
    db.refresh(new_user)
    
    return{"message": "User added succesfully"}

@router.post("/login")
def login(details: LoginModel, db: Session = Depends(get_db)):
    
    user = db.query(Users).filter(Users.username == details.username).first()
    
    if not user or not verify_password(details.password, user.password):
        return {"message": "Invalid credentials"}
    
    return {"message": "Login successful"}