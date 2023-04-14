# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class NewCredit(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, user_id=None, amount=None):  # noqa: E501
        """NewCredit - a model defined in OpenAPI

        :param user_id: The user_id of this NewCredit.  # noqa: E501
        :type user_id: int
        :param amount: The amount of this NewCredit.  # noqa: E501
        :type amount: int
        """
        self.openapi_types = {
            'user_id': int,
            'amount': int
        }

        self.attribute_map = {
            'user_id': 'user_id',
            'amount': 'amount'
        }

        self._user_id = user_id
        self._amount = amount

    @classmethod
    def from_dict(cls, dikt) -> 'NewCredit':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The NewCredit of this NewCredit.  # noqa: E501
        :rtype: NewCredit
        """
        return util.deserialize_model(dikt, cls)

    @property
    def user_id(self):
        """Gets the user_id of this NewCredit.

        The ID of the user to create the credit for.  # noqa: E501

        :return: The user_id of this NewCredit.
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this NewCredit.

        The ID of the user to create the credit for.  # noqa: E501

        :param user_id: The user_id of this NewCredit.
        :type user_id: int
        """
        if user_id is None:
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def amount(self):
        """Gets the amount of this NewCredit.

        The amount of the credit to create in units.  # noqa: E501

        :return: The amount of this NewCredit.
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this NewCredit.

        The amount of the credit to create in units.  # noqa: E501

        :param amount: The amount of this NewCredit.
        :type amount: int
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount