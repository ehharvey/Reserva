# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.new_recurring_unavailability import NewRecurringUnavailability
from openapi_server.models.new_unavailability import NewUnavailability
import re
from openapi_server import util

from openapi_server.models.new_recurring_unavailability import NewRecurringUnavailability  # noqa: E501
from openapi_server.models.new_unavailability import NewUnavailability  # noqa: E501
import re  # noqa: E501

class UnavailabilitiesPostRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, item=None, start_date_time=None, end_date_time=None, type=None, recurrence=None):  # noqa: E501
        """UnavailabilitiesPostRequest - a model defined in OpenAPI

        :param item: The item of this UnavailabilitiesPostRequest.  # noqa: E501
        :type item: str
        :param start_date_time: The start_date_time of this UnavailabilitiesPostRequest.  # noqa: E501
        :type start_date_time: str
        :param end_date_time: The end_date_time of this UnavailabilitiesPostRequest.  # noqa: E501
        :type end_date_time: str
        :param type: The type of this UnavailabilitiesPostRequest.  # noqa: E501
        :type type: str
        :param recurrence: The recurrence of this UnavailabilitiesPostRequest.  # noqa: E501
        :type recurrence: str
        """
        self.openapi_types = {
            'item': str,
            'start_date_time': str,
            'end_date_time': str,
            'type': str,
            'recurrence': str
        }

        self.attribute_map = {
            'item': 'item',
            'start_date_time': 'startDateTime',
            'end_date_time': 'endDateTime',
            'type': 'type',
            'recurrence': 'recurrence'
        }

        self._item = item
        self._start_date_time = start_date_time
        self._end_date_time = end_date_time
        self._type = type
        self._recurrence = recurrence

    @classmethod
    def from_dict(cls, dikt) -> 'UnavailabilitiesPostRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The _unavailabilities_post_request of this UnavailabilitiesPostRequest.  # noqa: E501
        :rtype: UnavailabilitiesPostRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def item(self):
        """Gets the item of this UnavailabilitiesPostRequest.

        The ID of the item. This is a UUID with a prefix of \"item-\".   # noqa: E501

        :return: The item of this UnavailabilitiesPostRequest.
        :rtype: str
        """
        return self._item

    @item.setter
    def item(self, item):
        """Sets the item of this UnavailabilitiesPostRequest.

        The ID of the item. This is a UUID with a prefix of \"item-\".   # noqa: E501

        :param item: The item of this UnavailabilitiesPostRequest.
        :type item: str
        """
        if item is None:
            raise ValueError("Invalid value for `item`, must not be `None`")  # noqa: E501
        if item is not None and not re.search(r'^[a-z]+-[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$', item):  # noqa: E501
            raise ValueError("Invalid value for `item`, must be a follow pattern or equal to `/^[a-z]+-[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/`")  # noqa: E501

        self._item = item

    @property
    def start_date_time(self):
        """Gets the start_date_time of this UnavailabilitiesPostRequest.

        Date-time string with 15-minute interval, e.g., 2023-04-02T12:00:00  # noqa: E501

        :return: The start_date_time of this UnavailabilitiesPostRequest.
        :rtype: str
        """
        return self._start_date_time

    @start_date_time.setter
    def start_date_time(self, start_date_time):
        """Sets the start_date_time of this UnavailabilitiesPostRequest.

        Date-time string with 15-minute interval, e.g., 2023-04-02T12:00:00  # noqa: E501

        :param start_date_time: The start_date_time of this UnavailabilitiesPostRequest.
        :type start_date_time: str
        """
        if start_date_time is None:
            raise ValueError("Invalid value for `start_date_time`, must not be `None`")  # noqa: E501
        if start_date_time is not None and not re.search(r'^[0-9]{4}-[0-9]{2}-[0-9]{2}T([01][0-9]|2[0-3]):(00|15|30|45):00$', start_date_time):  # noqa: E501
            raise ValueError("Invalid value for `start_date_time`, must be a follow pattern or equal to `/^[0-9]{4}-[0-9]{2}-[0-9]{2}T([01][0-9]|2[0-3]):(00|15|30|45):00$/`")  # noqa: E501

        self._start_date_time = start_date_time

    @property
    def end_date_time(self):
        """Gets the end_date_time of this UnavailabilitiesPostRequest.

        Date-time string with 15-minute interval, e.g., 2023-04-02T12:00:00  # noqa: E501

        :return: The end_date_time of this UnavailabilitiesPostRequest.
        :rtype: str
        """
        return self._end_date_time

    @end_date_time.setter
    def end_date_time(self, end_date_time):
        """Sets the end_date_time of this UnavailabilitiesPostRequest.

        Date-time string with 15-minute interval, e.g., 2023-04-02T12:00:00  # noqa: E501

        :param end_date_time: The end_date_time of this UnavailabilitiesPostRequest.
        :type end_date_time: str
        """
        if end_date_time is None:
            raise ValueError("Invalid value for `end_date_time`, must not be `None`")  # noqa: E501
        if end_date_time is not None and not re.search(r'^[0-9]{4}-[0-9]{2}-[0-9]{2}T([01][0-9]|2[0-3]):(00|15|30|45):00$', end_date_time):  # noqa: E501
            raise ValueError("Invalid value for `end_date_time`, must be a follow pattern or equal to `/^[0-9]{4}-[0-9]{2}-[0-9]{2}T([01][0-9]|2[0-3]):(00|15|30|45):00$/`")  # noqa: E501

        self._end_date_time = end_date_time

    @property
    def type(self):
        """Gets the type of this UnavailabilitiesPostRequest.


        :return: The type of this UnavailabilitiesPostRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this UnavailabilitiesPostRequest.


        :param type: The type of this UnavailabilitiesPostRequest.
        :type type: str
        """
        allowed_values = ["maintenance", "booking", "off_hours", "other"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def recurrence(self):
        """Gets the recurrence of this UnavailabilitiesPostRequest.

        Date-time string with 15-minute interval, e.g., 2023-04-02T12:00:00  # noqa: E501

        :return: The recurrence of this UnavailabilitiesPostRequest.
        :rtype: str
        """
        return self._recurrence

    @recurrence.setter
    def recurrence(self, recurrence):
        """Sets the recurrence of this UnavailabilitiesPostRequest.

        Date-time string with 15-minute interval, e.g., 2023-04-02T12:00:00  # noqa: E501

        :param recurrence: The recurrence of this UnavailabilitiesPostRequest.
        :type recurrence: str
        """
        if recurrence is None:
            raise ValueError("Invalid value for `recurrence`, must not be `None`")  # noqa: E501
        if recurrence is not None and not re.search(r'^[0-9]{4}-[0-9]{2}-[0-9]{2}T([01][0-9]|2[0-3]):(00|15|30|45):00$', recurrence):  # noqa: E501
            raise ValueError("Invalid value for `recurrence`, must be a follow pattern or equal to `/^[0-9]{4}-[0-9]{2}-[0-9]{2}T([01][0-9]|2[0-3]):(00|15|30|45):00$/`")  # noqa: E501

        self._recurrence = recurrence