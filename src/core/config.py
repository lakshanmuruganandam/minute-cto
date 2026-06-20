from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Minute CTO Agent"
    environment: str = "production"
    model_temperature: float = 0.2
    
    class Config:
        env_file = ".env"

settings = Settings()
