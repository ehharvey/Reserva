# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class UpdateItem(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    UpdateItem - a model defined in OpenAPI

        name: The name of this UpdateItem [Optional].
        location: The location of this UpdateItem [Optional].
        description: The description of this UpdateItem [Optional].
        type: The type of this UpdateItem [Optional].
        features: The features of this UpdateItem [Optional].
    """

    name: Optional[object] = Field(alias="name", default=None)
    location: Optional[object] = Field(alias="location", default=None)
    description: Optional[object] = Field(alias="description", default=None)
    type: Optional[object] = Field(alias="type", default=None)
    features: Optional[object] = Field(alias="features", default=None)

UpdateItem.update_forward_refs()