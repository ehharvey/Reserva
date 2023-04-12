# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class RecurringUnavailability(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    RecurringUnavailability - a model defined in OpenAPI

        item: The item of this RecurringUnavailability.
        start_date_time: The start_date_time of this RecurringUnavailability.
        end_date_time: The end_date_time of this RecurringUnavailability.
        type: The type of this RecurringUnavailability.
        recurrence: The recurrence of this RecurringUnavailability.
        id: The id of this RecurringUnavailability.
    """

    item: str = Field(alias="item")
    start_date_time: str = Field(alias="startDateTime")
    end_date_time: str = Field(alias="endDateTime")
    type: str = Field(alias="type")
    recurrence: str = Field(alias="recurrence")
    id: str = Field(alias="id")

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

    @validator("recurrence")
    def recurrence_pattern(cls, value):
        assert value is not None and re.match(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}T([01][0-9]|2[0-3]):(00|15|30|45):00$", value)
        return value

    @validator("id")
    def id_pattern(cls, value):
        assert value is not None and re.match(r"^[a-z]+-[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$", value)
        return value

RecurringUnavailability.update_forward_refs()