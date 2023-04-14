# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
import re
from openapi_server import util

import re  # noqa: E501

class User(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, username=None, email=None, password=None, role='user', id=None, created_at=None, last_updated_at=None):  # noqa: E501
        """User - a model defined in OpenAPI

        :param username: The username of this User.  # noqa: E501
        :type username: str
        :param email: The email of this User.  # noqa: E501
        :type email: str
        :param password: The password of this User.  # noqa: E501
        :type password: str
        :param role: The role of this User.  # noqa: E501
        :type role: str
        :param id: The id of this User.  # noqa: E501
        :type id: str
        :param created_at: The created_at of this User.  # noqa: E501
        :type created_at: datetime
        :param last_updated_at: The last_updated_at of this User.  # noqa: E501
        :type last_updated_at: datetime
        """
        self.openapi_types = {
            'username': str,
            'email': str,
            'password': str,
            'role': str,
            'id': str,
            'created_at': datetime,
            'last_updated_at': datetime
        }

        self.attribute_map = {
            'username': 'username',
            'email': 'email',
            'password': 'password',
            'role': 'role',
            'id': 'id',
            'created_at': 'createdAt',
            'last_updated_at': 'lastUpdatedAt'
        }

        self._username = username
        self._email = email
        self._password = password
        self._role = role
        self._id = id
        self._created_at = created_at
        self._last_updated_at = last_updated_at

    @classmethod
    def from_dict(cls, dikt) -> 'User':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The User of this User.  # noqa: E501
        :rtype: User
        """
        return util.deserialize_model(dikt, cls)

    @property
    def username(self):
        """Gets the username of this User.

        The user's username.  # noqa: E501

        :return: The username of this User.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this User.

        The user's username.  # noqa: E501

        :param username: The username of this User.
        :type username: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

    @property
    def email(self):
        """Gets the email of this User.

        The user's email address.  # noqa: E501

        :return: The email of this User.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this User.

        The user's email address.  # noqa: E501

        :param email: The email of this User.
        :type email: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def password(self):
        """Gets the password of this User.

        The user's password.  # noqa: E501

        :return: The password of this User.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this User.

        The user's password.  # noqa: E501

        :param password: The password of this User.
        :type password: str
        """
        if password is None:
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501

        self._password = password

    @property
    def role(self):
        """Gets the role of this User.

        The user's role.  # noqa: E501

        :return: The role of this User.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this User.

        The user's role.  # noqa: E501

        :param role: The role of this User.
        :type role: str
        """
        allowed_values = ["standard", "admin"]  # noqa: E501
        if role not in allowed_values:
            raise ValueError(
                "Invalid value for `role` ({0}), must be one of {1}"
                .format(role, allowed_values)
            )

        self._role = role

    @property
    def id(self):
        """Gets the id of this User.

        Id of a user. This is a UUID with the prefix \"user-\".   # noqa: E501

        :return: The id of this User.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this User.

        Id of a user. This is a UUID with the prefix \"user-\".   # noqa: E501

        :param id: The id of this User.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        if id is not None and not re.search(r'^[a-z]+-[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$', id):  # noqa: E501
            raise ValueError("Invalid value for `id`, must be a follow pattern or equal to `/^[a-z]+-[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/`")  # noqa: E501

        self._id = id

    @property
    def created_at(self):
        """Gets the created_at of this User.

        The date and time the user was created.  # noqa: E501

        :return: The created_at of this User.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this User.

        The date and time the user was created.  # noqa: E501

        :param created_at: The created_at of this User.
        :type created_at: datetime
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def last_updated_at(self):
        """Gets the last_updated_at of this User.

        The date and time the user was last updated.  # noqa: E501

        :return: The last_updated_at of this User.
        :rtype: datetime
        """
        return self._last_updated_at

    @last_updated_at.setter
    def last_updated_at(self, last_updated_at):
        """Sets the last_updated_at of this User.

        The date and time the user was last updated.  # noqa: E501

        :param last_updated_at: The last_updated_at of this User.
        :type last_updated_at: datetime
        """
        if last_updated_at is None:
            raise ValueError("Invalid value for `last_updated_at`, must not be `None`")  # noqa: E501

        self._last_updated_at = last_updated_at