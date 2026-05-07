from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    BOT_TOKEN: str
    ADMIN_IDS: list[int]
    DATABASE_URL: str = "sqlite+aiosqlite:///./movies.db"
    TMDB_API_KEY: str
    WEBAPP_URL: str
    
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()
