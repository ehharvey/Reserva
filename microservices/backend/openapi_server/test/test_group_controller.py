# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.groups_get200_response import GroupsGet200Response  # noqa: E501
from openapi_server.models.groups_id_memberships_get200_response import GroupsIdMembershipsGet200Response  # noqa: E501
from openapi_server.models.groups_id_memberships_post201_response import GroupsIdMembershipsPost201Response  # noqa: E501
from openapi_server.models.groups_post201_response import GroupsPost201Response  # noqa: E501
from openapi_server.models.new_group import NewGroup  # noqa: E501
from openapi_server.models.new_group_membership import NewGroupMembership  # noqa: E501
from openapi_server.models.update_group import UpdateGroup  # noqa: E501
from openapi_server.test import BaseTestCase


class TestGroupController(BaseTestCase):
    """GroupController integration test stubs"""

    def test_groups_get(self):
        """Test case for groups_get

        Gets a list of Group objects
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/groups',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_groups_id_delete(self):
        """Test case for groups_id_delete

        Deletes a Group object
        """
        headers = { 
        }
        response = self.client.open(
            '/groups/{id}'.format(id='id_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_groups_id_get(self):
        """Test case for groups_id_get

        Gets a Group object by id
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/groups/{id}'.format(id='id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_groups_id_memberships_get(self):
        """Test case for groups_id_memberships_get

        Gets a list of GroupMembership objects
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/groups/{id}/memberships'.format(id='id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_groups_id_memberships_membership_id_delete(self):
        """Test case for groups_id_memberships_membership_id_delete

        Deletes a GroupMembership object
        """
        headers = { 
        }
        response = self.client.open(
            '/groups/{id}/memberships/{membership_id}'.format(id='id_example', membership_id='membership_id_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_groups_id_memberships_membership_id_get(self):
        """Test case for groups_id_memberships_membership_id_get

        Gets a GroupMembership object by id
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/groups/{id}/memberships/{membership_id}'.format(id='id_example', membership_id='membership_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_groups_id_memberships_post(self):
        """Test case for groups_id_memberships_post

        Creates a new GroupMembership object
        """
        new_group_membership = {"user":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","group":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
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

        Updates a Group object
        """
        update_group = {"createdBy":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","name":"Project Group"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
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

        
        """
        new_group = null
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
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
