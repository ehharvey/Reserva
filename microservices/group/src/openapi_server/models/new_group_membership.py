# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.created_by import CreatedBy


class NewGroupMembership(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    NewGroupMembership - a model defined in OpenAPI

        group: The group of this NewGroupMembership.
        user: The user of this NewGroupMembership.
    """

    group: str = Field(alias="group")
    user: CreatedBy = Field(alias="user")

    @validator("group")
    def group_pattern(cls, value):
        assert value is not None and re.match(r"^[a-z]+-[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$", value)
        return value

NewGroupMembership.update_forward_refs()