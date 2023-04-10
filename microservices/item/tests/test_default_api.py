# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.items_get200_response import ItemsGet200Response  # noqa: F401
from openapi_server.models.items_id_get200_response import ItemsIdGet200Response  # noqa: F401
from openapi_server.models.items_id_put200_response import ItemsIdPut200Response  # noqa: F401
from openapi_server.models.update_item import UpdateItem  # noqa: F401


def test_delete_room_id(client: TestClient):
    """Test case for delete_room_id

    Delete a Room object existing in the Rooms resources
    """

    headers = {
    }
    response = client.request(
        "DELETE",
        "/items/{id}".format(id=None),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_items_get(client: TestClient):
    """Test case for items_get

    Gets a list of items. For now, the only kind of item is a room.
    """

    headers = {
    }
    response = client.request(
        "GET",
        "/items",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_items_id_get(client: TestClient):
    """Test case for items_id_get

    Gets a Item object by id. For now, the only kind of item is a room.
    """

    headers = {
    }
    response = client.request(
        "GET",
        "/items/{id}".format(id=None),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_items_id_put(client: TestClient):
    """Test case for items_id_put

    Updates an item. For now, the only kind of item is a room.
    """
    body = None

    headers = {
    }
    response = client.request(
        "PUT",
        "/items/{id}".format(id=None),
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_items_post(client: TestClient):
    """Test case for items_post

    Posts an item. For now, the only kind of item is a room.
    """
    body = {"features":[{"name":"Style","value":"Modern"},{"name":"Size","value":1000},{"name":"Has Windows","value":1}],"name":"Large Room","description":"Large Room with Low Ceilings","location":"1st Floor","type":"Room"}

    headers = {
    }
    response = client.request(
        "POST",
        "/items",
        headers=headers,
        json=body,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

