# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class GroupMembership(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    GroupMembership - a model defined in OpenAPI

        group: The group of this GroupMembership.
        user: The user of this GroupMembership.
        id: The id of this GroupMembership [Optional].
    """

    group: str = Field(alias="group")
    user: str = Field(alias="user")
    id: Optional[str] = Field(alias="id", default=None)

    @validator("group")
    def group_pattern(cls, value):
        assert value is not None and re.match(r"^[a-z]+-[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$", value)
        return value

    @validator("user")
    def user_pattern(cls, value):
        assert value is not None and re.match(r"^[a-z]+-[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$", value)
        return value

    @validator("id")
    def id_pattern(cls, value):
        assert value is not None and re.match(r"^[a-z]+-[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$", value)
        return value

GroupMembership.update_forward_refs()