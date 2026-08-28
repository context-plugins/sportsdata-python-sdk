from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .driver_race_odd import DriverRaceOdd, DriverRaceOddDict


class RaceOdds(SdkBaseModel):
    race_id: Optional[int] = Field(default=UNSET, alias="RaceID")
    """The unique ID of this race"""

    series_id: Optional[int] = Field(default=UNSET, alias="SeriesID")
    """The unique ID of the series that this race is associated with"""

    series_name: OptionalNullable[str] = Field(default=UNSET, alias="SeriesName")
    """The name of the series that this race is associated with"""

    season: Optional[int] = Field(default=UNSET, alias="Season")
    """The season that this race is associated with"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """The name of this race"""

    day: OptionalNullable[str] = Field(default=UNSET, alias="Day")
    """The day of this race"""

    date_time: OptionalNullable[str] = Field(default=UNSET, alias="DateTime")
    """The date/time of this race"""

    track: OptionalNullable[str] = Field(default=UNSET, alias="Track")
    """The name of the track for this race"""

    is_in_progress: OptionalNullable[bool] = Field(default=UNSET, alias="IsInProgress")
    """Indicates whether this race is currently in progress"""

    is_over: OptionalNullable[bool] = Field(default=UNSET, alias="IsOver")
    """Indicates whether this race is over"""

    pre_game_odds: Optional[list[DriverRaceOdd]] = Field(default=UNSET, alias="PreGameOdds")
    """List of the odds leading up to the start of the race"""


class RaceOddsDict(TypedDict):
    race_id: NotRequired[int]
    series_id: NotRequired[int]
    series_name: NotRequired[str | None]
    season: NotRequired[int]
    name: NotRequired[str | None]
    day: NotRequired[str | None]
    date_time: NotRequired[str | None]
    track: NotRequired[str | None]
    is_in_progress: NotRequired[bool | None]
    is_over: NotRequired[bool | None]
    pre_game_odds: NotRequired[list[DriverRaceOdd | DriverRaceOddDict]]
