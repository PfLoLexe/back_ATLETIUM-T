import bcrypt

from src.core.config import app_configuration


class PasswordHasher:
    @staticmethod
    def get_password_hash(password: str, username: str) -> str:
        hashed_username = bcrypt.hashpw(
            username.encode(),
            salt=app_configuration.username_salt.encode()
        ).decode()
        return bcrypt.hashpw(
            (hashed_username+password).encode(),
            salt=app_configuration.password_salt.encode()
        ).decode()
