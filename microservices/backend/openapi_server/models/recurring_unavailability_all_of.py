# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
import re
from openapi_server import util

import re  # noqa: E501

class RecurringUnavailabilityAllOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None):  # noqa: E501
        """RecurringUnavailabilityAllOf - a model defined in OpenAPI

        :param id: The id of this RecurringUnavailabilityAllOf.  # noqa: E501
        :type id: str
        """
        self.openapi_types = {
            'id': str
        }

        self.attribute_map = {
            'id': 'id'
        }

        self._id = id

    @classmethod
    def from_dict(cls, dikt) -> 'RecurringUnavailabilityAllOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The recurringUnavailability_allOf of this RecurringUnavailabilityAllOf.  # noqa: E501
        :rtype: RecurringUnavailabilityAllOf
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this RecurringUnavailabilityAllOf.

        the id of an unavailability. this is a uuid with the prefix \"unavailability-\".   # noqa: E501

        :return: The id of this RecurringUnavailabilityAllOf.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RecurringUnavailabilityAllOf.

        the id of an unavailability. this is a uuid with the prefix \"unavailability-\".   # noqa: E501

        :param id: The id of this RecurringUnavailabilityAllOf.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        if id is not None and not re.search(r'^[a-z]+-[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$', id):  # noqa: E501
            raise ValueError("Invalid value for `id`, must be a follow pattern or equal to `/^[a-z]+-[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/`")  # noqa: E501

        self._id = id