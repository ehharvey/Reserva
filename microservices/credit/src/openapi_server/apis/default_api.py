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
from openapi_server.models.credit import Credit
from openapi_server.models.error import Error
from openapi_server.models.new_credit import NewCredit
from openapi_server.models.update_credit_by_id_request import UpdateCreditByIdRequest


router = APIRouter()


@router.post(
    "/credits",
    responses={
        201: {"model": Credit, "description": "Successfully created a new credit."},
        401: {"model": Error, "description": "Authentication token is missing or invalid."},
    },
    tags=["default"],
    summary="Create a new credit",
    response_model_by_alias=True,
)
async def create_credit(
    new_credit: NewCredit = Body(None, description=""),
) -> Credit:
    ...


@router.delete(
    "/credits/{creditId}",
    responses={
        204: {"description": "Successfully deleted the credit."},
        401: {"description": "Authentication token is missing or invalid."},
        404: {"model": Error, "description": "Credit not found."},
    },
    tags=["default"],
    summary="Delete a credit by ID",
    response_model_by_alias=True,
)
async def delete_credit_by_id(
    creditId: int = Path(None, description="The ID of the credit to delete.", ge=1),
) -> None:
    ...


@router.get(
    "/credits/{creditId}",
    responses={
        200: {"model": Credit, "description": "Successfully retrieved the credit."},
        401: {"description": "Authentication token is missing or invalid."},
        404: {"model": Error, "description": "Credit not found."},
    },
    tags=["default"],
    summary="Get a credit by ID",
    response_model_by_alias=True,
)
async def get_credit_by_id(
    creditId: int = Path(None, description="The ID of the credit to retrieve.", ge=1),
) -> Credit:
    ...


@router.get(
    "/credits",
    responses={
        200: {"model": List[Credit], "description": "Successfully retrieved all credits."},
        401: {"description": "Authentication token is missing or invalid."},
    },
    tags=["default"],
    summary="Get all credits",
    response_model_by_alias=True,
)
async def get_credits(
) -> List[Credit]:
    ...


@router.patch(
    "/credits/{creditId}",
    responses={
        200: {"model": Credit, "description": "Successfully updated the credit."},
        401: {"description": "Authentication token is missing or invalid."},
        404: {"model": Error, "description": "Credit not found."},
    },
    tags=["default"],
    summary="Update a credit by ID",
    response_model_by_alias=True,
)
async def update_credit_by_id(
    creditId: int = Path(None, description="The ID of the credit to update.", ge=1),
    update_credit_by_id_request: UpdateCreditByIdRequest = Body(None, description=""),
) -> Credit:
    ...
