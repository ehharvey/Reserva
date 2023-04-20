import connexion
import six
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.groups_id_unavailabilities_get200_response import GroupsIdUnavailabilitiesGet200Response  # noqa: E501
from openapi_server.models.groups_id_users_get200_response import GroupsIdUsersGet200Response  # noqa: E501
from openapi_server.models.users_me_get200_response import UsersMeGet200Response  # noqa: E501
from openapi_server.models.users_me_groups_get200_response import UsersMeGroupsGet200Response, GroupMembership  # noqa: E501
from openapi_server import util


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
    return 'do some magic!'


def users_me_get():  # noqa: E501
    """get the current user

    returns the current user. # noqa: E501


    :rtype: Union[UsersMeGet200Response, Tuple[UsersMeGet200Response, int], Tuple[UsersMeGet200Response, int, Dict[str, str]]
    """
    


    return 'do some magic!'


def users_me_groups_get(user):  # noqa: E501
    """get all groups for the current user

    returns a list of all groups for the current user. # noqa: E501


    :rtype: Union[UsersMeGroupsGet200Response, Tuple[UsersMeGroupsGet200Response, int], Tuple[UsersMeGroupsGet200Response, int, Dict[str, str]]
    """

    result = UsersMeGroupsGet200Response(
        groups=[
            GroupMembership(
                id="groupmembership-026ce71f-2dfc-4dfa-b609-59d71929556f",
                user=user,
                group="group-026ce71f-2dfc-4dfa-b609-59d71929556f",
            )
        ]
    )

    return result.to_dict()

def users_me_unavailabilities_get(start=None, end=None):  # noqa: E501
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
    return 'do some magic!'
