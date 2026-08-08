from passlib.context import CryptContext
import os
from datetime import datetime, timedelta, timezone
from jose import jwt
# Configures which hashing algorithm(s) to use. bcrypt is one-way (can verify,
# can't reverse) and auto-salts, so identical passwords produce different hashes.
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    # Turns a plaintext password into a hash to store in hashed_password.
    return pwd_context.hash(password)

def verify_password(password: str, hashed_password: str) -> bool:
    # Checks a plaintext password (e.g. from a login request) against the stored
    # hash. Never decrypts the hash - just recomputes and compares.
    return pwd_context.verify(password, hashed_password)

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # 30 minutes
def create_access_token(data: dict) -> str:
    # Creates a JWT access token with an expiration time.
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt