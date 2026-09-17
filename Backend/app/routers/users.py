from fastapi import APIRouter, Depends
from database import get_db
from sqlalchemy.orm import Session
router = APIRouter(prefix="/users", tags=["users"])

@router.get("/users/{id}")
