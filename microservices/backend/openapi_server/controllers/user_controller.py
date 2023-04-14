import connexion
import six
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.new_user import NewUser  # noqa: E501
from openapi_server.models.update_user import UpdateUser  # noqa: E501
from openapi_server.models.user import User  # noqa: E501
from openapi_server.models.users_user_id_groups_get200_response import UsersUserIdGroupsGet200Response  # noqa: E501
from openapi_server import util


def users_admins_get():  # noqa: E501
    """Get all admin users

    Returns a list of all admin users. # noqa: E501


    :rtype: Union[List[User], Tuple[List[User], int], Tuple[List[User], int, Dict[str, str]]
    """
    return 'do some magic!'


def users_admins_post(new_user):  # noqa: E501
    """Create a new admin user

    Creates a new admin user account. # noqa: E501

    :param new_user: 
    :type new_user: dict | bytes

    :rtype: Union[User, Tuple[User, int], Tuple[User, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        new_user = NewUser.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def users_get():  # noqa: E501
    """Get all users

    Returns a list of all users. # noqa: E501


    :rtype: Union[List[User], Tuple[List[User], int], Tuple[List[User], int, Dict[str, str]]
    """
    return 'do some magic!'


def users_post(new_user):  # noqa: E501
    """Create a new user

    Creates a new user account. # noqa: E501

    :param new_user: 
    :type new_user: dict | bytes

    :rtype: Union[User, Tuple[User, int], Tuple[User, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        new_user = NewUser.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def users_standard_get():  # noqa: E501
    """Get all standard users

    Returns a list of all standard users. # noqa: E501


    :rtype: Union[List[User], Tuple[List[User], int], Tuple[List[User], int, Dict[str, str]]
    """
    return 'do some magic!'


def users_standard_post(new_user):  # noqa: E501
    """Create a new standard user

    Creates a new standard user account. # noqa: E501

    :param new_user: 
    :type new_user: dict | bytes

    :rtype: Union[User, Tuple[User, int], Tuple[User, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        new_user = NewUser.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def users_user_id_delete(user_id):  # noqa: E501
    """Delete a user by ID

    Deletes an existing user account. # noqa: E501

    :param user_id: The ID of the user to delete.
    :type user_id: int

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def users_user_id_get(user_id):  # noqa: E501
    """Get a user by ID

    Returns a single user by ID. # noqa: E501

    :param user_id: The ID of the user to retrieve.
    :type user_id: int

    :rtype: Union[User, Tuple[User, int], Tuple[User, int, Dict[str, str]]
    """
    return 'do some magic!'


def users_user_id_groups_get(user_id):  # noqa: E501
    """Get all groups for a user

    Returns a list of all groups for a user. # noqa: E501

    :param user_id: The ID of the user to retrieve groups for.
    :type user_id: int

    :rtype: Union[UsersUserIdGroupsGet200Response, Tuple[UsersUserIdGroupsGet200Response, int], Tuple[UsersUserIdGroupsGet200Response, int, Dict[str, str]]
    """
    return 'do some magic!'


def users_user_id_put(user_id, update_user):  # noqa: E501
    """Update a user by ID

    Updates an existing user account. # noqa: E501

    :param user_id: The ID of the user to update.
    :type user_id: int
    :param update_user: 
    :type update_user: dict | bytes

    :rtype: Union[User, Tuple[User, int], Tuple[User, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        update_user = UpdateUser.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
