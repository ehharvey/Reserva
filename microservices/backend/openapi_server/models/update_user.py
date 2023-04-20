# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class UpdateUser(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, username=None, email=None, password=None):  # noqa: E501
        """UpdateUser - a model defined in OpenAPI

        :param username: The username of this UpdateUser.  # noqa: E501
        :type username: str
        :param email: The email of this UpdateUser.  # noqa: E501
        :type email: str
        :param password: The password of this UpdateUser.  # noqa: E501
        :type password: str
        """
        self.openapi_types = {
            'username': str,
            'email': str,
            'password': str
        }

        self.attribute_map = {
            'username': 'username',
            'email': 'email',
            'password': 'password'
        }

        self._username = username
        self._email = email
        self._password = password

    @classmethod
    def from_dict(cls, dikt) -> 'UpdateUser':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The UpdateUser of this UpdateUser.  # noqa: E501
        :rtype: UpdateUser
        """
        return util.deserialize_model(dikt, cls)

    @property
    def username(self):
        """Gets the username of this UpdateUser.

        The user's username.  # noqa: E501

        :return: The username of this UpdateUser.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this UpdateUser.

        The user's username.  # noqa: E501

        :param username: The username of this UpdateUser.
        :type username: str
        """

        self._username = username

    @property
    def email(self):
        """Gets the email of this UpdateUser.

        The user's email address.  # noqa: E501

        :return: The email of this UpdateUser.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UpdateUser.

        The user's email address.  # noqa: E501

        :param email: The email of this UpdateUser.
        :type email: str
        """

        self._email = email

    @property
    def password(self):
        """Gets the password of this UpdateUser.

        The user's password.  # noqa: E501

        :return: The password of this UpdateUser.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this UpdateUser.

        The user's password.  # noqa: E501

        :param password: The password of this UpdateUser.
        :type password: str
        """

        self._password = password
