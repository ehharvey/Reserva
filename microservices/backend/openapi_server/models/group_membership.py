# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
import re
from openapi_server import util

import re  # noqa: E501

class GroupMembership(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, group=None, user=None, id=None):  # noqa: E501
        """GroupMembership - a model defined in OpenAPI

        :param group: The group of this GroupMembership.  # noqa: E501
        :type group: str
        :param user: The user of this GroupMembership.  # noqa: E501
        :type user: str
        :param id: The id of this GroupMembership.  # noqa: E501
        :type id: str
        """
        self.openapi_types = {
            'group': str,
            'user': str,
            'id': str
        }

        self.attribute_map = {
            'group': 'group',
            'user': 'user',
            'id': 'id'
        }

        self._group = group
        self._user = user
        self._id = id

    @classmethod
    def from_dict(cls, dikt) -> 'GroupMembership':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The groupMembership of this GroupMembership.  # noqa: E501
        :rtype: GroupMembership
        """
        return util.deserialize_model(dikt, cls)

    @property
    def group(self):
        """Gets the group of this GroupMembership.

        the id of a group. this is a uuid with the prefix \"group-\".   # noqa: E501

        :return: The group of this GroupMembership.
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this GroupMembership.

        the id of a group. this is a uuid with the prefix \"group-\".   # noqa: E501

        :param group: The group of this GroupMembership.
        :type group: str
        """
        if group is None:
            raise ValueError("Invalid value for `group`, must not be `None`")  # noqa: E501
        if group is not None and not re.search(r'^[a-z]+-[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$', group):  # noqa: E501
            raise ValueError("Invalid value for `group`, must be a follow pattern or equal to `/^[a-z]+-[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/`")  # noqa: E501

        self._group = group

    @property
    def user(self):
        """Gets the user of this GroupMembership.

        id of a user. This is just a string, since the user id is provided by the authentication provider. (in this case, auth0)   # noqa: E501

        :return: The user of this GroupMembership.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this GroupMembership.

        id of a user. This is just a string, since the user id is provided by the authentication provider. (in this case, auth0)   # noqa: E501

        :param user: The user of this GroupMembership.
        :type user: str
        """
        if user is None:
            raise ValueError("Invalid value for `user`, must not be `None`")  # noqa: E501

        self._user = user

    @property
    def id(self):
        """Gets the id of this GroupMembership.

        the id of a group membership.  # noqa: E501

        :return: The id of this GroupMembership.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GroupMembership.

        the id of a group membership.  # noqa: E501

        :param id: The id of this GroupMembership.
        :type id: str
        """
        if id is not None and not re.search(r'^[a-z]+-[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$', id):  # noqa: E501
            raise ValueError("Invalid value for `id`, must be a follow pattern or equal to `/^[a-z]+-[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/`")  # noqa: E501

        self._id = id
