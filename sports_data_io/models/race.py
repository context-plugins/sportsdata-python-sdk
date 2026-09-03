from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class Race(SdkBaseModel):
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

    broadcast: OptionalNullable[str] = Field(default=UNSET, alias="Broadcast")
    """The broadcast airing this race"""

    winner_id: OptionalNullable[int] = Field(default=UNSET, alias="WinnerID")
    """The unique ID of the driver who won this race"""

    pole_winner_id: OptionalNullable[int] = Field(default=UNSET, alias="PoleWinnerID")
    """The unique ID of the driver who won the qualifying pole"""

    is_in_progress: Optional[bool] = Field(default=UNSET, alias="IsInProgress")
    """Indicates whether this race is currently in progress"""

    is_over: Optional[bool] = Field(default=UNSET, alias="IsOver")
    """Indicates whether this race is over"""

    updated: OptionalNullable[str] = Field(default=UNSET, alias="Updated")
    """The date/time when this race was last updated"""

    created: OptionalNullable[str] = Field(default=UNSET, alias="Created")
    """The date/time when this race was created (in US Eastern Time)"""

    rescheduled_day: OptionalNullable[str] = Field(default=UNSET, alias="RescheduledDay")
    """The day that this is race is rescheduled for (if race was postponed)"""

    rescheduled_date_time: OptionalNullable[str] = Field(default=UNSET, alias="RescheduledDateTime")
    """The date/time that this is race is rescheduled for (if race was postponed)"""

    canceled: Optional[bool] = Field(default=UNSET, alias="Canceled")
    """Indicates whether this race has been canceled"""

    scheduled_laps: OptionalNullable[int] = Field(default=UNSET, alias="ScheduledLaps")
    """Number of laps scheduled for this race"""

    actual_laps: OptionalNullable[int] = Field(default=UNSET, alias="ActualLaps")
    """Total number of laps ran for this race"""


class RaceDict(TypedDict):
    race_id: NotRequired[int]
    series_id: NotRequired[int]
    series_name: NotRequired[str | None]
    season: NotRequired[int]
    name: NotRequired[str | None]
    day: NotRequired[str | None]
    date_time: NotRequired[str | None]
    track: NotRequired[str | None]
    broadcast: NotRequired[str | None]
    winner_id: NotRequired[int | None]
    pole_winner_id: NotRequired[int | None]
    is_in_progress: NotRequired[bool]
    is_over: NotRequired[bool]
    updated: NotRequired[str | None]
    created: NotRequired[str | None]
    rescheduled_day: NotRequired[str | None]
    rescheduled_date_time: NotRequired[str | None]
    canceled: NotRequired[bool]
    scheduled_laps: NotRequired[int | None]
    actual_laps: NotRequired[int | None]
