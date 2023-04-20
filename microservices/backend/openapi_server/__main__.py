#!/usr/bin/env python3

from dotenv import load_dotenv
import connexion
from injector import SingletonScope

from openapi_server import encoder
from flask_cors import CORS
from flask_injector import FlaskInjector, RequestScope
from pymongo import MongoClient
from pymongo.database import Database

from mongoengine import connect
from openapi_server.config import get_env_config
from openapi_server.user_utils import configure as configure_user_utils, configure_dev

config = get_env_config()

if config.FLASK_ENV == "development":
    load_dotenv()
    config = get_env_config()

def mongo_client():
    client = MongoClient(config.MONGO_URI)

    return client

# Configure dependency injection
def configure(binder):
    binder.bind(MongoClient, to=mongo_client(), scope=RequestScope)


def main():
    app = connexion.App(__name__, specification_dir='./openapi/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('openapi.yaml',
                arguments={'title': 'Main API'},
                pythonic_params=True)

    

    # Configure user utils
    if config.FLASK_ENV == "development":
        configure_dev()
    else:
        configure_user_utils(
            domain=config.AUTH0_DOMAIN,
            management_api_token=config.AUTH0_API_TOKEN
        )

    # Configure FlaskInjector
    FlaskInjector(app=app.app, modules=[configure])

    # Enable CORS
    CORS(app.app)

    app.run(port=8080, debug=config.FLASK_DEBUG)


if __name__ == '__main__':
    main()
