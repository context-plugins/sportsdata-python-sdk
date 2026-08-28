from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class Event(SdkBaseModel):
    event_id: Optional[int] = Field(default=UNSET, alias="EventId")
    """The unique ID of this event"""

    league_id: Optional[int] = Field(default=UNSET, alias="LeagueId")
    """The unique ID of this event's MMA league"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """The full name of the event"""

    short_name: OptionalNullable[str] = Field(default=UNSET, alias="ShortName")
    """The short name of the event"""

    season: OptionalNullable[int] = Field(default=UNSET, alias="Season")
    """The season the event took place"""

    day: OptionalNullable[str] = Field(default=UNSET, alias="Day")
    """The date of the event"""

    date_time: OptionalNullable[str] = Field(default=UNSET, alias="DateTime")
    """The start time and day of the event"""

    status: OptionalNullable[str] = Field(default=UNSET, alias="Status")
    """Indicates the event's status. Possible values include: Scheduled, In Progress, Final, Suspended, Postponed,
    Canceled"""

    active: OptionalNullable[bool] = Field(default=UNSET, alias="Active")
    """Indicates if the event is active"""


class EventDict(TypedDict):
    event_id: NotRequired[int]
    league_id: NotRequired[int]
    name: NotRequired[str | None]
    short_name: NotRequired[str | None]
    season: NotRequired[int | None]
    day: NotRequired[str | None]
    date_time: NotRequired[str | None]
    status: NotRequired[str | None]
    active: NotRequired[bool | None]
