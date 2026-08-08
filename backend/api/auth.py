from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from services.user import register_user, authenticate_user
from schemas.user import UserCreate, UserOut, UserLogin, Token
from utils.security import create_access_token

router = APIRouter()
@router.post("/register", response_model=UserOut)
def register(user_create: UserCreate, db: Session = Depends(get_db)):
    try:
        new_user = register_user(db, user_create)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return new_user

@router.post("/login", response_model=Token)
def login(user_login: UserLogin, db: Session = Depends(get_db)):
    try:
        user = authenticate_user(db, user_login)
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token}