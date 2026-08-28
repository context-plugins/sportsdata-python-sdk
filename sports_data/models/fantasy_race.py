from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class FantasyRace(SdkBaseModel):
    driver_id: Optional[int] = Field(default=UNSET, alias="DriverID")
    """The unique ID of this driver (assigned by SportsDataIO)"""

    season: Optional[int] = Field(default=UNSET, alias="Season")
    """The season that this race is associated with"""

    day: OptionalNullable[str] = Field(default=UNSET, alias="Day")
    """The day of this race"""

    date_time: OptionalNullable[str] = Field(default=UNSET, alias="DateTime")
    """The date/time of this race"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """The name of this race"""

    fantasy_points: OptionalNullable[float] = Field(default=UNSET, alias="FantasyPoints")
    """The fantasy points scored by this driver"""

    fantasy_points_draft_kings: OptionalNullable[float] = Field(default=UNSET, alias="FantasyPointsDraftKings")
    """The fantasy points scored by this driver, according to the DraftKings scoring system"""

    updated: OptionalNullable[str] = Field(default=UNSET, alias="Updated")
    """The date/time when this race was last updated"""


class FantasyRaceDict(TypedDict):
    driver_id: NotRequired[int]
    season: NotRequired[int]
    day: NotRequired[str | None]
    date_time: NotRequired[str | None]
    name: NotRequired[str | None]
    fantasy_points: NotRequired[float | None]
    fantasy_points_draft_kings: NotRequired[float | None]
    updated: NotRequired[str | None]
