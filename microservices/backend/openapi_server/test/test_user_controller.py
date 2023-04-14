# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.new_user import NewUser  # noqa: E501
from openapi_server.models.update_user import UpdateUser  # noqa: E501
from openapi_server.models.user import User  # noqa: E501
from openapi_server.models.users_user_id_groups_get200_response import UsersUserIdGroupsGet200Response  # noqa: E501
from openapi_server.test import BaseTestCase


class TestUserController(BaseTestCase):
    """UserController integration test stubs"""

    def test_users_admins_get(self):
        """Test case for users_admins_get

        Get all admin users
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

    def test_users_admins_post(self):
        """Test case for users_admins_post

        Create a new admin user
        """
        new_user = null
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/users/admins',
            method='POST',
            headers=headers,
            data=json.dumps(new_user),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_users_get(self):
        """Test case for users_get

        Get all users
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

    def test_users_post(self):
        """Test case for users_post

        Create a new user
        """
        new_user = null
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/users',
            method='POST',
            headers=headers,
            data=json.dumps(new_user),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_users_standard_get(self):
        """Test case for users_standard_get

        Get all standard users
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

    def test_users_standard_post(self):
        """Test case for users_standard_post

        Create a new standard user
        """
        new_user = null
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/users/standard',
            method='POST',
            headers=headers,
            data=json.dumps(new_user),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_users_user_id_delete(self):
        """Test case for users_user_id_delete

        Delete a user by ID
        """
        headers = { 
        }
        response = self.client.open(
            '/users/{user_id}'.format(user_id=56),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_users_user_id_get(self):
        """Test case for users_user_id_get

        Get a user by ID
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

        Get all groups for a user
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

    def test_users_user_id_put(self):
        """Test case for users_user_id_put

        Update a user by ID
        """
        update_user = {"password":"password","email":"email","username":"username"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/users/{user_id}'.format(user_id=56),
            method='PUT',
            headers=headers,
            data=json.dumps(update_user),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
