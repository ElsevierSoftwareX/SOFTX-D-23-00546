from pydantic import BaseSettings


class CommonSettings(BaseSettings):
    APP_NAME: str = "KorCAT-web"
    DEBUG_MODE: bool = False


class ServerSettings(BaseSettings):
    HOST: str = "0.0.0.0"
    PORT: int = 8000


class DatabaseSettings(BaseSettings):
    DB_URL: str="mongodb+srv://admin:devil286@korcat-web-cluster.nv1kxic.mongodb.net/?retryWrites=true&w=majority"
    DB_NAME: str="KorCAT-web"


class Settings(CommonSettings, ServerSettings, DatabaseSettings):
    pass


settings = Settings()
