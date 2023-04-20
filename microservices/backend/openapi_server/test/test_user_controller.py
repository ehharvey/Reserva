# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.groups_id_unavailabilities_get200_response import GroupsIdUnavailabilitiesGet200Response  # noqa: E501
from openapi_server.models.groups_id_users_get200_response import GroupsIdUsersGet200Response  # noqa: E501
from openapi_server.models.users_me_get200_response import UsersMeGet200Response  # noqa: E501
from openapi_server.models.users_me_groups_get200_response import UsersMeGroupsGet200Response  # noqa: E501
from openapi_server.test import BaseTestCase


class TestUserController(BaseTestCase):
    """UserController integration test stubs"""

    def test_users_get(self):
        """Test case for users_get

        get all users
        """
        query_string = [('search', 'search_example'),
                        ('page', 1),
                        ('per_page', 10)]
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
            'Authorization': 'Bearer special-key',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/users',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_users_me_get(self):
        """Test case for users_me_get

        get the current user
        """
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
            'Authorization': 'Bearer special-key',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/users/me',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_users_me_groups_get(self):
        """Test case for users_me_groups_get

        get all groups for the current user
        """
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
            'Authorization': 'Bearer special-key',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/users/me/groups',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_users_me_unavailabilities_get(self):
        """Test case for users_me_unavailabilities_get

        get all unavailabilities for the current user
        """
        query_string = [('start', '2013-10-20T19:20:30+01:00'),
                        ('end', '2013-10-20T19:20:30+01:00')]
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
            'Authorization': 'Bearer special-key',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/users/me/unavailabilities',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
