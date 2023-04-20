# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.groups_id_unavailabilities_get200_response import GroupsIdUnavailabilitiesGet200Response  # noqa: E501
from openapi_server.models.item import Item  # noqa: E501
from openapi_server.models.items_get200_response import ItemsGet200Response  # noqa: E501
from openapi_server.models.items_post201_response import ItemsPost201Response  # noqa: E501
from openapi_server.models.new_item import NewItem  # noqa: E501
from openapi_server.test import BaseTestCase


class TestItemController(BaseTestCase):
    """ItemController integration test stubs"""

    def test_items_get(self):
        """Test case for items_get

        gets a list of items. for now, the only kind of item is a room.
        """
        query_string = [('page', 1),
                        ('per_page', 10),
                        ('nameSearch', 'name_search_example'),
                        ('locationSearch', 'location_search_example'),
                        ('descriptionSearch', 'description_search_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/items',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_items_id_delete(self):
        """Test case for items_id_delete

        delete a room object
        """
        headers = { 
            'Authorization': 'Bearer special-key',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/items/{id}'.format(id=56),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_items_id_put(self):
        """Test case for items_id_put

        updates an item. for now, the only kind of item is a room.
        """
        item = openapi_server.Item()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/items/{id}'.format(id=56),
            method='PUT',
            headers=headers,
            data=json.dumps(item),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_items_id_unavailabilities_get(self):
        """Test case for items_id_unavailabilities_get

        gets a list of unavailabilities for a given item.
        """
        query_string = [('start', '2013-10-20T19:20:30+01:00'),
                        ('end', '2013-10-20T19:20:30+01:00'),
                        ('page', 1),
                        ('per_page', 10)]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/items/{id}/unavailabilities'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_items_post(self):
        """Test case for items_post

        posts an item. for now, the only kind of item is a room.
        """
        new_item = openapi_server.NewItem()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/items',
            method='POST',
            headers=headers,
            data=json.dumps(new_item),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
