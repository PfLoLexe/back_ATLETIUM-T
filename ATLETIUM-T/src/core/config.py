import os

from dotenv import load_dotenv


class Config:

    username_salt: str
    password_salt: str
    jwt_token_type: str
    access_token_expire_time_long: str
    access_token_expire_time_standard: str
    jwt_algorithm: str
    jwt_secret_key: str
    db_url: str

    def load_configuration(self):
        load_dotenv()

        self.db_url = os.getenv("DB_URL")

        self.username_salt = os.getenv("USERNAME_SALT")
        self.password_salt = os.getenv("PASSWORD_SALT")

        self.jwt_token_type = os.getenv("JWT_TOKEN_TYPE")
        self.access_token_expire_time_long = os.getenv("ACCESS_TOKEN_LONG_EXPIRE_TIME")
        self.access_token_expire_time_standard = os.getenv("ACCESS_TOKEN_STANDARD_EXPIRE_TIME")
        self.jwt_secret_key = os.getenv("SECRET_KEY")
        self.jwt_algorithm = os.getenv("JWT_TOKEN_GENERATION_ALGORITHM")

app_configuration: Config = Config()
