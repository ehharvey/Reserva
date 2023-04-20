from dataclasses import dataclass
import os
import http.client
import json


@dataclass
class Config:
    # auth0
    AUTH0_DOMAIN: str = ""
    AUTH0_CLIENT_ID: str = ""
    AUTH0_CLIENT_SECRET: str = ""
    AUTH0_API_TOKEN: str = ""

    # MongoDB
    MONGO_URI: str = "mongodb://root:example@localhost:27017/"

    # Flask
    FLASK_ENV: str = "development"
    FLASK_DEBUG: bool = True
    FLASK_PORT: int = 8080


def get_env_config():
    env = os.environ.copy()

    # pop out environment variables that are not in the Config object
    for key in list(env.keys()):
        if not hasattr(Config, key):
            env.pop(key)


    return Config(
        **env
    )