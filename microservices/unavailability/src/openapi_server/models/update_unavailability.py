# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class UpdateUnavailability(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    UpdateUnavailability - a model defined in OpenAPI

        item: The item of this UpdateUnavailability [Optional].
        start_date_time: The start_date_time of this UpdateUnavailability [Optional].
        end_date_time: The end_date_time of this UpdateUnavailability [Optional].
        type: The type of this UpdateUnavailability [Optional].
    """

    item: Optional[str] = Field(alias="item", default=None)
    start_date_time: Optional[str] = Field(alias="startDateTime", default=None)
    end_date_time: Optional[str] = Field(alias="endDateTime", default=None)
    type: Optional[str] = Field(alias="type", default=None)

    @validator("item")
    def item_pattern(cls, value):
        assert value is not None and re.match(r"^[a-z]+-[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$", value)
        return value

    @validator("start_date_time")
    def start_date_time_pattern(cls, value):
        assert value is not None and re.match(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}T([01][0-9]|2[0-3]):(00|15|30|45):00$", value)
        return value

    @validator("end_date_time")
    def end_date_time_pattern(cls, value):
        assert value is not None and re.match(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}T([01][0-9]|2[0-3]):(00|15|30|45):00$", value)
        return value

UpdateUnavailability.update_forward_refs()