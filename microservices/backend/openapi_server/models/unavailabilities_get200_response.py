# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.unavailability import Unavailability
from openapi_server import util

from openapi_server.models.unavailability import Unavailability  # noqa: E501

class UnavailabilitiesGet200Response(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, unavailabilities=None):  # noqa: E501
        """UnavailabilitiesGet200Response - a model defined in OpenAPI

        :param unavailabilities: The unavailabilities of this UnavailabilitiesGet200Response.  # noqa: E501
        :type unavailabilities: List[Unavailability]
        """
        self.openapi_types = {
            'unavailabilities': List[Unavailability]
        }

        self.attribute_map = {
            'unavailabilities': 'unavailabilities'
        }

        self._unavailabilities = unavailabilities

    @classmethod
    def from_dict(cls, dikt) -> 'UnavailabilitiesGet200Response':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The _unavailabilities_get_200_response of this UnavailabilitiesGet200Response.  # noqa: E501
        :rtype: UnavailabilitiesGet200Response
        """
        return util.deserialize_model(dikt, cls)

    @property
    def unavailabilities(self):
        """Gets the unavailabilities of this UnavailabilitiesGet200Response.


        :return: The unavailabilities of this UnavailabilitiesGet200Response.
        :rtype: List[Unavailability]
        """
        return self._unavailabilities

    @unavailabilities.setter
    def unavailabilities(self, unavailabilities):
        """Sets the unavailabilities of this UnavailabilitiesGet200Response.


        :param unavailabilities: The unavailabilities of this UnavailabilitiesGet200Response.
        :type unavailabilities: List[Unavailability]
        """

        self._unavailabilities = unavailabilities