# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.group_membership import GroupMembership
from openapi_server import util

from openapi_server.models.group_membership import GroupMembership  # noqa: E501

class UsersMeGroupsGet200Response(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, groups=None):  # noqa: E501
        """UsersMeGroupsGet200Response - a model defined in OpenAPI

        :param groups: The groups of this UsersMeGroupsGet200Response.  # noqa: E501
        :type groups: List[GroupMembership]
        """
        self.openapi_types = {
            'groups': List[GroupMembership]
        }

        self.attribute_map = {
            'groups': 'groups'
        }

        self._groups = groups

    @classmethod
    def from_dict(cls, dikt) -> 'UsersMeGroupsGet200Response':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The _users_me_groups_get_200_response of this UsersMeGroupsGet200Response.  # noqa: E501
        :rtype: UsersMeGroupsGet200Response
        """
        return util.deserialize_model(dikt, cls)

    @property
    def groups(self):
        """Gets the groups of this UsersMeGroupsGet200Response.


        :return: The groups of this UsersMeGroupsGet200Response.
        :rtype: List[GroupMembership]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this UsersMeGroupsGet200Response.


        :param groups: The groups of this UsersMeGroupsGet200Response.
        :type groups: List[GroupMembership]
        """

        self._groups = groups
