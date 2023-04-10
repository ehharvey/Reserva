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
from openapi_server.models.items_get200_response import ItemsGet200Response
from openapi_server.models.items_id_get200_response import ItemsIdGet200Response
from openapi_server.models.items_id_put200_response import ItemsIdPut200Response
from openapi_server.models.update_item import UpdateItem


router = APIRouter()


@router.delete(
    "/items/{id}",
    responses={
        204: {"description": "Deleted"},
        404: {"description": "Item Not Found "},
    },
    tags=["default"],
    summary="Delete a Room object existing in the Rooms resources",
    response_model_by_alias=True,
)
async def delete_room_id(
    id:  = Path(None, description="User ID"),
) -> None:
    """## More Information Request for &#x60;DELETE/rooms/{id}&#x60; requires an id """
    ...


@router.get(
    "/items",
    responses={
        200: {"model": ItemsGet200Response, "description": "OK"},
    },
    tags=["default"],
    summary="Gets a list of items. For now, the only kind of item is a room.",
    response_model_by_alias=True,
)
async def items_get(
) -> ItemsGet200Response:
    ...


@router.get(
    "/items/{id}",
    responses={
        200: {"model": ItemsIdGet200Response, "description": "OK"},
        404: {"description": "Item Not Found "},
    },
    tags=["default"],
    summary="Gets a Item object by id. For now, the only kind of item is a room.",
    response_model_by_alias=True,
)
async def items_id_get(
    id:  = Path(None, description="", regex=r"^[a-z]+-[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$"),
) -> ItemsIdGet200Response:
    ...


@router.put(
    "/items/{id}",
    responses={
        200: {"model": ItemsIdPut200Response, "description": "OK"},
        404: {"description": "Item Not Found "},
    },
    tags=["default"],
    summary="Updates an item. For now, the only kind of item is a room.",
    response_model_by_alias=True,
)
async def items_id_put(
    id:  = Path(None, description="User ID"),
    body:  = Body(None, description=""),
) -> ItemsIdPut200Response:
    ...


@router.post(
    "/items",
    responses={
        201: {"model": ItemsIdGet200Response, "description": "Created"},
        400: {"description": "Bad Request "},
    },
    tags=["default"],
    summary="Posts an item. For now, the only kind of item is a room.",
    response_model_by_alias=True,
)
async def items_post(
    body:  = Body(None, description=""),
) -> ItemsIdGet200Response:
    ...
