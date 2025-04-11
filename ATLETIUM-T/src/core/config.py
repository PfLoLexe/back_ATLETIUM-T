import os

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

        environment = os.getenv("ENVIRONMENT")

        self.db_url = os.getenv(environment + "_DB_URL")
        self.username_salt = os.getenv(
            environment + "_USERNAME_SALT")
        self.password_salt = os.getenv(
            environment + "_PASSWORD_SALT")
        # загрузка других переменных окружения
        # ...

        self.pincode_salt = os.getenv(environment + "_PINCODE_SALT")
        self.jwt_token_type = os.getenv(environment + "_JWT_TOKEN_TYPE")
        self.access_token_expire_time_long = os.getenv(environment + "_ACCESS_TOKEN_LONG_EXPIRE_TIME")
        self.access_token_expire_time_standard = os.getenv(environment + "_ACCESS_TOKEN_STANDARD_EXPIRE_TIME")
        self.jwt_secret_key = os.getenv(environment + "_SECRET_KEY")
        self.jwt_algorithm = os.getenv(environment + "_JWT_TOKEN_GENERATION_ALGORITHM")
        self.jwt_token_expire_time_string_format = os.getenv(environment + "_JWT_TOKEN_EXPIRE_TIME_STRING_FORMAT")


app_configuration: Config = Config()
