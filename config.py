from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional
class Settings(BaseSettings):
    
    OPENROUTER_API_KEY: str
    OPENROUTER_MODEL_NAME: str 

    CERBRASE_API_KEY: str 

    GEMINI_API_KEY:str
    GEMINI_MODEL:str

    GROQ_API_KEY:str
    GROQ_MODEL:str

    FIREWORKS_MODEL: str
    FIREWORKS_API_KEY:str

    MISTRAL_KEY:str
    MISTRAL_MODEL:str

    OPENAI_KEY:str
    OPENAI_MODEL:str

    TEMPR: float
    class Config:
        env_file = ".env"
        extra = "ignore"  # Ignore extra fields
def get_settings():
    return Settings()