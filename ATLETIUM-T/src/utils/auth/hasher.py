import os
import bcrypt
from passlib.context import CryptContext
from dotenv import load_dotenv

load_dotenv()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str, username: str) -> str:
    hashed_username = pwd_context.hash(username)
    return bcrypt.hashpw(
        (password+hashed_username).encode(),
        salt=(os.getenv("SALT")).encode()
    ).decode()
