# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.group import Group


class GroupsIdGet200Response(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    GroupsIdGet200Response - a model defined in OpenAPI

        group: The group of this GroupsIdGet200Response [Optional].
    """

    group: Optional[Group] = Field(alias="Group", default=None)

GroupsIdGet200Response.update_forward_refs()
