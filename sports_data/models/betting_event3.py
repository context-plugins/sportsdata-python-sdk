from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .betting_market2 import BettingMarket2, BettingMarket2Dict


class BettingEvent3(SdkBaseModel):
    betting_event_id: Optional[int] = Field(default=UNSET, alias="BettingEventId")
    """The unique ID associated with the betting event"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """The name of the betting event"""

    betting_event_type_id: Optional[int] = Field(default=UNSET, alias="BettingEventTypeID")
    """The ID associated with the type of betting event"""

    betting_event_type: OptionalNullable[str] = Field(default=UNSET, alias="BettingEventType")
    """Indicates the type of betting event"""

    start_date: OptionalNullable[str] = Field(default=UNSET, alias="StartDate")
    """The start date of this betting event"""

    created: OptionalNullable[str] = Field(default=UNSET, alias="Created")
    """The timestamp of when the betting event was created"""

    updated: OptionalNullable[str] = Field(default=UNSET, alias="Updated")
    """The last updated date of this betting event (in US Eastern Time)"""

    fight_id: OptionalNullable[int] = Field(default=UNSET, alias="FightId")
    """The unique ID of the fight related to the betting event"""

    betting_markets: Optional[list[BettingMarket2]] = Field(default=UNSET, alias="BettingMarkets")
    """A list of possible betting markets found within the betting event"""


class BettingEvent3Dict(TypedDict):
    betting_event_id: NotRequired[int]
    name: NotRequired[str | None]
    betting_event_type_id: NotRequired[int]
    betting_event_type: NotRequired[str | None]
    start_date: NotRequired[str | None]
    created: NotRequired[str | None]
    updated: NotRequired[str | None]
    fight_id: NotRequired[int | None]
    betting_markets: NotRequired[list[BettingMarket2 | BettingMarket2Dict]]
