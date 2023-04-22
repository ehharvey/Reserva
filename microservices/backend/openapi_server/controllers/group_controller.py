from bson import ObjectId
import connexion
from pymongo import MongoClient
import six
from typing import Dict
from typing import Tuple
from typing import Union
from openapi_server.models.user import User
from openapi_server.user_utils import get_user_details

from openapi_server.models.group_membership import GroupMembership
from openapi_server.models.group_memberships_post201_response import GroupMembershipsPost201Response  # noqa: E501
from openapi_server.models.groups_id_unavailabilities_get200_response import GroupsIdUnavailabilitiesGet200Response  # noqa: E501
from openapi_server.models.groups_id_users_get200_response import GroupsIdUsersGet200Response  # noqa: E501
from openapi_server.models.groups_post201_response import GroupsPost201Response  # noqa: E501
from openapi_server.models.new_group import NewGroup  # noqa: E501
from openapi_server.models.new_group_membership import NewGroupMembership  # noqa: E501
from openapi_server.models.update_group import UpdateGroup  # noqa: E501
from openapi_server import util
from openapi_server.db_utils import create_group, create_group_membership, get_group, get_group_membership, get_model_from_mongo


def group_memberships_post(client: MongoClient, new_group_membership=None):  # noqa: E501
    """creates a new groupMembership object

    creates a new groupMembership object. Only the group owner can create a membership. (After a user becomes a member, they can delete their own membership.)  # noqa: E501

    :param new_group_membership: 
    :type new_group_membership: dict | bytes

    :rtype: Union[GroupMembershipsPost201Response, Tuple[GroupMembershipsPost201Response, int], Tuple[GroupMembershipsPost201Response, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        new_group_membership = NewGroupMembership.from_dict(connexion.request.get_json())  # noqa: E501

        result = create_group_membership(new_group_membership, client)

        return GroupMembershipsPost201Response(result), 201
    else:
        return "Invalid request", 400


def groups_id_delete(id, client: MongoClient):  # noqa: E501
    """deletes a group object.  Also deletes all groupMembership objects associated with the group. 

    deletes a group object # noqa: E501

    :param id: 
    :type id: str
    :type id: str

    :rtype: Union[GroupsPost201Response, Tuple[GroupsPost201Response, int], Tuple[GroupsPost201Response, int, Dict[str, str]]
    """
    
    db = client["main"]
    groups = db["groups"]
    group_memberships = db["group_memberships"]

    group = groups.find_one({"_id": id})
    if group is None:
        return "Group not found", 404

    group_memberships.delete_many({"group_id": id})
    groups.delete_one({"_id": id})

    return "Group deleted", 204

@get_user_details
def groups_memberships_id_delete(user_details: User, membership_id, client: MongoClient):  # noqa: E501
    """deletes a groupMembership object

    deletes a groupMembership object.  The group owner can delete any membership. A user can delete their own membership.  # noqa: E501

    :param membership_id: 
    :type membership_id: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """

    # Get group membership
    group_membership = get_group_membership(membership_id, client)

    # Get associated group
    group = get_group(group_membership.group, client)

    # Delete if group_membership has user
    if group_membership.user == user_details.id or group.owner == user_details.id:
        client["main"]["group_memberships"].delete_one({"_id": ObjectId(membership_id)})
        return "Group membership deleted", 204
    else:
        return "Unauthorized", 401


@get_user_details
def groups_id_put(user_details: User, client: MongoClient, id, update_group=None):  # noqa: E501
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

        # Get group
        group = get_group(id, client)

        # Check if user is owner
        if group.owner == user_details.id:
            # Update group
            client["main"]["groups"].update_one({"_id": ObjectId(id)}, {"$set": update_group.to_dict()})
            return "Group updated", 204
        else:
            return "Unauthorized", 401
    else:
        return "Invalid request", 400

@get_user_details
def groups_id_unavailabilities_get(user_details: User, client: MongoClient, id):  # noqa: E501
    """gets a list of unavailability objects

    gets a list of unavailability objects for a group # noqa: E501

    :param id: 
    :type id: str
    :type id: str

    :rtype: Union[GroupsIdUnavailabilitiesGet200Response, Tuple[GroupsIdUnavailabilitiesGet200Response, int], Tuple[GroupsIdUnavailabilitiesGet200Response, int, Dict[str, str]]
    """


    # Get associated group memberships
    group_memberships = [ g for g in client["main"]["group_memberships"].find({"group": ObjectId(id)}) ]


    if not group_memberships:
        return "Group not found", 404

    # Check if user is member
    if user_details.id in [group_membership["user"] for group_membership in group_memberships]:
        # Get associated unavailabilities
        unavailabilities = client["main"]["unavailabilities"].find({"owner": ObjectId(id)})
        return GroupsIdUnavailabilitiesGet200Response(
            [get_model_from_mongo(unavailability) for unavailability in unavailabilities]
        ), 200
    else:
        return "Unauthorized", 401
    
@get_user_details
def groups_id_users_get(user_details: User, client: MongoClient, id):  # noqa: E501
    """gets a list of user objects

    gets a list of user objects for a group # noqa: E501

    :param id: 
    :type id: str
    :type id: str

    :rtype: Union[GroupsIdUsersGet200Response, Tuple[GroupsIdUsersGet200Response, int], Tuple[GroupsIdUsersGet200Response, int, Dict[str, str]]
    """
    # Get associated group memberships
    group_memberships = client["main"]["group_memberships"].find({"group": ObjectId(id)})

    # Get associated users
    users = client["main"]["users"].find({"_id": {"$in": [group_membership["user"] for group_membership in group_memberships]}})

    # If user is member, return users
    if user_details.id in [group_membership["user"] for group_membership in group_memberships]:
        return GroupsIdUsersGet200Response(
            [get_model_from_mongo(user) for user in users]
        ), 200
    else:
        return "Unauthorized", 401


def groups_post(new_group=None):  # noqa: E501
    """creates a new group object

    creates a new group object # noqa: E501

    :param new_group: 
    :type new_group: dict | bytes

    :rtype: Union[GroupsPost201Response, Tuple[GroupsPost201Response, int], Tuple[GroupsPost201Response, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        new_group = NewGroup.from_dict(connexion.request.get_json())  # noqa: E501
        
        # Create group
        group = create_group(new_group)

        return GroupsPost201Response(group), 201
    else:
        return "Invalid request", 400
