# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.user import User  # noqa: E501
from openapi_server.models.users_get200_response import UsersGet200Response  # noqa: E501
from openapi_server.models.users_user_id_groups_get200_response import UsersUserIdGroupsGet200Response  # noqa: E501
from openapi_server.test import BaseTestCase


class TestUserController(BaseTestCase):
    """UserController integration test stubs"""

    def test_users_admins_get(self):
        """Test case for users_admins_get

        get all admin users
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/users/admins',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_users_get(self):
        """Test case for users_get

        get all users
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/users',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_users_standard_get(self):
        """Test case for users_standard_get

        get all standard users
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/users/standard',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_users_user_id_get(self):
        """Test case for users_user_id_get

        get a user by id
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/users/{user_id}'.format(user_id=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_users_user_id_groups_get(self):
        """Test case for users_user_id_groups_get

        get all groups for a user
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/users/{user_id}/groups'.format(user_id=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
