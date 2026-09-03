from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .betting_market3 import BettingMarket3, BettingMarket3Dict


class BettingEvent5(SdkBaseModel):
    betting_event_id: Optional[int] = Field(default=UNSET, alias="BettingEventID")
    """The unique ID assocated with the betting event"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """The name of this betting event"""

    season: OptionalNullable[int] = Field(default=UNSET, alias="Season")
    """The season of this betting event"""

    betting_event_type_id: Optional[int] = Field(default=UNSET, alias="BettingEventTypeID")
    """The ID associated with the type of betting event"""

    betting_event_type: OptionalNullable[str] = Field(default=UNSET, alias="BettingEventType")
    """Indicates the type of betting event"""

    start_date: OptionalNullable[str] = Field(default=UNSET, alias="StartDate")
    """The last day for betting on this event"""

    created: OptionalNullable[str] = Field(default=UNSET, alias="Created")
    """The date/time when this betting event was created (in US Eastern Time)"""

    updated: OptionalNullable[str] = Field(default=UNSET, alias="Updated")
    """The last updated date of this betting event"""

    race_id: OptionalNullable[int] = Field(default=UNSET, alias="RaceID")
    """The unique ID of the race tied to this event"""

    betting_markets: Optional[list[BettingMarket3]] = Field(default=UNSET, alias="BettingMarkets")
    """A list of the possible betting markets within a betting event"""


class BettingEvent5Dict(TypedDict):
    betting_event_id: NotRequired[int]
    name: NotRequired[str | None]
    season: NotRequired[int | None]
    betting_event_type_id: NotRequired[int]
    betting_event_type: NotRequired[str | None]
    start_date: NotRequired[str | None]
    created: NotRequired[str | None]
    updated: NotRequired[str | None]
    race_id: NotRequired[int | None]
    betting_markets: NotRequired[list[BettingMarket3 | BettingMarket3Dict]]
