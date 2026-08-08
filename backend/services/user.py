from sqlalchemy.orm import Session
from schemas.user import UserCreate, UserLogin
from repositories.user import get_user_by_email, create_user
from utils.security import hash_password, verify_password
from models.user import User

def register_user(db: Session, user_create: UserCreate) -> User:
    existing_user = get_user_by_email(db, user_create.email)
    if existing_user:
        raise ValueError("Email already registered")
    hashed_password = hash_password(user_create.password)
    new_user = create_user(db, user_create.email, hashed_password, user_create.full_name)
    return new_user

def authenticate_user(db: Session, user_login: UserLogin) -> User :
    user = get_user_by_email(db, user_login.email)
    if not user:
        raise ValueError("Invalid email or password")
    if not verify_password(user_login.password, user.hashed_password):
        raise ValueError("Invalid email or password")
    return user