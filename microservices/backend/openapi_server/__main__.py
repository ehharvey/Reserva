#!/usr/bin/env python3

from dotenv import load_dotenv
import connexion

from openapi_server import encoder
from flask_cors import CORS
from flask_injector import FlaskInjector
from openapi_server.config import get_env_config
from openapi_server.user_utils import configure as configure_user_utils

def main():
    app = connexion.App(__name__, specification_dir='./openapi/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('openapi.yaml',
                arguments={'title': 'Main API'},
                pythonic_params=True)

    config = get_env_config()

    if config.FLASK_ENV == "development":
        load_dotenv()
        config = get_env_config()

    # Configure user utils
    configure_user_utils(
        domain=config.AUTH0_DOMAIN,
        management_api_token=config.AUTH0_API_TOKEN
    )

    # Enable CORS
    CORS(app.app)
    app.run(port=8080, debug=config.FLASK_DEBUG)


if __name__ == '__main__':
    main()
