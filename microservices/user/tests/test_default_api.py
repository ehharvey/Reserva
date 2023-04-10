# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.new_user import NewUser  # noqa: F401
from openapi_server.models.update_user import UpdateUser  # noqa: F401
from openapi_server.models.user import User  # noqa: F401
from openapi_server.models.users_user_id_groups_get200_response import UsersUserIdGroupsGet200Response  # noqa: F401


def test_users_admins_get(client: TestClient):
    """Test case for users_admins_get

    Get all admin users
    """

    headers = {
    }
    response = client.request(
        "GET",
        "/users/admins",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_users_admins_post(client: TestClient):
    """Test case for users_admins_post

    Create a new admin user
    """
    new_user = null

    headers = {
    }
    response = client.request(
        "POST",
        "/users/admins",
        headers=headers,
        json=new_user,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_users_get(client: TestClient):
    """Test case for users_get

    Get all users
    """

    headers = {
    }
    response = client.request(
        "GET",
        "/users",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_users_post(client: TestClient):
    """Test case for users_post

    Create a new user
    """
    new_user = null

    headers = {
    }
    response = client.request(
        "POST",
        "/users",
        headers=headers,
        json=new_user,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_users_standard_get(client: TestClient):
    """Test case for users_standard_get

    Get all standard users
    """

    headers = {
    }
    response = client.request(
        "GET",
        "/users/standard",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_users_standard_post(client: TestClient):
    """Test case for users_standard_post

    Create a new standard user
    """
    new_user = null

    headers = {
    }
    response = client.request(
        "POST",
        "/users/standard",
        headers=headers,
        json=new_user,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_users_user_id_delete(client: TestClient):
    """Test case for users_user_id_delete

    Delete a user by ID
    """

    headers = {
    }
    response = client.request(
        "DELETE",
        "/users/{userId}".format(userId=56),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_users_user_id_get(client: TestClient):
    """Test case for users_user_id_get

    Get a user by ID
    """

    headers = {
    }
    response = client.request(
        "GET",
        "/users/{userId}".format(userId=56),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_users_user_id_groups_get(client: TestClient):
    """Test case for users_user_id_groups_get

    Get all groups for a user
    """

    headers = {
    }
    response = client.request(
        "GET",
        "/users/{userId}/groups".format(userId=56),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_users_user_id_put(client: TestClient):
    """Test case for users_user_id_put

    Update a user by ID
    """
    update_user = {"password":"password","email":"email","username":"username"}

    headers = {
    }
    response = client.request(
        "PUT",
        "/users/{userId}".format(userId=56),
        headers=headers,
        json=update_user,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

