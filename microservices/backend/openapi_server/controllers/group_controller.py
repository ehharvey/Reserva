import connexion
import six
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.group_memberships_post201_response import GroupMembershipsPost201Response  # noqa: E501
from openapi_server.models.groups_id_users_get200_response import GroupsIdUsersGet200Response  # noqa: E501
from openapi_server.models.groups_post201_response import GroupsPost201Response  # noqa: E501
from openapi_server.models.new_group import NewGroup  # noqa: E501
from openapi_server.models.new_group_membership import NewGroupMembership  # noqa: E501
from openapi_server.models.update_group import UpdateGroup  # noqa: E501
from openapi_server import util


def group_memberships_post(new_group_membership=None):  # noqa: E501
    """creates a new groupMembership object

    creates a new groupMembership object. Only the group owner can create a membership. (After a user becomes a member, they can delete their own membership.)  # noqa: E501

    :param new_group_membership: 
    :type new_group_membership: dict | bytes

    :rtype: Union[GroupMembershipsPost201Response, Tuple[GroupMembershipsPost201Response, int], Tuple[GroupMembershipsPost201Response, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        new_group_membership = NewGroupMembership.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def groups_id_delete(id):  # noqa: E501
    """deletes a group object.  Also deletes all groupMembership objects associated with the group. 

    deletes a group object # noqa: E501

    :param id: 
    :type id: str
    :type id: str

    :rtype: Union[GroupsPost201Response, Tuple[GroupsPost201Response, int], Tuple[GroupsPost201Response, int, Dict[str, str]]
    """
    return 'do some magic!'


def groups_id_memberships_membership_id_delete(id, membership_id):  # noqa: E501
    """deletes a groupMembership object

    deletes a groupMembership object.  The group owner can delete any membership. A user can delete their own membership.  # noqa: E501

    :param id: 
    :type id: str
    :type id: str
    :param membership_id: 
    :type membership_id: str
    :type membership_id: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def groups_id_put(id, update_group=None):  # noqa: E501
    """updates a group object

    updates a group object # noqa: E501

    :param id: 
    :type id: str
    :type id: str
    :param update_group: 
    :type update_group: dict | bytes

    :rtype: Union[GroupsPost201Response, Tuple[GroupsPost201Response, int], Tuple[GroupsPost201Response, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        update_group = UpdateGroup.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def groups_id_users_get(id):  # noqa: E501
    """gets a list of user objects

    gets a list of user objects for a group # noqa: E501

    :param id: 
    :type id: str
    :type id: str

    :rtype: Union[GroupsIdUsersGet200Response, Tuple[GroupsIdUsersGet200Response, int], Tuple[GroupsIdUsersGet200Response, int, Dict[str, str]]
    """
    return 'do some magic!'


def groups_post(new_group=None):  # noqa: E501
    """creates a new group object

    creates a new group object # noqa: E501

    :param new_group: 
    :type new_group: dict | bytes

    :rtype: Union[GroupsPost201Response, Tuple[GroupsPost201Response, int], Tuple[GroupsPost201Response, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        new_group = NewGroup.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
