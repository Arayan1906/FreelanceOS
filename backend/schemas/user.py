from pydantic import BaseModel, EmailStr
from datetime import datetime

# What the client sends when registering. Plaintext password here is fine -
# it travels over HTTPS and gets hashed by the service before ever touching the DB.
class UserCreate(BaseModel):
    email: EmailStr
    password: str
    full_name :str

# What we send back to the client. Deliberately has no password/hashed_password
# field - Pydantic only reads fields declared here, so it can never leak it,
# even if a full User ORM object (which does have hashed_password) is passed in.
class UserOut(BaseModel):
    id: int
    email: EmailStr
    full_name: str
    is_active: bool
    created_at: datetime

    class Config:
        # Lets this schema be built from an object's attributes (e.g. a SQLAlchemy
        # User row: user.id, user.email) instead of only from a dict.
        from_attributes = True

# What the client sends when logging in.
class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"