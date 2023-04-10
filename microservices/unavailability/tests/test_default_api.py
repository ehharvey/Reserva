# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.unavailabilities_get200_response import UnavailabilitiesGet200Response  # noqa: F401
from openapi_server.models.unavailabilities_id_delete200_response import UnavailabilitiesIdDelete200Response  # noqa: F401
from openapi_server.models.unavailabilities_id_get200_response import UnavailabilitiesIdGet200Response  # noqa: F401
from openapi_server.models.unavailabilities_id_get400_response import UnavailabilitiesIdGet400Response  # noqa: F401
from openapi_server.models.unavailabilities_id_put200_response import UnavailabilitiesIdPut200Response  # noqa: F401
from openapi_server.models.unavailabilities_post_request import UnavailabilitiesPostRequest  # noqa: F401


def test_unavailabilities_get(client: TestClient):
    """Test case for unavailabilities_get

    
    """

    headers = {
    }
    response = client.request(
        "GET",
        "/unavailabilities",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_unavailabilities_id_delete(client: TestClient):
    """Test case for unavailabilities_id_delete

    
    """

    headers = {
    }
    response = client.request(
        "DELETE",
        "/unavailabilities/{id}".format(id='id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_unavailabilities_id_get(client: TestClient):
    """Test case for unavailabilities_id_get

    
    """

    headers = {
    }
    response = client.request(
        "GET",
        "/unavailabilities/{id}".format(id='id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_unavailabilities_id_put(client: TestClient):
    """Test case for unavailabilities_id_put

    
    """

    headers = {
    }
    response = client.request(
        "PUT",
        "/unavailabilities/{id}".format(id='id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_unavailabilities_post(client: TestClient):
    """Test case for unavailabilities_post

    
    """
    unavailabilities_post_request = openapi_server.UnavailabilitiesPostRequest()

    headers = {
    }
    response = client.request(
        "POST",
        "/unavailabilities",
        headers=headers,
        json=unavailabilities_post_request,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

