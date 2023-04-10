# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.groups_get200_response import GroupsGet200Response  # noqa: F401
from openapi_server.models.groups_id_get200_response import GroupsIdGet200Response  # noqa: F401
from openapi_server.models.groups_id_memberships_get200_response import GroupsIdMembershipsGet200Response  # noqa: F401
from openapi_server.models.groups_id_memberships_post201_response import GroupsIdMembershipsPost201Response  # noqa: F401
from openapi_server.models.new_group import NewGroup  # noqa: F401
from openapi_server.models.new_group_membership import NewGroupMembership  # noqa: F401
from openapi_server.models.update_group import UpdateGroup  # noqa: F401


def test_groups_get(client: TestClient):
    """Test case for groups_get

    Gets a list of Group objects
    """

    headers = {
    }
    response = client.request(
        "GET",
        "/groups",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_groups_id_delete(client: TestClient):
    """Test case for groups_id_delete

    Deletes a Group object
    """

    headers = {
    }
    response = client.request(
        "DELETE",
        "/groups/{id}".format(id='id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_groups_id_get(client: TestClient):
    """Test case for groups_id_get

    Gets a Group object by id
    """

    headers = {
    }
    response = client.request(
        "GET",
        "/groups/{id}".format(id='id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_groups_id_memberships_get(client: TestClient):
    """Test case for groups_id_memberships_get

    Gets a list of GroupMembership objects
    """

    headers = {
    }
    response = client.request(
        "GET",
        "/groups/{id}/memberships".format(id='id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_groups_id_memberships_membership_id_delete(client: TestClient):
    """Test case for groups_id_memberships_membership_id_delete

    Deletes a GroupMembership object
    """

    headers = {
    }
    response = client.request(
        "DELETE",
        "/groups/{id}/memberships/{membershipId}".format(id='id_example', membershipId='membership_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_groups_id_memberships_membership_id_get(client: TestClient):
    """Test case for groups_id_memberships_membership_id_get

    Gets a GroupMembership object by id
    """

    headers = {
    }
    response = client.request(
        "GET",
        "/groups/{id}/memberships/{membershipId}".format(id='id_example', membershipId='membership_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_groups_id_memberships_post(client: TestClient):
    """Test case for groups_id_memberships_post

    Creates a new GroupMembership object
    """
    new_group_membership = {"user":"{}","group":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}

    headers = {
    }
    response = client.request(
        "POST",
        "/groups/{id}/memberships".format(id='id_example'),
        headers=headers,
        json=new_group_membership,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_groups_id_put(client: TestClient):
    """Test case for groups_id_put

    Updates a Group object
    """
    update_group = {"created_by":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","name":"Project Group"}

    headers = {
    }
    response = client.request(
        "PUT",
        "/groups/{id}".format(id='id_example'),
        headers=headers,
        json=update_group,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_groups_post(client: TestClient):
    """Test case for groups_post

    
    """
    new_group = null

    headers = {
    }
    response = client.request(
        "POST",
        "/groups",
        headers=headers,
        json=new_group,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

