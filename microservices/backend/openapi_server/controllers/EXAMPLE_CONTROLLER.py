# This is not a real controller, just an example of how to use
# the database and retrieve user data

import connexion
from pymongo import MongoClient
from openapi_server.db_utils import create_item
from openapi_server.models.items_post201_response import ItemsPost201Response
from openapi_server.models.new_item import NewItem
from openapi_server.models.user import User
from openapi_server.models.users_me_get200_response import UsersMeGet200Response
from openapi_server.user_utils import get_user_details
from openapi_server.models.users_me_groups_get200_response import UsersMeGroupsGet200Response
from openapi_server.models.group_membership import GroupMembership


# user = USER ID
# db = DATABASE CONNECTION
def users_me_groups_get(user, client: MongoClient):  # noqa: E501
    """get all groups for the current user

    returns a list of all groups for the current user. # noqa: E501


    :rtype: Union[UsersMeGroupsGet200Response, Tuple[UsersMeGroupsGet200Response, int], Tuple[UsersMeGroupsGet200Response, int, Dict[str, str]]
    """

    groups = [
        GroupMembership(
            **group
        )
        for group in client.main.groupMemberships.find({"user": user})
    ]
    

    result = UsersMeGroupsGet200Response(
        groups=groups
    )

    return result.to_dict()


# get_user_details is a decorator that retrieves the user data
# and supplies it as user_details parameter to the function
@get_user_details
def users_me_get(user_details: User):  # noqa: E501
    """get the current user

    returns the current user. # noqa: E501


    :rtype: Union[UsersMeGet200Response, Tuple[UsersMeGet200Response, int], Tuple[UsersMeGet200Response, int, Dict[str, str]]
    """
    
    return UsersMeGet200Response(
        user=user_details
    ).to_dict()


# This example shows how to use the database to create a new item
# We have utils to create items which return the created item
def items_post(new_item=None):  # noqa: E501
    """posts an item. for now, the only kind of item is a room.

     # noqa: E501

    :param new_item: 
    :type new_item: dict | bytes

    :rtype: Union[ItemsPost201Response, Tuple[ItemsPost201Response, int], Tuple[ItemsPost201Response, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        new_item = NewItem.from_dict(connexion.request.get_json())  # noqa: E501
        created = create_item(new_item)
        return ItemsPost201Response(room=created), 201
    return 'do some magic!'