﻿import os

from dotenv import load_dotenv


class Config:

    username_salt: str = None
    password_salt: str = None
    pincode_salt: str = None
    jwt_token_type: str = None
    access_token_expire_time_long: str = None
    access_token_expire_time_standard: str = None
    jwt_algorithm: str = None
    jwt_secret_key: str = None
    jwt_token_expire_time_string_format: str = None
    db_url: str = None

    def load_configuration(self):
        load_dotenv()

        self.db_url = os.getenv("DB_URL")

        self.username_salt = os.getenv("USERNAME_SALT")
        self.password_salt = os.getenv("PASSWORD_SALT")
        self.pincode_salt = os.getenv("PINCODE_SALT")

        self.jwt_token_type = os.getenv("JWT_TOKEN_TYPE")
        self.access_token_expire_time_long = os.getenv("ACCESS_TOKEN_LONG_EXPIRE_TIME")
        self.access_token_expire_time_standard = os.getenv("ACCESS_TOKEN_STANDARD_EXPIRE_TIME")
        self.jwt_secret_key = os.getenv("SECRET_KEY")
        self.jwt_algorithm = os.getenv("JWT_TOKEN_GENERATION_ALGORITHM")
        self.jwt_token_expire_time_string_format = os.getenv("JWT_TOKEN_EXPIRE_TIME_STRING_FORMAT")

app_configuration: Config = Config()
