# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.authentication_login_post201_response import AuthenticationLoginPost201Response  # noqa: F401
from openapi_server.models.authentication_login_post_request import AuthenticationLoginPostRequest  # noqa: F401


def test_authentication_login_post(client: TestClient):
    """Test case for authentication_login_post

    
    """
    authentication_login_post_request = openapi_server.AuthenticationLoginPostRequest()

    headers = {
    }
    response = client.request(
        "POST",
        "/authentication/login",
        headers=headers,
        json=authentication_login_post_request,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_authentication_logout_post(client: TestClient):
    """Test case for authentication_logout_post

    
    """
    authentication_login_post201_response = openapi_server.AuthenticationLoginPost201Response()

    headers = {
    }
    response = client.request(
        "POST",
        "/authentication/logout",
        headers=headers,
        json=authentication_login_post201_response,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_authentication_validate_put(client: TestClient):
    """Test case for authentication_validate_put

    
    """
    authentication_login_post201_response = openapi_server.AuthenticationLoginPost201Response()

    headers = {
    }
    response = client.request(
        "PUT",
        "/authentication/validate",
        headers=headers,
        json=authentication_login_post201_response,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

