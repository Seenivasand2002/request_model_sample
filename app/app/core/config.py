from pydantic import AnyHttpUrl
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
   
    SQLALCHEMY_DATABASE_URL: str = "mysql+pymysql://python_admin:12345@192.168.1.108/test_employee"
    BACKEND_CORS_ORIGINS: list[AnyHttpUrl] = ["http://localhost:8000","http://localhost:8002",  "http://localhost:8080", "http://localhost:3000",
                                              "http://localhost:3001", "http://localhost:3002", "https://cbe.themaestro.in", "http://cbe.themaestro.in",
                                              ]      
settings = Settings()