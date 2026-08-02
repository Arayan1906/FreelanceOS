from sqlalchemy.orm import Session
from schemas.user import UserCreate
from repositories.user import get_user_by_email, create_user
from utils.security import hash_password
from models.user import User

def register_user(db: Session, user_create: UserCreate) -> User:
    existing_user = get_user_by_email(db, user_create.email)
    if existing_user:
        raise ValueError("Email already registered")
    hashed_password = hash_password(user_create.password)
    new_user = create_user(db, user_create.email, hashed_password, user_create.full_name)
    return new_user