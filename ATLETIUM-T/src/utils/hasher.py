import os
import bcrypt
from dotenv import load_dotenv

load_dotenv()

class Hasher:
    @staticmethod
    def get_password_hash(password: str, username: str) -> str:
        hashed_username = bcrypt.hashpw(
            username.encode(),
            salt=(os.getenv("USERNAME_SALT")).encode()
        ).decode()
        return bcrypt.hashpw(
            (hashed_username+password).encode(),
            salt=(os.getenv("PWD_SALT")).encode()
        ).decode()
