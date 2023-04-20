from dataclasses import dataclass
import os


@dataclass
class Config:
    # auth0
    AUTH0_DOMAIN: str
    AUTH0_API_TOKEN: str

    # MongoDB
    MONGO_URI: str
    MONGO_DB: str

    # Flask
    FLASK_ENV: str = "development"
    FLASK_DEBUG: bool = True


def get_env_config():
    return Config(
        AUTH0_DOMAIN=os.environ.get("AUTH0_DOMAIN"),
        AUTH0_API_TOKEN=os.environ.get("AUTH0_API_TOKEN"),
        MONGO_URI=os.environ.get("MONGO_URI"),
        MONGO_DB=os.environ.get("MONGO_DB"),
    )