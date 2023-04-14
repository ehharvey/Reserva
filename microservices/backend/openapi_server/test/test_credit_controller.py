# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.credit import Credit  # noqa: E501
from openapi_server.models.new_credit import NewCredit  # noqa: E501
from openapi_server.models.update_credit_by_id_request import UpdateCreditByIdRequest  # noqa: E501
from openapi_server.test import BaseTestCase


class TestCreditController(BaseTestCase):
    """CreditController integration test stubs"""

    def test_create_credit(self):
        """Test case for create_credit

        Create a new credit
        """
        new_credit = {"amount":6,"user_id":0}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/credits',
            method='POST',
            headers=headers,
            data=json.dumps(new_credit),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_credit_by_id(self):
        """Test case for delete_credit_by_id

        Delete a credit by ID
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/credits/{credit_id}'.format(credit_id=56),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_credit_by_id(self):
        """Test case for get_credit_by_id

        Get a credit by ID
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/credits/{credit_id}'.format(credit_id=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_credits(self):
        """Test case for get_credits

        Get all credits
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/credits',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_credit_by_id(self):
        """Test case for update_credit_by_id

        Update a credit by ID
        """
        update_credit_by_id_request = openapi_server.UpdateCreditByIdRequest()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/credits/{credit_id}'.format(credit_id=56),
            method='PATCH',
            headers=headers,
            data=json.dumps(update_credit_by_id_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
