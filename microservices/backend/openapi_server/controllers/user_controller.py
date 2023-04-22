import connexion
from pymongo import MongoClient
import six
from typing import Dict
from typing import Tuple
from typing import Union
from openapi_server.models.unavailability import Unavailability
from openapi_server.models.user import User


from openapi_server.models.groups_id_unavailabilities_get200_response import GroupsIdUnavailabilitiesGet200Response  # noqa: E501
from openapi_server.models.groups_id_users_get200_response import GroupsIdUsersGet200Response  # noqa: E501
from openapi_server.models.users_me_get200_response import UsersMeGet200Response  # noqa: E501
from openapi_server.models.users_me_groups_get200_response import UsersMeGroupsGet200Response, GroupMembership  # noqa: E501
from openapi_server import util
from openapi_server.user_utils import get_user_details, get_users


def users_get(search=None, page=None, per_page=None):  # noqa: E501
    """get all users

    returns a list of all users. # noqa: E501

    :param search: a search string to filter users by.
    :type search: str
    :param page: the page of users to retrieve.
    :type page: int
    :param per_page: the number of users to retrieve per page.
    :type per_page: int

    :rtype: Union[GroupsIdUsersGet200Response, Tuple[GroupsIdUsersGet200Response, int], Tuple[GroupsIdUsersGet200Response, int, Dict[str, str]]
    """

    return GroupsIdUsersGet200Response(
        users=get_users(search, page, per_page)
    ).to_dict()



@get_user_details
def users_me_get(user_details: User):  # noqa: E501
    """get the current user

    returns the current user. # noqa: E501


    :rtype: Union[UsersMeGet200Response, Tuple[UsersMeGet200Response, int], Tuple[UsersMeGet200Response, int, Dict[str, str]]
    """
    
    return UsersMeGet200Response(
        user=user_details
    ).to_dict()

@get_user_details
def users_me_groups_get(user_details: User, db: MongoClient):  # noqa: E501
    """get all groups for the current user

    returns a list of all groups for the current user. # noqa: E501


    :rtype: Union[UsersMeGroupsGet200Response, Tuple[UsersMeGroupsGet200Response, int], Tuple[UsersMeGroupsGet200Response, int, Dict[str, str]]
    """

    groups = [
        GroupMembership(
            id=group_membership["_id"].__str__(),
            group=group_membership["group"].__str__(),
            user=group_membership["user"].__str__()
        )
        for group_membership in db.main.group_memberships.find({"user": user_details.id})
    ]
    
    result = UsersMeGroupsGet200Response(
        groups=groups
    )

    return result.to_dict()

@get_user_details
def users_me_unavailabilities_get(user_details: User, db: MongoClient, start=None, end=None):  # noqa: E501
    """get all unavailabilities for the current user

    returns a list of all unavailabilities for the current user. # noqa: E501

    :param start: the start of the time range to retrieve unavailabilities for.
    :type start: str
    :param end: the end of the time range to retrieve unavailabilities for.
    :type end: str

    :rtype: Union[GroupsIdUnavailabilitiesGet200Response, Tuple[GroupsIdUnavailabilitiesGet200Response, int], Tuple[GroupsIdUnavailabilitiesGet200Response, int, Dict[str, str]]
    """
    start = util.deserialize_datetime(start)
    end = util.deserialize_datetime(end)

    unavailabilities = [
        Unavailability(
            end_date=unavailability["end_date"].__str__(),
            id=unavailability["_id"].__str__(),
            item=unavailability["item"].__str__(),
            owner=unavailability["owner"].__str__(),
            start_date=unavailability["start_date"].__str__(),
            type=unavailability["type"]
        )
        for unavailability in db.main.unavailabilities.find({"owner": user_details.id})
    ]


    result = GroupsIdUnavailabilitiesGet200Response(
        unavailabilities=unavailabilities
    )

    return result

