# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.item import Item
from openapi_server import util

from openapi_server.models.item import Item  # noqa: E501

class ItemsGet200Response(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, rooms=None):  # noqa: E501
        """ItemsGet200Response - a model defined in OpenAPI

        :param rooms: The rooms of this ItemsGet200Response.  # noqa: E501
        :type rooms: List[Item]
        """
        self.openapi_types = {
            'rooms': List[Item]
        }

        self.attribute_map = {
            'rooms': 'rooms'
        }

        self._rooms = rooms

    @classmethod
    def from_dict(cls, dikt) -> 'ItemsGet200Response':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The _items_get_200_response of this ItemsGet200Response.  # noqa: E501
        :rtype: ItemsGet200Response
        """
        return util.deserialize_model(dikt, cls)

    @property
    def rooms(self):
        """Gets the rooms of this ItemsGet200Response.


        :return: The rooms of this ItemsGet200Response.
        :rtype: List[Item]
        """
        return self._rooms

    @rooms.setter
    def rooms(self, rooms):
        """Sets the rooms of this ItemsGet200Response.


        :param rooms: The rooms of this ItemsGet200Response.
        :type rooms: List[Item]
        """

        self._rooms = rooms
