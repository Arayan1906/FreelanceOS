from passlib.context import CryptContext

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

