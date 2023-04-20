# This is not a real controller, just an example of how to use
# the database and retrieve user data

from pymongo import MongoClient
from openapi_server.models.user import User
from openapi_server.models.users_me_get200_response import UsersMeGet200Response
from openapi_server.user_utils import get_user_details
from openapi_server.models.users_me_groups_get200_response import UsersMeGroupsGet200Response
from openapi_server.models.group_membership import GroupMembership


# user = USER ID
# db = DATABASE CONNECTION
def users_me_groups_get(user, db: MongoClient):  # noqa: E501
    """get all groups for the current user

    returns a list of all groups for the current user. # noqa: E501


    :rtype: Union[UsersMeGroupsGet200Response, Tuple[UsersMeGroupsGet200Response, int], Tuple[UsersMeGroupsGet200Response, int, Dict[str, str]]
    """

    groups = [
        GroupMembership(
            **group
        )
        for group in db.main.groupMemberships.find({"user": user})
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