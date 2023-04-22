#!/usr/bin/env python3

import datetime
from dotenv import load_dotenv
import connexion
from injector import SingletonScope
from openapi_server.controllers.security_controller_ import configure_jwk_client_dev, configure_jwk_client

from openapi_server import encoder
from flask_cors import CORS
from flask_injector import FlaskInjector, RequestScope
from pymongo import MongoClient
from pymongo.database import Database
from bson import ObjectId

from openapi_server.config import get_env_config
from openapi_server.user_utils import configure_prod as configure_user_utils, configure_dev

from openapi_server.models import NewItem, NewGroup, NewGroupMembership, NewUnavailability, Feature
from openapi_server.db_utils import create_item, create_group, create_group_membership, create_unavailability

config = get_env_config()

if config.FLASK_ENV == "development":
    load_dotenv()
    config = get_env_config()

def mongo_client():
    client = MongoClient(config.MONGO_URI)

    return client

# Configure dependency injection
def configure_prod(binder):
    binder.bind(MongoClient, to=mongo_client(), scope=RequestScope)


def seed_db():
    client = mongo_client()
    db = client["main"]

    # Clear all collections
    db["items"].delete_many({})
    db["groups"].delete_many({})
    db["unavailabilities"].delete_many({})
    db["group_memberships"].delete_many({})

    # Seed items
    items = [
        NewItem(
            name="Room 1", 
            description="Description A",
            location="Location A",
            type="Room",
            features=[
                Feature(name="Feature 1", value="Value 1"),
                Feature(name="Feature 2", value="Value 2"),
                Feature(name="Feature 3", value="Value 3"),
            ],
        ),
        NewItem(
            name="Item 2",
            description="Description B",
            location="Location B",
            type="Room",
            features=[
                Feature(name="Feature 1", value="Value 1"),
                Feature(name="Feature 2", value="Value 2"),
                Feature(name="Feature 3", value="Value 3"),
            ],
        ),
    ]

    created_items = [
        create_item(item, "auth0|643db743a891bec857308e2f", client)
        for item in items
    ]

    # Seed groups
    groups = [
        NewGroup(
            name="Group 1"
        )
    ]

    created_groups = [
        create_group(group, "auth0|643db743a891bec857308e2f", client)
        for group in groups
    ]

    # Seed group memberships
    group_memberships = [
        NewGroupMembership(
            group=cg.id,
            user="auth0|643db743a891bec857308e2f",
        )

        for cg in created_groups
    ]

    for group_membership in group_memberships:
        create_group_membership(group_membership, client)

    # Seed unavailable times
    unavailabilities = [
        NewUnavailability(
            item=item.id,
            owner="auth0|643db743a891bec857308e2f",
            start_date=datetime.datetime.now(),
            end_date=datetime.datetime.now() + datetime.timedelta(hours=1),
            type="Booking"
        )
        for item in created_items
    ]

    for unavailability in unavailabilities:
        create_unavailability(unavailability, client)


def main():
    app = connexion.App(__name__, specification_dir='./openapi/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('openapi.yaml',
                arguments={'title': 'Main API'},
                pythonic_params=True)

    if config.FLASK_ENV == "development":
        configure_dev()
        seed_db()
        configure_jwk_client_dev()
    else:
        configure_user_utils(
            domain=config.AUTH0_DOMAIN,
            management_api_token=config.AUTH0_API_TOKEN
        )
        configure_jwk_client(
            domain=config.AUTH0_DOMAIN
        )

    # Configure FlaskInjector
    FlaskInjector(app=app.app, modules=[configure_prod])

    # Enable CORS
    CORS(app.app)

    app.run(port=8080, debug=config.FLASK_DEBUG)


if __name__ == '__main__':
    main()
