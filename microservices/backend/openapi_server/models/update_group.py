# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
import re
from openapi_server import util

import re  # noqa: E501

class UpdateGroup(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name=None, created_by=None):  # noqa: E501
        """UpdateGroup - a model defined in OpenAPI

        :param name: The name of this UpdateGroup.  # noqa: E501
        :type name: str
        :param created_by: The created_by of this UpdateGroup.  # noqa: E501
        :type created_by: str
        """
        self.openapi_types = {
            'name': str,
            'created_by': str
        }

        self.attribute_map = {
            'name': 'name',
            'created_by': 'createdBy'
        }

        self._name = name
        self._created_by = created_by

    @classmethod
    def from_dict(cls, dikt) -> 'UpdateGroup':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The updateGroup of this UpdateGroup.  # noqa: E501
        :rtype: UpdateGroup
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this UpdateGroup.

        the name of the group.  # noqa: E501

        :return: The name of this UpdateGroup.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateGroup.

        the name of the group.  # noqa: E501

        :param name: The name of this UpdateGroup.
        :type name: str
        """

        self._name = name

    @property
    def created_by(self):
        """Gets the created_by of this UpdateGroup.

        id of a user. this is a uuid with the prefix \"user-\".   # noqa: E501

        :return: The created_by of this UpdateGroup.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this UpdateGroup.

        id of a user. this is a uuid with the prefix \"user-\".   # noqa: E501

        :param created_by: The created_by of this UpdateGroup.
        :type created_by: str
        """
        if created_by is not None and not re.search(r'^[a-z]+-[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$', created_by):  # noqa: E501
            raise ValueError("Invalid value for `created_by`, must be a follow pattern or equal to `/^[a-z]+-[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/`")  # noqa: E501

        self._created_by = created_by