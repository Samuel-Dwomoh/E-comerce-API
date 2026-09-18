from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from models import UserModel, LoginModel
from database import get_db
from schemas.schemas import Users
from passlib.context import CryptContext
import jwt
from datetime import datetime, timedelta, timezone
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

router = APIRouter(prefix="/auth", tags=["auth"])

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc)+ expires_delta
    else:
        expire = datetime.now(timezone.utc)+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

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
    
    user_obj = Users(username=details.username, email=details.email, password=hashedPassword)

    db.add(user_obj)
    db.commit()
    db.refresh(user_obj)
    
    return{"message": "User added succesfully"}

@router.post("/login")
def login(details: LoginModel, db: Session = Depends(get_db)):
    
    user = db.query(Users).filter(Users.username == details.username).first()
    
    if not user or not verify_password(details.password, user.password):
        return {"message": "Invalid credentials"}
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    access_token = create_access_token(data={"sub":str(details.username)}, expires_delta=access_token_expires)
    
    return {"access_token": access_token, "token_type": "bearer"}
