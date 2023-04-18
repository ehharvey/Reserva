# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.groups_id_memberships_get200_response import GroupsIdMembershipsGet200Response  # noqa: E501
from openapi_server.models.groups_id_memberships_post201_response import GroupsIdMembershipsPost201Response  # noqa: E501
from openapi_server.models.groups_post201_response import GroupsPost201Response  # noqa: E501
from openapi_server.models.new_group import NewGroup  # noqa: E501
from openapi_server.models.new_group_membership import NewGroupMembership  # noqa: E501
from openapi_server.models.update_group import UpdateGroup  # noqa: E501
from openapi_server.test import BaseTestCase


class TestGroupController(BaseTestCase):
    """GroupController integration test stubs"""

    def test_groups_id_delete(self):
        """Test case for groups_id_delete

        deletes a group object
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

    def test_groups_id_get(self):
        """Test case for groups_id_get

        gets a group object by id
        """
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/groups/{id}'.format(id='id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_groups_id_memberships_get(self):
        """Test case for groups_id_memberships_get

        gets a list of groupMembership objects
        """
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/groups/{id}/memberships'.format(id='id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_groups_id_memberships_membershipid_delete(self):
        """Test case for groups_id_memberships_membershipid_delete

        deletes a groupMembership object
        """
        headers = { 
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/groups/{id}/memberships/{membershipid}'.format(id='id_example', membershipid='membershipid_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_groups_id_memberships_membershipid_get(self):
        """Test case for groups_id_memberships_membershipid_get

        gets a groupMembership object by id
        """
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/groups/{id}/memberships/{membershipid}'.format(id='id_example', membershipid='membershipid_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_groups_id_memberships_post(self):
        """Test case for groups_id_memberships_post

        creates a new groupMembership object
        """
        new_group_membership = openapi_server.NewGroupMembership()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/groups/{id}/memberships'.format(id='id_example'),
            method='POST',
            headers=headers,
            data=json.dumps(new_group_membership),
            content_type='application/json')
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
