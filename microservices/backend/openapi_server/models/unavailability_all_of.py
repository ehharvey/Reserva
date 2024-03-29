# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
import re
from openapi_server import util

import re  # noqa: E501

class UnavailabilityAllOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, create_date=None, last_updated_date=None):  # noqa: E501
        """UnavailabilityAllOf - a model defined in OpenAPI

        :param id: The id of this UnavailabilityAllOf.  # noqa: E501
        :type id: str
        :param create_date: The create_date of this UnavailabilityAllOf.  # noqa: E501
        :type create_date: datetime
        :param last_updated_date: The last_updated_date of this UnavailabilityAllOf.  # noqa: E501
        :type last_updated_date: datetime
        """
        self.openapi_types = {
            'id': str,
            'create_date': datetime,
            'last_updated_date': datetime
        }

        self.attribute_map = {
            'id': 'id',
            'create_date': 'createDate',
            'last_updated_date': 'lastUpdatedDate'
        }

        self._id = id
        self._create_date = create_date
        self._last_updated_date = last_updated_date

    @classmethod
    def from_dict(cls, dikt) -> 'UnavailabilityAllOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The unavailability_allOf of this UnavailabilityAllOf.  # noqa: E501
        :rtype: UnavailabilityAllOf
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this UnavailabilityAllOf.

        the id of an unavailability. this is a uuid with the prefix \"unavailability-\".   # noqa: E501

        :return: The id of this UnavailabilityAllOf.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UnavailabilityAllOf.

        the id of an unavailability. this is a uuid with the prefix \"unavailability-\".   # noqa: E501

        :param id: The id of this UnavailabilityAllOf.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        

        self._id = id

    @property
    def create_date(self):
        """Gets the create_date of this UnavailabilityAllOf.

        the date and time the unavailability was created.  # noqa: E501

        :return: The create_date of this UnavailabilityAllOf.
        :rtype: datetime
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """Sets the create_date of this UnavailabilityAllOf.

        the date and time the unavailability was created.  # noqa: E501

        :param create_date: The create_date of this UnavailabilityAllOf.
        :type create_date: datetime
        """
        if create_date is None:
            raise ValueError("Invalid value for `create_date`, must not be `None`")  # noqa: E501

        self._create_date = create_date

    @property
    def last_updated_date(self):
        """Gets the last_updated_date of this UnavailabilityAllOf.

        the date and time the unavailability was last updated.  # noqa: E501

        :return: The last_updated_date of this UnavailabilityAllOf.
        :rtype: datetime
        """
        return self._last_updated_date

    @last_updated_date.setter
    def last_updated_date(self, last_updated_date):
        """Sets the last_updated_date of this UnavailabilityAllOf.

        the date and time the unavailability was last updated.  # noqa: E501

        :param last_updated_date: The last_updated_date of this UnavailabilityAllOf.
        :type last_updated_date: datetime
        """
        if last_updated_date is None:
            raise ValueError("Invalid value for `last_updated_date`, must not be `None`")  # noqa: E501

        self._last_updated_date = last_updated_date
