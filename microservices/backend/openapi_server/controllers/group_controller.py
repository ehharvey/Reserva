import connexion
import six
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.groups_get200_response import GroupsGet200Response  # noqa: E501
from openapi_server.models.groups_id_memberships_get200_response import GroupsIdMembershipsGet200Response  # noqa: E501
from openapi_server.models.groups_id_memberships_post201_response import GroupsIdMembershipsPost201Response  # noqa: E501
from openapi_server.models.groups_post201_response import GroupsPost201Response  # noqa: E501
from openapi_server.models.new_group import NewGroup  # noqa: E501
from openapi_server.models.new_group_membership import NewGroupMembership  # noqa: E501
from openapi_server.models.update_group import UpdateGroup  # noqa: E501
from openapi_server import util


def groups_get():  # noqa: E501
    """Gets a list of Group objects

     # noqa: E501


    :rtype: Union[GroupsGet200Response, Tuple[GroupsGet200Response, int], Tuple[GroupsGet200Response, int, Dict[str, str]]
    """
    return 'do some magic!'


def groups_id_delete(id):  # noqa: E501
    """Deletes a Group object

     # noqa: E501

    :param id: 
    :type id: str
    :type id: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def groups_id_get(id):  # noqa: E501
    """Gets a Group object by id

     # noqa: E501

    :param id: 
    :type id: str
    :type id: str

    :rtype: Union[GroupsPost201Response, Tuple[GroupsPost201Response, int], Tuple[GroupsPost201Response, int, Dict[str, str]]
    """
    return 'do some magic!'


def groups_id_memberships_get(id):  # noqa: E501
    """Gets a list of GroupMembership objects

     # noqa: E501

    :param id: 
    :type id: str
    :type id: str

    :rtype: Union[GroupsIdMembershipsGet200Response, Tuple[GroupsIdMembershipsGet200Response, int], Tuple[GroupsIdMembershipsGet200Response, int, Dict[str, str]]
    """
    return 'do some magic!'


def groups_id_memberships_membership_id_delete(id, membership_id):  # noqa: E501
    """Deletes a GroupMembership object

     # noqa: E501

    :param id: 
    :type id: str
    :type id: str
    :param membership_id: 
    :type membership_id: str
    :type membership_id: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def groups_id_memberships_membership_id_get(id, membership_id):  # noqa: E501
    """Gets a GroupMembership object by id

     # noqa: E501

    :param id: 
    :type id: str
    :type id: str
    :param membership_id: 
    :type membership_id: str
    :type membership_id: str

    :rtype: Union[GroupsIdMembershipsPost201Response, Tuple[GroupsIdMembershipsPost201Response, int], Tuple[GroupsIdMembershipsPost201Response, int, Dict[str, str]]
    """
    return 'do some magic!'


def groups_id_memberships_post(id, new_group_membership=None):  # noqa: E501
    """Creates a new GroupMembership object

     # noqa: E501

    :param id: 
    :type id: str
    :type id: str
    :param new_group_membership: 
    :type new_group_membership: dict | bytes

    :rtype: Union[GroupsIdMembershipsPost201Response, Tuple[GroupsIdMembershipsPost201Response, int], Tuple[GroupsIdMembershipsPost201Response, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        new_group_membership = NewGroupMembership.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def groups_id_put(id, update_group=None):  # noqa: E501
    """Updates a Group object

     # noqa: E501

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


def groups_post(new_group=None):  # noqa: E501
    """groups_post

     # noqa: E501

    :param new_group: 
    :type new_group: dict | bytes

    :rtype: Union[GroupsPost201Response, Tuple[GroupsPost201Response, int], Tuple[GroupsPost201Response, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        new_group = NewGroup.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
