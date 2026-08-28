from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class RaceBasic2(SdkBaseModel):
    """RaceBasic object (Includes basic information such as RaceID, Day, DateTime, Updated, and Created)"""

    race_id: Optional[int] = Field(default=UNSET, alias="RaceID")
    """The unique ID of this race"""

    day: OptionalNullable[str] = Field(default=UNSET, alias="Day")
    """The day of this race"""

    date_time: OptionalNullable[str] = Field(default=UNSET, alias="DateTime")
    """The date/time of this race"""

    updated: OptionalNullable[str] = Field(default=UNSET, alias="Updated")
    """The date/time when this race was last updated"""

    created: OptionalNullable[str] = Field(default=UNSET, alias="Created")
    """The date/time when this race was created (in US Eastern Time)"""


class RaceBasic2Dict(TypedDict):
    race_id: NotRequired[int]
    day: NotRequired[str | None]
    date_time: NotRequired[str | None]
    updated: NotRequired[str | None]
    created: NotRequired[str | None]
