# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.item import Item  # noqa: E501
from openapi_server.models.items_get200_response import ItemsGet200Response  # noqa: E501
from openapi_server.models.items_id_put200_response import ItemsIdPut200Response  # noqa: E501
from openapi_server.models.items_post201_response import ItemsPost201Response  # noqa: E501
from openapi_server.models.new_item import NewItem  # noqa: E501
from openapi_server.test import BaseTestCase


class TestItemController(BaseTestCase):
    """ItemController integration test stubs"""

    def test_delete_room_id(self):
        """Test case for delete_room_id

        Delete a Room object existing in the Rooms resources
        """
        headers = { 
        }
        response = self.client.open(
            '/items/{id}'.format(id=56),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_items_get(self):
        """Test case for items_get

        Gets a list of items. For now, the only kind of item is a room.
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/items',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_items_id_get(self):
        """Test case for items_id_get

        Gets a Item object by id. For now, the only kind of item is a room.
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/items/{id}'.format(id='id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_items_id_put(self):
        """Test case for items_id_put

        Updates an item. For now, the only kind of item is a room.
        """
        item = null
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/items/{id}'.format(id=56),
            method='PUT',
            headers=headers,
            data=json.dumps(item),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_items_post(self):
        """Test case for items_post

        Posts an item. For now, the only kind of item is a room.
        """
        new_item = null
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
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
