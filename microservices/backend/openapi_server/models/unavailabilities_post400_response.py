# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class UnavailabilitiesPost400Response(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, error=None):  # noqa: E501
        """UnavailabilitiesPost400Response - a model defined in OpenAPI

        :param error: The error of this UnavailabilitiesPost400Response.  # noqa: E501
        :type error: object
        """
        self.openapi_types = {
            'error': object
        }

        self.attribute_map = {
            'error': 'error'
        }

        self._error = error

    @classmethod
    def from_dict(cls, dikt) -> 'UnavailabilitiesPost400Response':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The _unavailabilities_post_400_response of this UnavailabilitiesPost400Response.  # noqa: E501
        :rtype: UnavailabilitiesPost400Response
        """
        return util.deserialize_model(dikt, cls)

    @property
    def error(self):
        """Gets the error of this UnavailabilitiesPost400Response.


        :return: The error of this UnavailabilitiesPost400Response.
        :rtype: object
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this UnavailabilitiesPost400Response.


        :param error: The error of this UnavailabilitiesPost400Response.
        :type error: object
        """

        self._error = error
