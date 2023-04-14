# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
import re
from openapi_server import util

import re  # noqa: E501

class GroupAllOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, created_at=None, last_updated_at=None):  # noqa: E501
        """GroupAllOf - a model defined in OpenAPI

        :param id: The id of this GroupAllOf.  # noqa: E501
        :type id: str
        :param created_at: The created_at of this GroupAllOf.  # noqa: E501
        :type created_at: datetime
        :param last_updated_at: The last_updated_at of this GroupAllOf.  # noqa: E501
        :type last_updated_at: datetime
        """
        self.openapi_types = {
            'id': str,
            'created_at': datetime,
            'last_updated_at': datetime
        }

        self.attribute_map = {
            'id': 'id',
            'created_at': 'createdAt',
            'last_updated_at': 'lastUpdatedAt'
        }

        self._id = id
        self._created_at = created_at
        self._last_updated_at = last_updated_at

    @classmethod
    def from_dict(cls, dikt) -> 'GroupAllOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Group_allOf of this GroupAllOf.  # noqa: E501
        :rtype: GroupAllOf
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this GroupAllOf.

        The ID of a group. This is a UUID with the prefix \"group-\".   # noqa: E501

        :return: The id of this GroupAllOf.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GroupAllOf.

        The ID of a group. This is a UUID with the prefix \"group-\".   # noqa: E501

        :param id: The id of this GroupAllOf.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        if id is not None and not re.search(r'^[a-z]+-[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$', id):  # noqa: E501
            raise ValueError("Invalid value for `id`, must be a follow pattern or equal to `/^[a-z]+-[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/`")  # noqa: E501

        self._id = id

    @property
    def created_at(self):
        """Gets the created_at of this GroupAllOf.

        The date and time the group was created.  # noqa: E501

        :return: The created_at of this GroupAllOf.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this GroupAllOf.

        The date and time the group was created.  # noqa: E501

        :param created_at: The created_at of this GroupAllOf.
        :type created_at: datetime
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def last_updated_at(self):
        """Gets the last_updated_at of this GroupAllOf.

        The date and time the group was last updated.  # noqa: E501

        :return: The last_updated_at of this GroupAllOf.
        :rtype: datetime
        """
        return self._last_updated_at

    @last_updated_at.setter
    def last_updated_at(self, last_updated_at):
        """Sets the last_updated_at of this GroupAllOf.

        The date and time the group was last updated.  # noqa: E501

        :param last_updated_at: The last_updated_at of this GroupAllOf.
        :type last_updated_at: datetime
        """
        if last_updated_at is None:
            raise ValueError("Invalid value for `last_updated_at`, must not be `None`")  # noqa: E501

        self._last_updated_at = last_updated_at
