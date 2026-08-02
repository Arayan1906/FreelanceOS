from sqlalchemy.orm import Session
from models.user import User

def get_user_by_email(db: Session, email: str) -> User | None:
    # Look up a single user row by email, or None if no match. Used for both
    # login (find the user to check) and registration (check email isn't taken).
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, email:str, hashed_password:str, full_name:str) -> User:
    # Create a new user row in the database. Used for registration.
    user = User(email=email, hashed_password=hashed_password, full_name=full_name)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

