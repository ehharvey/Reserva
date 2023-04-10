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
from openapi_server.models.unavailabilities_get200_response import UnavailabilitiesGet200Response
from openapi_server.models.unavailabilities_id_delete200_response import UnavailabilitiesIdDelete200Response
from openapi_server.models.unavailabilities_id_get200_response import UnavailabilitiesIdGet200Response
from openapi_server.models.unavailabilities_id_get400_response import UnavailabilitiesIdGet400Response
from openapi_server.models.unavailabilities_id_put200_response import UnavailabilitiesIdPut200Response
from openapi_server.models.unavailabilities_post_request import UnavailabilitiesPostRequest


router = APIRouter()


@router.get(
    "/unavailabilities",
    responses={
        200: {"model": UnavailabilitiesGet200Response, "description": "OK"},
    },
    tags=["default"],
    response_model_by_alias=True,
)
async def unavailabilities_get(
) -> UnavailabilitiesGet200Response:
    """Retrieve all unavailability associated with a student or a room."""
    ...


@router.delete(
    "/unavailabilities/{id}",
    responses={
        200: {"model": UnavailabilitiesIdDelete200Response, "description": "Deleted"},
        400: {"model": object, "description": "Bad Request"},
    },
    tags=["default"],
    response_model_by_alias=True,
)
async def unavailabilities_id_delete(
    id: str = Path(None, description="The unavailability ID", regex=r"^[a-z]+-[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$"),
) -> UnavailabilitiesIdDelete200Response:
    """Delete a specific unavailability identified by the &#x60;id&#x60; parameter."""
    ...


@router.get(
    "/unavailabilities/{id}",
    responses={
        200: {"model": UnavailabilitiesIdGet200Response, "description": "OK"},
        400: {"model": UnavailabilitiesIdGet400Response, "description": "Bad Request"},
    },
    tags=["default"],
    response_model_by_alias=True,
)
async def unavailabilities_id_get(
    id: str = Path(None, description="The unavailability ID", regex=r"^[a-z]+-[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$"),
) -> UnavailabilitiesIdGet200Response:
    """Retrieves information about a specific unavailability identified by the &#x60;id&#x60; parameter."""
    ...


@router.put(
    "/unavailabilities/{id}",
    responses={
        200: {"model": UnavailabilitiesIdPut200Response, "description": "OK"},
        400: {"model": object, "description": "Bad Request"},
    },
    tags=["default"],
    response_model_by_alias=True,
)
async def unavailabilities_id_put(
    id: str = Path(None, description="The unavailability ID", regex=r"^[a-z]+-[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$"),
) -> UnavailabilitiesIdPut200Response:
    """Update a specific unavailability identified by the &#x60;id&#x60; parameter with the information  provided in the request body. """
    ...


@router.post(
    "/unavailabilities",
    responses={
        201: {"model": str, "description": "Created"},
        400: {"model": str, "description": "Bad Request"},
    },
    tags=["default"],
    response_model_by_alias=True,
)
async def unavailabilities_post(
    unavailabilities_post_request: UnavailabilitiesPostRequest = Body(None, description=""),
) -> str:
    ...
