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
from openapi_server.models.authentication_login_post201_response import AuthenticationLoginPost201Response
from openapi_server.models.authentication_login_post_request import AuthenticationLoginPostRequest


router = APIRouter()


@router.post(
    "/authentication/login",
    responses={
        201: {"model": AuthenticationLoginPost201Response, "description": "Authentication Passed"},
        401: {"description": "Authentication Failed"},
    },
    tags=["default"],
    response_model_by_alias=True,
)
async def authentication_login_post(
    authentication_login_post_request: AuthenticationLoginPostRequest = Body(None, description=""),
) -> AuthenticationLoginPost201Response:
    ...


@router.post(
    "/authentication/logout",
    responses={
        200: {"description": "Logout Successful"},
        401: {"description": "Authentication Failed"},
    },
    tags=["default"],
    response_model_by_alias=True,
)
async def authentication_logout_post(
    authentication_login_post201_response: AuthenticationLoginPost201Response = Body(None, description=""),
) -> None:
    ...


@router.put(
    "/authentication/validate",
    responses={
        200: {"description": "Authentication Token is valid"},
        401: {"description": "Authentication Failed"},
    },
    tags=["default"],
    response_model_by_alias=True,
)
async def authentication_validate_put(
    authentication_login_post201_response: AuthenticationLoginPost201Response = Body(None, description=""),
) -> None:
    ...
