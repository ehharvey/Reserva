import connexion
import six
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.user import User  # noqa: E501
from openapi_server.models.users_get200_response import UsersGet200Response  # noqa: E501
from openapi_server.models.users_user_id_groups_get200_response import UsersUserIdGroupsGet200Response  # noqa: E501
from openapi_server import util


def users_admins_get():  # noqa: E501
    """get all admin users

    returns a list of all admin users. # noqa: E501


    :rtype: Union[List[User], Tuple[List[User], int], Tuple[List[User], int, Dict[str, str]]
    """
    return 'do some magic!'


def users_get():  # noqa: E501
    """get all users

    returns a list of all users. # noqa: E501


    :rtype: Union[UsersGet200Response, Tuple[UsersGet200Response, int], Tuple[UsersGet200Response, int, Dict[str, str]]
    """
    return 'do some magic!'


def users_standard_get():  # noqa: E501
    """get all standard users

    returns a list of all standard users. # noqa: E501


    :rtype: Union[List[User], Tuple[List[User], int], Tuple[List[User], int, Dict[str, str]]
    """
    return 'do some magic!'


def users_user_id_get(user_id):  # noqa: E501
    """get a user by id

    returns a single user by id. # noqa: E501

    :param user_id: the id of the user to retrieve.
    :type user_id: int

    :rtype: Union[User, Tuple[User, int], Tuple[User, int, Dict[str, str]]
    """
    return 'do some magic!'


def users_user_id_groups_get(user_id):  # noqa: E501
    """get all groups for a user

    returns a list of all groups for a user. # noqa: E501

    :param user_id: the id of the user to retrieve groups for.
    :type user_id: int

    :rtype: Union[UsersUserIdGroupsGet200Response, Tuple[UsersUserIdGroupsGet200Response, int], Tuple[UsersUserIdGroupsGet200Response, int, Dict[str, str]]
    """
    return 'do some magic!'
