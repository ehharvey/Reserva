# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.unavailability import Unavailability
from openapi_server import util

from openapi_server.models.unavailability import Unavailability  # noqa: E501

class UnavailabilitiesIdGet200Response(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, unavailability=None):  # noqa: E501
        """UnavailabilitiesIdGet200Response - a model defined in OpenAPI

        :param unavailability: The unavailability of this UnavailabilitiesIdGet200Response.  # noqa: E501
        :type unavailability: Unavailability
        """
        self.openapi_types = {
            'unavailability': Unavailability
        }

        self.attribute_map = {
            'unavailability': 'unavailability'
        }

        self._unavailability = unavailability

    @classmethod
    def from_dict(cls, dikt) -> 'UnavailabilitiesIdGet200Response':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The _unavailabilities__id__get_200_response of this UnavailabilitiesIdGet200Response.  # noqa: E501
        :rtype: UnavailabilitiesIdGet200Response
        """
        return util.deserialize_model(dikt, cls)

    @property
    def unavailability(self):
        """Gets the unavailability of this UnavailabilitiesIdGet200Response.


        :return: The unavailability of this UnavailabilitiesIdGet200Response.
        :rtype: Unavailability
        """
        return self._unavailability

    @unavailability.setter
    def unavailability(self, unavailability):
        """Sets the unavailability of this UnavailabilitiesIdGet200Response.


        :param unavailability: The unavailability of this UnavailabilitiesIdGet200Response.
        :type unavailability: Unavailability
        """

        self._unavailability = unavailability
