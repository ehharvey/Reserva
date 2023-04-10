# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class UnavailabilitiesIdGet400Response(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    UnavailabilitiesIdGet400Response - a model defined in OpenAPI

        message: The message of this UnavailabilitiesIdGet400Response [Optional].
    """

    message: Optional[str] = Field(alias="message", default=None)

UnavailabilitiesIdGet400Response.update_forward_refs()
