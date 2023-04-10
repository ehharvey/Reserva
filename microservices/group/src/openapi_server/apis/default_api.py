# coding: utf-8

from typing import Dict, List  # noqa: F401

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    Path,
    Query,
    Response,
    Security,
    status,
)

from openapi_server.models.extra_models import TokenModel  # noqa: F401
from openapi_server.models.groups_get200_response import GroupsGet200Response
from openapi_server.models.groups_id_get200_response import GroupsIdGet200Response
from openapi_server.models.groups_id_memberships_get200_response import GroupsIdMembershipsGet200Response
from openapi_server.models.groups_id_memberships_post201_response import GroupsIdMembershipsPost201Response
from openapi_server.models.new_group import NewGroup
from openapi_server.models.new_group_membership import NewGroupMembership
from openapi_server.models.update_group import UpdateGroup


router = APIRouter()


@router.get(
    "/groups",
    responses={
        200: {"model": GroupsGet200Response, "description": "OK"},
    },
    tags=["default"],
    summary="Gets a list of Group objects",
    response_model_by_alias=True,
)
async def groups_get(
) -> GroupsGet200Response:
    ...


@router.delete(
    "/groups/{id}",
    responses={
        204: {"description": "Deleted"},
    },
    tags=["default"],
    summary="Deletes a Group object",
    response_model_by_alias=True,
)
async def groups_id_delete(
    id: str = Path(None, description="", regex=r"^[a-z]+-[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$"),
) -> None:
    ...


@router.get(
    "/groups/{id}",
    responses={
        200: {"model": GroupsIdGet200Response, "description": "OK"},
    },
    tags=["default"],
    summary="Gets a Group object by id",
    response_model_by_alias=True,
)
async def groups_id_get(
    id: str = Path(None, description="", regex=r"^[a-z]+-[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$"),
) -> GroupsIdGet200Response:
    ...


@router.get(
    "/groups/{id}/memberships",
    responses={
        200: {"model": GroupsIdMembershipsGet200Response, "description": "OK"},
    },
    tags=["default"],
    summary="Gets a list of GroupMembership objects",
    response_model_by_alias=True,
)
async def groups_id_memberships_get(
    id: str = Path(None, description="", regex=r"^[a-z]+-[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$"),
) -> GroupsIdMembershipsGet200Response:
    ...


@router.delete(
    "/groups/{id}/memberships/{membershipId}",
    responses={
        204: {"description": "Deleted"},
        404: {"description": "Not Found"},
    },
    tags=["default"],
    summary="Deletes a GroupMembership object",
    response_model_by_alias=True,
)
async def groups_id_memberships_membership_id_delete(
    id: str = Path(None, description="", regex=r"^[a-z]+-[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$"),
    membershipId: str = Path(None, description="", regex=r"^[a-z]+-[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$"),
) -> None:
    ...


@router.get(
    "/groups/{id}/memberships/{membershipId}",
    responses={
        200: {"model": GroupsIdMembershipsPost201Response, "description": "OK"},
        404: {"description": "Not Found"},
    },
    tags=["default"],
    summary="Gets a GroupMembership object by id",
    response_model_by_alias=True,
)
async def groups_id_memberships_membership_id_get(
    id: str = Path(None, description="", regex=r"^[a-z]+-[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$"),
    membershipId: str = Path(None, description="", regex=r"^[a-z]+-[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$"),
) -> GroupsIdMembershipsPost201Response:
    ...


@router.post(
    "/groups/{id}/memberships",
    responses={
        201: {"model": GroupsIdMembershipsPost201Response, "description": "OK"},
    },
    tags=["default"],
    summary="Creates a new GroupMembership object",
    response_model_by_alias=True,
)
async def groups_id_memberships_post(
    id: str = Path(None, description="", regex=r"^[a-z]+-[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$"),
    new_group_membership: NewGroupMembership = Body(None, description=""),
) -> GroupsIdMembershipsPost201Response:
    ...


@router.put(
    "/groups/{id}",
    responses={
        200: {"model": GroupsIdGet200Response, "description": "OK"},
    },
    tags=["default"],
    summary="Updates a Group object",
    response_model_by_alias=True,
)
async def groups_id_put(
    id: str = Path(None, description="", regex=r"^[a-z]+-[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$"),
    update_group: UpdateGroup = Body(None, description=""),
) -> GroupsIdGet200Response:
    ...


@router.post(
    "/groups",
    responses={
        201: {"model": GroupsIdGet200Response, "description": "OK"},
    },
    tags=["default"],
    response_model_by_alias=True,
)
async def groups_post(
    new_group: NewGroup = Body(None, description=""),
) -> GroupsIdGet200Response:
    ...
