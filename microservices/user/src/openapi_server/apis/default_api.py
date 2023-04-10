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
from openapi_server.models.new_user import NewUser
from openapi_server.models.update_user import UpdateUser
from openapi_server.models.user import User
from openapi_server.models.users_user_id_groups_get200_response import UsersUserIdGroupsGet200Response


router = APIRouter()


@router.get(
    "/users/admins",
    responses={
        200: {"model": List[User], "description": "A list of admin users"},
    },
    tags=["default"],
    summary="Get all admin users",
    response_model_by_alias=True,
)
async def users_admins_get(
) -> List[User]:
    """Returns a list of all admin users."""
    ...


@router.post(
    "/users/admins",
    responses={
        201: {"model": User, "description": "The new admin user"},
        400: {"description": "Invalid input"},
    },
    tags=["default"],
    summary="Create a new admin user",
    response_model_by_alias=True,
)
async def users_admins_post(
    new_user: NewUser = Body(None, description=""),
) -> User:
    """Creates a new admin user account."""
    ...


@router.get(
    "/users",
    responses={
        200: {"model": List[User], "description": "A list of users"},
    },
    tags=["default"],
    summary="Get all users",
    response_model_by_alias=True,
)
async def users_get(
) -> List[User]:
    """Returns a list of all users."""
    ...


@router.post(
    "/users",
    responses={
        201: {"model": User, "description": "The new user"},
        400: {"description": "Invalid input"},
    },
    tags=["default"],
    summary="Create a new user",
    response_model_by_alias=True,
)
async def users_post(
    new_user: NewUser = Body(None, description=""),
) -> User:
    """Creates a new user account."""
    ...


@router.get(
    "/users/standard",
    responses={
        200: {"model": List[User], "description": "A list of standard users"},
    },
    tags=["default"],
    summary="Get all standard users",
    response_model_by_alias=True,
)
async def users_standard_get(
) -> List[User]:
    """Returns a list of all standard users."""
    ...


@router.post(
    "/users/standard",
    responses={
        201: {"model": User, "description": "The new standard user"},
        400: {"description": "Invalid input"},
    },
    tags=["default"],
    summary="Create a new standard user",
    response_model_by_alias=True,
)
async def users_standard_post(
    new_user: NewUser = Body(None, description=""),
) -> User:
    """Creates a new standard user account."""
    ...


@router.delete(
    "/users/{userId}",
    responses={
        204: {"description": "User deleted"},
        404: {"description": "User not found"},
    },
    tags=["default"],
    summary="Delete a user by ID",
    response_model_by_alias=True,
)
async def users_user_id_delete(
    userId: int = Path(None, description="The ID of the user to delete."),
) -> None:
    """Deletes an existing user account."""
    ...


@router.get(
    "/users/{userId}",
    responses={
        200: {"model": User, "description": "The requested user"},
        404: {"description": "User not found"},
    },
    tags=["default"],
    summary="Get a user by ID",
    response_model_by_alias=True,
)
async def users_user_id_get(
    userId: int = Path(None, description="The ID of the user to retrieve."),
) -> User:
    """Returns a single user by ID."""
    ...


@router.get(
    "/users/{userId}/groups",
    responses={
        200: {"model": UsersUserIdGroupsGet200Response, "description": "A list of groups"},
    },
    tags=["default"],
    summary="Get all groups for a user",
    response_model_by_alias=True,
)
async def users_user_id_groups_get(
    userId: int = Path(None, description="The ID of the user to retrieve groups for."),
) -> UsersUserIdGroupsGet200Response:
    """Returns a list of all groups for a user."""
    ...


@router.put(
    "/users/{userId}",
    responses={
        200: {"model": User, "description": "The updated user"},
        400: {"description": "Invalid input"},
        404: {"description": "User not found"},
    },
    tags=["default"],
    summary="Update a user by ID",
    response_model_by_alias=True,
)
async def users_user_id_put(
    userId: int = Path(None, description="The ID of the user to update."),
    update_user: UpdateUser = Body(None, description=""),
) -> User:
    """Updates an existing user account."""
    ...
