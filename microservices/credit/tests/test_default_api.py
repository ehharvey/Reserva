# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.credit import Credit  # noqa: F401
from openapi_server.models.error import Error  # noqa: F401
from openapi_server.models.new_credit import NewCredit  # noqa: F401
from openapi_server.models.update_credit_by_id_request import UpdateCreditByIdRequest  # noqa: F401


def test_create_credit(client: TestClient):
    """Test case for create_credit

    Create a new credit
    """
    new_credit = {"amount":6,"user_id":0}

    headers = {
    }
    response = client.request(
        "POST",
        "/credits",
        headers=headers,
        json=new_credit,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_delete_credit_by_id(client: TestClient):
    """Test case for delete_credit_by_id

    Delete a credit by ID
    """

    headers = {
    }
    response = client.request(
        "DELETE",
        "/credits/{creditId}".format(creditId=56),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_credit_by_id(client: TestClient):
    """Test case for get_credit_by_id

    Get a credit by ID
    """

    headers = {
    }
    response = client.request(
        "GET",
        "/credits/{creditId}".format(creditId=56),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_credits(client: TestClient):
    """Test case for get_credits

    Get all credits
    """

    headers = {
    }
    response = client.request(
        "GET",
        "/credits",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_update_credit_by_id(client: TestClient):
    """Test case for update_credit_by_id

    Update a credit by ID
    """
    update_credit_by_id_request = openapi_server.UpdateCreditByIdRequest()

    headers = {
    }
    response = client.request(
        "PATCH",
        "/credits/{creditId}".format(creditId=56),
        headers=headers,
        json=update_credit_by_id_request,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

