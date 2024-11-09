import bcrypt

from src.core.config import app_configuration


class Hasher:
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

    @staticmethod
    def get_pincode_hash(pincode: str) -> str:
        hashed_pincode = bcrypt.hashpw(
            password=pincode.encode(),
            salt=app_configuration.pincode_salt.encode()
        ).decode()
        return hashed_pincode
