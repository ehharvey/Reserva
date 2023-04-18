# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.unavailabilities_get200_response import UnavailabilitiesGet200Response  # noqa: E501
from openapi_server.models.unavailabilities_id_delete200_response import UnavailabilitiesIdDelete200Response  # noqa: E501
from openapi_server.models.unavailabilities_id_put200_response import UnavailabilitiesIdPut200Response  # noqa: E501
from openapi_server.models.unavailabilities_id_put400_response import UnavailabilitiesIdPut400Response  # noqa: E501
from openapi_server.models.unavailabilities_post201_response import UnavailabilitiesPost201Response  # noqa: E501
from openapi_server.models.unavailabilities_post400_response import UnavailabilitiesPost400Response  # noqa: E501
from openapi_server.models.unavailabilities_post_request import UnavailabilitiesPostRequest  # noqa: E501
from openapi_server.test import BaseTestCase


class TestUnavailabilityController(BaseTestCase):
    """UnavailabilityController integration test stubs"""

    def test_unavailabilities_get(self):
        """Test case for unavailabilities_get

        Get a list of unavailabilities
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/unavailabilities',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_unavailabilities_id_delete(self):
        """Test case for unavailabilities_id_delete

        Delete an unavailability
        """
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/unavailabilities/{id}'.format(id='id_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_unavailabilities_id_put(self):
        """Test case for unavailabilities_id_put

        update an unavailability
        """
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/unavailabilities/{id}'.format(id='id_example'),
            method='PUT',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_unavailabilities_post(self):
        """Test case for unavailabilities_post

        Create a new unavailability
        """
        unavailabilities_post_request = openapi_server.UnavailabilitiesPostRequest()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/unavailabilities',
            method='POST',
            headers=headers,
            data=json.dumps(unavailabilities_post_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
