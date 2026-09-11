from fastapi import APIRouter
from models import User


router = APIRouter(prefix="/auth", tags=["auth"])

@router.get("/register")
def register(details:User):
    return{details}
    