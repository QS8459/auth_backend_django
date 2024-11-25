from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    pg_database:str
    pg_user: str
    pg_password: str
    pg_host: str
    secret_key: str

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

settings = Settings()