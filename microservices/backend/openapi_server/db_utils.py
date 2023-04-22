import datetime
from bson import ObjectId
from pymongo import MongoClient
from openapi_server.models.base_model_ import Model
from openapi_server.models import NewItem, NewGroup, NewGroupMembership, NewUnavailability
from openapi_server.models import Item, Group, GroupMembership, Unavailability

def create_item(new_item: NewItem, user, client: MongoClient) -> Item:
    """
    Create an item in the database

    :param new_item: The new item
    :param client: The database client
    """

    db = client["main"]
    items = db["items"]

    item = Item(
        id=ObjectId(),
        created_by=user,
        create_date=datetime.datetime.now(),
        last_update_date=datetime.datetime.now(),
        **new_item.to_dict()
    )

    item_dict = item.to_dict()
    item_dict["_id"] = item_dict.pop("id")

    items.insert_one(item_dict)

    return item

def create_group(new_group: NewGroup, user, client: MongoClient) -> Group:
    """
    Create a group in the database

    :param new_group: The new group
    :param client: The database client
    """

    db = client["main"]
    groups = db["groups"]

    group = Group(
        id=ObjectId(),
        owner=user,
        create_date=datetime.datetime.now(),
        last_update_date=datetime.datetime.now(),
        **new_group.to_dict()
    )

    group_dict = group.to_dict()
    group_dict["_id"] = group_dict.pop("id")

    groups.insert_one(group_dict)

    return group

def create_group_membership(new_group_membership: NewGroupMembership,  client: MongoClient) -> GroupMembership:
    """
    Create a group membership in the database

    :param new_group_membership: The new group membership
    :param client: The database client
    """

    db = client["main"]
    group_memberships = db["group_memberships"]

    group_membership = GroupMembership(
        id=ObjectId(),
        **new_group_membership.to_dict()
    )

    group_membership_dict = group_membership.to_dict()
    group_membership_dict["_id"] = group_membership_dict.pop("id")

    group_memberships.insert_one(group_membership_dict)

    return group_membership

def create_unavailability(new_unavailability: NewUnavailability, client: MongoClient) -> Unavailability:
    """
    Create an unavailability in the database

    :param new_unavailability: The new unavailability
    :param client: The database client
    """

    db = client["main"]
    unavailabilities = db["unavailabilities"]

    unavailability = Unavailability(
        id=ObjectId(),
        create_date=datetime.datetime.now(),
        last_updated_date=datetime.datetime.now(),
        **new_unavailability.to_dict()
    )

    unavailability_dict = unavailability.to_dict()
    unavailability_dict["_id"] = unavailability_dict.pop("id")

    unavailabilities.insert_one(unavailability_dict)

    return get_model_from_mongo(unavailability_dict)

def get_model_from_mongo(mongo: dict) -> Model:
    """
    Convert a mongo dict to a model

    :param mongo: The mongo dict
    """

    mongo["id"] = mongo.pop("_id")

    # Convert any ObjectId to a string
    for key in mongo:
        if isinstance(mongo[key], ObjectId):
            mongo[key] = str(mongo[key])

    return Model.from_dict(mongo)