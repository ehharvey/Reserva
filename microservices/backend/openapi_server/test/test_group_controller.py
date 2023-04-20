# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.group_memberships_post201_response import GroupMembershipsPost201Response  # noqa: E501
from openapi_server.models.groups_id_unavailabilities_get200_response import GroupsIdUnavailabilitiesGet200Response  # noqa: E501
from openapi_server.models.groups_id_users_get200_response import GroupsIdUsersGet200Response  # noqa: E501
from openapi_server.models.groups_post201_response import GroupsPost201Response  # noqa: E501
from openapi_server.models.new_group import NewGroup  # noqa: E501
from openapi_server.models.new_group_membership import NewGroupMembership  # noqa: E501
from openapi_server.models.update_group import UpdateGroup  # noqa: E501
from openapi_server.test import BaseTestCase


class TestGroupController(BaseTestCase):
    """GroupController integration test stubs"""

    def test_group_memberships_post(self):
        """Test case for group_memberships_post

        creates a new groupMembership object
        """
        new_group_membership = openapi_server.NewGroupMembership()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/groupMemberships',
            method='POST',
            headers=headers,
            data=json.dumps(new_group_membership),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_groups_id_delete(self):
        """Test case for groups_id_delete

        deletes a group object.  Also deletes all groupMembership objects associated with the group. 
        """
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/groups/{id}'.format(id='id_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_groups_id_memberships_membership_id_delete(self):
        """Test case for groups_id_memberships_membership_id_delete

        deletes a groupMembership object
        """
        headers = { 
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/groups/{id}/memberships/{membership_id}'.format(id='id_example', membership_id='membership_id_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_groups_id_put(self):
        """Test case for groups_id_put

        updates a group object
        """
        update_group = openapi_server.UpdateGroup()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/groups/{id}'.format(id='id_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(update_group),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_groups_id_unavailabilities_get(self):
        """Test case for groups_id_unavailabilities_get

        gets a list of unavailability objects
        """
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/groups/{id}/unavailabilities'.format(id='id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_groups_id_users_get(self):
        """Test case for groups_id_users_get

        gets a list of user objects
        """
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/groups/{id}/users'.format(id='id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_groups_post(self):
        """Test case for groups_post

        creates a new group object
        """
        new_group = openapi_server.NewGroup()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/groups',
            method='POST',
            headers=headers,
            data=json.dumps(new_group),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
