# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.feature import Feature
import re
from openapi_server import util

from openapi_server.models.feature import Feature  # noqa: E501
import re  # noqa: E501

class Item(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name=None, location=None, description=None, type=None, features=None, id=None, create_date=None, last_update_date=None, created_by=None):  # noqa: E501
        """Item - a model defined in OpenAPI

        :param name: The name of this Item.  # noqa: E501
        :type name: str
        :param location: The location of this Item.  # noqa: E501
        :type location: str
        :param description: The description of this Item.  # noqa: E501
        :type description: str
        :param type: The type of this Item.  # noqa: E501
        :type type: str
        :param features: The features of this Item.  # noqa: E501
        :type features: List[Feature]
        :param id: The id of this Item.  # noqa: E501
        :type id: str
        :param create_date: The create_date of this Item.  # noqa: E501
        :type create_date: datetime
        :param last_update_date: The last_update_date of this Item.  # noqa: E501
        :type last_update_date: datetime
        :param created_by: The created_by of this Item.  # noqa: E501
        :type created_by: str
        """
        self.openapi_types = {
            'name': str,
            'location': str,
            'description': str,
            'type': str,
            'features': List[Feature],
            'id': str,
            'create_date': datetime,
            'last_update_date': datetime,
            'created_by': str
        }

        self.attribute_map = {
            'name': 'name',
            'location': 'location',
            'description': 'description',
            'type': 'type',
            'features': 'features',
            'id': 'id',
            'create_date': 'createDate',
            'last_update_date': 'lastUpdateDate',
            'created_by': 'createdBy'
        }

        self._name = name
        self._location = location
        self._description = description
        self._type = type
        self._features = features
        self._id = id
        self._create_date = create_date
        self._last_update_date = last_update_date
        self._created_by = created_by

    @classmethod
    def from_dict(cls, dikt) -> 'Item':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The item of this Item.  # noqa: E501
        :rtype: Item
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this Item.

        the name of the item. for now, these will be names of rooms  # noqa: E501

        :return: The name of this Item.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Item.

        the name of the item. for now, these will be names of rooms  # noqa: E501

        :param name: The name of this Item.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def location(self):
        """Gets the location of this Item.

        the location of the item.  # noqa: E501

        :return: The location of this Item.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this Item.

        the location of the item.  # noqa: E501

        :param location: The location of this Item.
        :type location: str
        """
        if location is None:
            raise ValueError("Invalid value for `location`, must not be `None`")  # noqa: E501

        self._location = location

    @property
    def description(self):
        """Gets the description of this Item.

        a description of the item.  # noqa: E501

        :return: The description of this Item.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Item.

        a description of the item.  # noqa: E501

        :param description: The description of this Item.
        :type description: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def type(self):
        """Gets the type of this Item.

        the type of the item. for now, this will only be room.  # noqa: E501

        :return: The type of this Item.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Item.

        the type of the item. for now, this will only be room.  # noqa: E501

        :param type: The type of this Item.
        :type type: str
        """
        allowed_values = ["room"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def features(self):
        """Gets the features of this Item.

        the features of the item. for now, these will be the features of the room.   # noqa: E501

        :return: The features of this Item.
        :rtype: List[Feature]
        """
        return self._features

    @features.setter
    def features(self, features):
        """Sets the features of this Item.

        the features of the item. for now, these will be the features of the room.   # noqa: E501

        :param features: The features of this Item.
        :type features: List[Feature]
        """
        if features is None:
            raise ValueError("Invalid value for `features`, must not be `None`")  # noqa: E501

        self._features = features

    @property
    def id(self):
        """Gets the id of this Item.

        the id of the item. this is a uuid with a prefix of \"item-\".   # noqa: E501

        :return: The id of this Item.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Item.

        the id of the item. this is a uuid with a prefix of \"item-\".   # noqa: E501

        :param id: The id of this Item.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501  

        self._id = id

    @property
    def create_date(self):
        """Gets the create_date of this Item.

        the date and time the item was created.  # noqa: E501

        :return: The create_date of this Item.
        :rtype: datetime
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """Sets the create_date of this Item.

        the date and time the item was created.  # noqa: E501

        :param create_date: The create_date of this Item.
        :type create_date: datetime
        """
        if create_date is None:
            raise ValueError("Invalid value for `create_date`, must not be `None`")  # noqa: E501

        self._create_date = create_date

    @property
    def last_update_date(self):
        """Gets the last_update_date of this Item.

        the date and time the item was last updated.  # noqa: E501

        :return: The last_update_date of this Item.
        :rtype: datetime
        """
        return self._last_update_date

    @last_update_date.setter
    def last_update_date(self, last_update_date):
        """Sets the last_update_date of this Item.

        the date and time the item was last updated.  # noqa: E501

        :param last_update_date: The last_update_date of this Item.
        :type last_update_date: datetime
        """
        if last_update_date is None:
            raise ValueError("Invalid value for `last_update_date`, must not be `None`")  # noqa: E501

        self._last_update_date = last_update_date

    @property
    def created_by(self):
        """Gets the created_by of this Item.

        id of a user. This is just a string, since the user id is provided by the authentication provider. (in this case, auth0)   # noqa: E501

        :return: The created_by of this Item.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this Item.

        id of a user. This is just a string, since the user id is provided by the authentication provider. (in this case, auth0)   # noqa: E501

        :param created_by: The created_by of this Item.
        :type created_by: str
        """
        if created_by is None:
            raise ValueError("Invalid value for `created_by`, must not be `None`")  # noqa: E501

        self._created_by = created_by
